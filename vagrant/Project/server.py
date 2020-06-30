from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurant/new"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h2> add a new restaurant idiot </h2>"

                output += "<form method=POST enctype='multipart/form-data' action='/restaurant/new'>"
                output += "<h2>Name?</h2>"
                output += "<input name='restaurant' type='text' placeholder='New Restaurant Name'>"
                output += "<input type='submit' value='submit'>"
                output += "</form></body></html>"

                self.wfile.write(output)
                # print(output)
                return

            if self.path.endswith("/edit"):
                ID = self.path.split("/")[2]
                restaurant = session.query(Restaurant).filter_by(id = ID).one()

                if restaurant:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h2>What will you rename this place?</h2>"

                    output += "<form method=POST enctype='multipart/form-data' action='/restaurant/%s/edit'>" % restaurant.id
                    output += "<input name='newName' type='text' placeholder='%s'>" % restaurant.name
                    output += "<input type='submit' value='submit'>"
                    output += "</form></body></html>"

                    self.wfile.write(output)
                # print(output)
                return
            
            if self.path.endswith("/delete"):
                ID = self.path.split("/")[2]
                restaurant = session.query(Restaurant).filter_by(id = ID).one()

                if restaurant:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<form method=POST enctype='multipart/form-data' action='/restaurant/%s/delete'>" % restaurant.id
                    output += "<h1>Are you sure you want to delete %s?</h1>" % restaurant.name
                    output += "<input type='submit' value='submit'>"
                    output += "</form></body></html>"

                    self.wfile.write(output)
                # print(output)
                return

            if self.path.endswith("/restaurant"):
                restaurants = session.query(Restaurant).all()
                output = ""
                output += "<a href = '/restaurant/new' > Make a New Restaurant Here </a></br></br>"

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output += "<html><body>"
                for rest in restaurants:
                    output += rest.name
                    output += "</br><a href='/restaurant/%s/edit'>Edit</a></br><a href='/restaurant/%s/delete'>Delete</a></br>"%(rest.id, rest.id,)
                output += "</body></html>"

                self.wfile.write(output)
                # print(output)
                return

        except IOError:
            self.send_error(404, "File not found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/edit"):

                ctype, pdict = cgi.parse_header(
                    self.headers.getheader("content-type"))
                if ctype == "multipart/form-data":
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get("newName")

                    ID = self.path.split("/")[2]
                    rest = session.query(Restaurant).filter_by(id=ID).one()
                    rest.name = messagecontent[0]
                    session.commit()

                    self.send_response(301)
                    self.send_header("Content-type", "text/html")
                    self.send_header("Location", "/restaurant")
                    self.end_headers()

                self.wfile.write(output)
                # print(output)
                return

            if self.path.endswith("/delete"):

                ctype, pdict = cgi.parse_header(
                    self.headers.getheader("content-type"))
                if ctype == "multipart/form-data":
                    ID = self.path.split("/")[2]
                    rest = session.query(Restaurant).filter_by(id=ID).one()
                    session.delete(rest)
                    session.commit()

                    self.send_response(301)
                    self.send_header("Content-type", "text/html")
                    self.send_header("Location", "/restaurant")
                    self.end_headers()

                self.wfile.write(output)
                # print(output)
                return

            if self.path.endswith("/restaurant/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader("content-type"))
                if ctype == "multipart/form-data":
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get("restaurant")

                    newRest = Restaurant(name=messagecontent[0])
                    session.add(newRest)
                    session.commit()

                    self.send_response(301)
                    self.send_header("Content-type", "text/html")
                    self.send_header("Location", "/restaurant")
                    self.end_headers()

                self.wfile.write(output)
                # print(output)
                return
        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(("", port), webserverHandler)
        print("Web server running on %s" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print("Web server closed")
        server.socket.close()


if __name__ == "__main__":
    main()
