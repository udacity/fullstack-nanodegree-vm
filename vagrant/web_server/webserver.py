#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Restaurant
import cgi

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        output = ''

        try:
            if self.path.endswith('/restaurants'):
                restaurants = session.query(Restaurant).all()

                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output += '<html><body>'
                output += '<h1>Restaurant</h1>'
                output += '<h2><a href="/restaurant/new">Create New ' \
                          'Restaurant</a></h2>'

                for restaurant in restaurants:
                    output += restaurant.name
                    output += '</br><a href="/restaurants/%s/edit">edit</a>' % restaurant.id
                    output += '</br><a href="/restaurants/%s/delete">delete</a></br>' % restaurant.id

                output += '</body></html>'
                self.wfile.write(output)
                return

            if self.path.endswith('/new'):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = ''
                output += '''
                    <html>
                        <body>
                            <h1>Make a New Restaurant</h1>
                            <form method="POST" enctype="multipart/form-data" 
                            action="restaurants/new">
                                <input type="text" placeholder="New Restaurant Name" name="name">
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                    </html>
                '''

                self.wfile.write(output)
                return

            if self.path.endswith('/edit'):
                id = self.path.split('/')[2]
                match = session.query(Restaurant).filter_by(id = id).one()

                if match:
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html')
                    self.end_headers()

                    output = ''
                    output += '<html><body>'
                    output += '<h1> %s </h1>' % match.name
                    output += "<form method='POST' " \
                              "enctype='multipart/form-data' action = " "'/restaurants/%s/edit' >" % id
                    output += "<input name = 'name' type='text' " \
                              "placeholder = '%s' >" % match.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
                    return

            if self.path.endswith('/delete'):
                id = self.path.split('/')[2]
                match = session.query(Restaurant).filter_by(id = id).one()

                if match:
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html')
                    self.end_headers()

                    output = ''
                    output += '<html><body>'
                    output += '<h2>Are you sure to delete %s ?</h2>' % \
                              match.name
                    output += '''
                        <form method="POST" enctype="multipart/form-data" 
                            action="/restaurants/%s/delete">
                            ''' % match.id
                    output += '<input type="hidden" name="delete_id" ' \
                              'value="%s">' % match.id
                    output += '''
                        
                            <button type="submit">Delete</button>
                        </form>
                        </body>
                        </html>
                    '''

                    self.wfile.write(output)
                    return


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        try:
            if self.path.endswith('/new'):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type')
                )

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    name = fields.get('name')

                    new_restaurant = Restaurant(name = name[0])
                    session.add(new_restaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-Type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type')
                )

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    new_name = fields.get('name')
                    id = self.path.split('/')[2]

                    new_restaurant_name = session.query(
                        Restaurant).filter_by(id = id).one()
                    new_restaurant_name.name = new_name[0]
                    session.add(new_restaurant_name)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-Type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith('/delete'):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type')
                )

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    delete_id = fields.get('delete_id')

                    query = session.query(Restaurant).filter_by(
                        id = delete_id[0]).one()
                    session.delete(query)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-Type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print('Serve running on: %s' % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C entered, stopping web server...')
        server.close()


if __name__ == '__main__':
    main()
