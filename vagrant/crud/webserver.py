from http.server import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Restaurant, MenuItem
import cgi
import re


class webserverHandler(BaseHTTPRequestHandler):

    def __open_sql_session(self):        
        engine = create_engine('sqlite:///restaurantmenu.db')
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind = engine)
        session = DBSession()
        return session
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        try:
            split_path = self.path.split('/')
            print(split_path)
            if self.path.endswith('/hello'):
                self._set_headers()
                output = '<html><body>Hello!'
                output += '<form method="POST" enctype="multipart/form-data" '
                output += 'action="/hello">'
                output += '<h2>What would you like me to say?</h2>'
                output += '<input name="message" type="text">'
                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
            elif self.path.endswith('/hola'):
                self._set_headers()
                output = '<html><body>&#161Hola!'
                output += '<a href="/hello">Back to Hello</a>'
                output += '<form method="POST" enctype="multipart/form-data" '
                output += 'action="/hello">'
                output += '<h2>What would you like me to say?</h2>'
                output += '<input name="message" type="text">'
                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
            elif self.path.endswith('/restaurants'):
                self._set_headers()                    
                output = '<html><body><ul>'
                session = self.__open_sql_session()
                restaurants_list = session.query(Restaurant).all()
                for restaurant in restaurants_list:
                    rid = str(restaurant.id)
                    output += '<li>'
                    output += '<h2>'+restaurant.name+'</h2>'
                    output += '<h3><a href="/restaurants/'+rid+ \
                              '/edit">Edit</a></h3>'
                    output += '<h3><a href="#">Delete</a></h3>'
                    output += '</li>'
                output += '</ul></body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
            elif self.path.endswith('/restaurants/new'):
                self._set_headers()
                output = '<html><body>'
                output += '<form method="POST" enctype="multipart/form-data" '
                output += 'action="/restaurants">'
                output += '<h2>Write a new restaurant name please.</h2>'
                output += '<input name="restaurant_name" type="text">'
                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
            elif split_path[1] == 'restaurants' and split_path[3] == 'edit':
                rid = split_path[2]
                self._set_headers()
                output = '<html><body>'
                output += '<form method="POST" enctype="multipart/form-data" '
                output += 'action="/restaurants">'
                output += '<h2>Change the restaurant name.</h2>'
                output += '<input name="id" type="hidden" value="'+rid+'">'
                output += '<input name="new_restaurant_name" type="text">'
                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
        except IOError:
            self.send_error(404, 'File Not Found {}'.format(self.path))

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            if form.getvalue('message') is not None:
                output = ''
                output += '<html><body>'
                output += '<h2>Okay,</h2>'
                output += '<h1>{}</h1>'.format(form.getvalue("message"))
                output += '<form method="POST" enctype="multipart/form-data" '
                output += 'action="/hello">'
                output += '<h2>What would you like me to say?</h2>'
                output += '<input name="message" type="text">'
                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
            elif form.getvalue('restaurant_name') is not None:
                session = self.__open_sql_session()
                restaurant_object = Restaurant(
                    name=form.getvalue('restaurant_name'))
                session.add(restaurant_object)
                session.commit()
            elif form.getvalue('new_restaurant_name') is not None:
                print(form.getvalue('id'), form.getvalue('new_restaurant_name'))
                session = self.__open_sql_session()
                restaurant = session.query(Restaurant).get(form.getvalue('id'))
                restaurant.name = form.getvalue('new_restaurant_name')
                session.commit()
        except Exception as exc:
            print(exc)

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print('WebServer: Server running on port {}'.format(port))
        server.serve_forever()
    except KeyboardInterrupt:
        print('WebServer: ^C entered, stopping web server')
        pass

if __name__ == '__main__':
    main()