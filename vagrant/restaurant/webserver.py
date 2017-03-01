from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import func
from database_setup import Restaurant, MenuItem, engine


DBSession = sessionmaker(bind=engine)

session = DBSession()


def get_all_restaurants():
    allRestaurants = session.query(Restaurant).all()

    return allRestaurants


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'restaurantName' type = 'text' placeholder = 'Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants"):
                restaurants = get_all_restaurants()

                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"

                for r in restaurants:
                    output += "<span>%s<span>" % r.name
                    output += "</br>"
                    output += "<a href ='restaurants/%s/edit'>Edit</a>" % r.id
                    output += "</br>"
                    output += "<a href ='restaurants/%s/delete'>Delete</a>" % r.id
                    output += "</br></br></br></br>"

                output += "</body></html>"

                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantPathId = self.path.split("/")[2]
                restaurant = session.query(Restaurant).filter_by(id=restaurantPathId).one()

                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                if restaurant:
                    output = ""
                    output += "<html><body>"
                    output += "<h1>%s</h1>" % restaurant.name
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/%s/edit'>" % restaurant.id
                    output += "<input name = 'restaurantNewName' type = 'text' placeholder = 'Restaurant Name' > "
                    output += "<input type='submit' value='Edit'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
                    return

            if self.path.endswith("/delete"):
                restaurantPathId = self.path.split("/")[2]
                restaurant = session.query(Restaurant).filter_by(id=restaurantPathId).one()

                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                if restaurant:
                    output = ""
                    output += "<html><body>"
                    output += "<h1>%s</h1>" % restaurant.name
                    output += "<p>Are you sure you want to delete it?</p>"
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/%s/delete'>" % restaurant.id
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
                    return

        except IOError:
            self.send_error(404, "File not found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    content = fields.get('restaurantName')

                    newRestaurant = Restaurant(name=content[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    content = fields.get('restaurantNewName')

                    restaurantPathId = self.path.split("/")[2]
                    restaurant = session.query(Restaurant).filter_by(id=restaurantPathId).one()

                    if restaurant and content[0]:
                        restaurant.name = content[0]
                        session.add(restaurant)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/delete"):
                restaurantPathId = self.path.split("/")[2]
                restaurant = session.query(Restaurant).filter_by(id=restaurantPathId).one()

                if restaurant:
                    session.delete(restaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered stopping webserver"
        server.socket.close()


if __name__ == '__main__':
    main()
