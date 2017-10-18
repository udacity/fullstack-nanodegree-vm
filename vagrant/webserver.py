#!/usr/bin/env python2.7
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_initial import Base, Restaurant, MenuItem

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/restaurants":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            restaurants = session.query(Restaurant).all()
            output = ""
            output += "<html><body>"
            output += "<a href='/restaurants/new'> Make a New Restaurant </a>"
            output += "<br><br><br>"

            for restaurant in restaurants:
                output += restaurant.name
                output += "<br>"
                output += "<a href='/restaurants/%s/edit'> Edit </a>" % restaurant.id
                output += "<br>"
                output += "<a href='/restaurants/%s/delete'> Delete </a>" % restaurant.id
                output += "<br><br><br>"

            output += "</body></html>"
            self.wfile.write(output.encode())

        if self.path == "/restaurants/new":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += " <h2> Enter new Restaurant Name: </h2>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants'>
                            <input name="restaurant_name" type="text" >
                            <input type="submit" value="Submit">
                        </form>'''
            output += "</body></html>"
            self.wfile.write(output.encode())

        # else:
        #     self.send_error(404, 'File Not Found: %s' % self.path)

        if self.path.endswith('/edit'):  # endswith identifies the last word in path
            myRestaurantPath = self.path.split('/')[2]
            myRestaurantId = session.query(Restaurant).filter_by(id=myRestaurantPath).one()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += ' <h2> %s </h2> ' % myRestaurantId.name
            output += "<br>"
            output += " <h4> Enter new Restaurant Name: </h4>"
            output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'> " % myRestaurantPath
            output += '<input name="my_restaurant_name" type="text" placeholder="%s" >' % myRestaurantId.name
            output += '<input type="submit" value="Submit">'
            output += '</form>'
            output += "</body></html>"
            self.wfile.write(output.encode())

        if self.path.endswith("/delete"):
            myRestaurantPath = self.path.split('/')[2]
            myRestaurantId = session.query(Restaurant).filter_by(id=myRestaurantPath).one()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1> Are you sure you want to delete %s ? </h1>" % myRestaurantId.name
            output += "<form method='POST' enctype = 'multipart/form-data' action = '/restaurants/%s/delete'>" % myRestaurantPath
            output += "<input type = 'submit' value = 'Yes'>"
            output += "</form>"
            output += "<a href='/restaurants'> No </a>"
            output += "</body></html>"
            self.wfile.write(output)

    def do_POST(self):
        if self.path == '/restaurants/new':
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('restaurant_name')

            # Creating new Restaurants
                new_restaurant = Restaurant(name=messagecontent[0])
                session.add(new_restaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

        if self.path.endswith('/edit'):
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('my_restaurant_name')
                myRestaurantPath = self.path.split('/')[2]
                myRestaurantId = session.query(Restaurant).filter_by(id=myRestaurantPath).one()

                # Editing Restaurants name
                if myRestaurantId:
                    myRestaurantId.name = messagecontent[0]
                    session.add(myRestaurantId)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        if self.path.endswith("/delete"):
            myRestaurantPath = self.path.split("/")[2]
            myRestaurantId = session.query(Restaurant).filter_by(id=myRestaurantPath).one()

            # Deleting Restaurant
            if myRestaurantId:
                session.delete(myRestaurantId)
                session.commit()
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    main()
