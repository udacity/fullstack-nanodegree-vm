from os import sys
import logging, traceback
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine, Integer
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant
from urlparse import urlparse
import re

CONTENT_TYPE_TEXT_HTML = 'text/html'
ERROR_MISSIN_URL_PARAM = 'missing parameter in URL.'

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', CONTENT_TYPE_TEXT_HTML)
                self.end_headers()

                output = ""
                output += "<html><body>List of Restaurants:"

                restaurants = session.query(Restaurant).all()
                for restaurant in restaurants:
                    output += "<p>{}</p>".format(restaurant.name)
                    output += "<a href='/restaurants/{}/edit'>Edit</a>".format(restaurant.id)
                    output += "   "
                    output += "<a href='/restaurants/{}/delete'>Delete</a>".format(restaurant.id)
                
                output += "</br></br>"
                output += "<a href='/restaurants/new'>New</a></body></html>"

                self.wfile.write(output)
                return

            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Create New Restaurant"
                output += "  <form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
                output += "    <label>Restaurant name: <input name='newRestaurantName' type='text'></label>"
                output += "    <input type='submit' value='Submit'>"
                output += "  </form></body></html>"

                self.wfile.write(output)
                return

            if self.path.endswith('/edit'):
                return self.editRestaurant()

            if self.path.endswith('/delete'):
                module = re.search('.*/([0-9]+)/delete', self.path)
                if module:
                    rest_id = module.group(1)
                else:
                    raise AttributeError(ERROR_MISSIN_URL_PARAM)
                delete_restaurant = session.query(Restaurant).filter_by(id=rest_id).one()

                if delete_restaurant != []:
                    self.send_response(200)
                    self.send_header('Content-type', CONTENT_TYPE_TEXT_HTML)
                    self.end_headers()

                    output = ""
                    output += "<html><body>Delete Restaurant"
                    output += "  <form method='POST' enctype='multipart/form-data' action='/restaurants/{}/delete'>".format(delete_restaurant.id)
                    output += "    <label>Name: {}".format(delete_restaurant.name)
                    output += "    <input type='submit' value='Delete'></label>"
                    output += "  </form></body></html>"

                    self.wfile.write(output)
                return

        except Exception:
            print("system error: {}".format(sys.exc_info()))

    def editRestaurant(self):
        module = re.search('.*/([0-9]+)/edit', self.path)
        if module:
            rest_id = module.group(1)
        else:
            raise AttributeError('missing parameter in URL.')
        edit_restaurant = session.query(Restaurant).filter_by(id=rest_id).one()

        if edit_restaurant != []:
            self.send_response(200)
            self.send_header('Content-type', CONTENT_TYPE_TEXT_HTML)
            self.end_headers()

            output = ""
            output += "<html><body>Edit Restaurant"
            output += "  <form method='POST' enctype='multipart/form-data' action='/restaurants/{}/edit'>".format(edit_restaurant.id)
            output += "    <label>Name: <input name='editedRestaurantName' type='text' placeholder='{}'></label>".format(edit_restaurant.name) 
            output += "    <input type='submit' value='Submit'>"
            output += "  </form> </body></html>"

            self.wfile.write(output)

    def do_POST(self):
        try:
            self.log_request()
            if self.path.endswith('/restaurants/new'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                new_restaurant = Restaurant(name=messagecontent[0])
                session.add(new_restaurant)
                session.commit()

                self.restaurantsRedirect()

                return

            if self.path.endswith('/edit'):
                module = re.search('.*/([0-9]+)/edit', self.path)
                if module:
                    rest_id = module.group(1)
                else:
                    raise AttributeError(ERROR_MISSIN_URL_PARAM)

                print("Editing restaurant (ID:{})".format(rest_id))

                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('editedRestaurantName')
                print("editedRestaurantName='{}'".format(messagecontent[0]))

                restaurant = session.query(Restaurant).filter_by(id=rest_id).one()
                restaurant.name = messagecontent[0]
                session.add(restaurant)
                session.commit()

                self.restaurantsRedirect()

                return

            if self.path.endswith('/delete'):
                module = re.search('.*/([0-9]+)/delete', self.path)
                if module:
                    rest_id = module.group(1)
                else:
                    raise AttributeError(ERROR_MISSIN_URL_PARAM)

                delete_restaurant = session.query(Restaurant).filter_by(id=rest_id).one() 
                session.delete(delete_restaurant)
                session.commit()

                self.restaurantsRedirect()
                return
            
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stderr)
            session.rollback()
            #self.send_header(404, 'File Not Found {}'.format(self.path))

    def restaurantsRedirect(self):
        self.send_response(301)
        self.send_header('Content-type', CONTENT_TYPE_TEXT_HTML)
        self.send_header('Location', '/restaurants')
        self.end_headers()

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print('Web server running on port {}'.format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C entered, stopping web server...')
        server.socket.close()

if __name__ == '__main__':
    main()