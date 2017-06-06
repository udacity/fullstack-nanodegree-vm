#!/usr/bin python
# -*- coding: utf-8 -*-
# VAGRANT is set up to: localhost://18080

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.set_header(200)
                restaurants = session.query(Restaurant).all()
                output = "<html><body>"
                output += "<a href='/restaurants/new'>add new restaurant</a>"
                output += "<br><br>"
                for restaurant in restaurants:
                    output += "%s<br>" % (restaurant.name)
                    output += """<a href='/restaurants/%s/edit'>
                                edit</a><br>""" % (restaurant.id)
                    output += """<a href='/restaurants/%s/delete'>
                                delete</a><br>""" % (restaurant.id)
                    output += "<br>"
                output += "</body></html>"
                self.write_page(output)

            if self.path.endswith("/restaurants/new"):
                self.set_header(200)
                output = "<html><body>"
                output += '''<form method='POST' enctype='multipart/form-data'
                            action='/restaurants/new'><h2>Make a New Restaurant
                            </h2><input name="newRestaurant" type="text" >
                            <input type="submit" value="Create"> </form>'''
                output += "</body></html>"
                self.write_page(output)

            if self.path.endswith("/edit"):
                self.set_header(200)
                restaurant = self.get_by_urlID_from_table(Restaurant)
                output = "<html><body>"
                if restaurant:
                    output += '''<form method='POST' enctype='multipart/form-data'
                                action='/restaurants/%s/edit'><h2>Rename %s</h2>
                                <input name="newName" type="text" placeholder =
                                '%s' ><input type="submit" value="Update">
                                </form>''' % (restaurant.id, restaurant.name,
                              restaurant.name)
                else:
                    output += "<h1>There is no such Restaurant in our DB!</h1>"
                output += "</body></html>"
                self.write_page(output)

            if self.path.endswith("/delete"):
                self.set_header(200)
                restaurant = self.get_by_urlID_from_table(Restaurant)
                output = "<html><body>"
                if restaurant:
                    output += '''<form method='POST' enctype='multipart/form-data'
                                action='/restaurants/%s/delete'><h2>Are you sure
                                you want to delete %s?</h2>
                                <input name="delete" type="submit" value="Delete">
                                </form>''' % (restaurant.id, restaurant.name)
                else:
                    output += "<h1>There is no such Restaurant in our DB!</h1>"
                output += "</body></html>"
                self.write_page(output)

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                field_restaurant = self.get_fieldname("newRestaurant")
                if field_restaurant:
                    new_restaurant = Restaurant(name=field_restaurant)
                    session.add(new_restaurant)
                    session.commit()
                    self.redirect("/restaurants")
                else:
                    self.set_header(301)
                    output = "<html><body>"
                    output += "<h1> Make sure you give it a name! </h1>"
                    output += '''<form method='POST' enctype='multipart/form-data'
                                 action='/restaurants/new'><h2>Make a New Restaurant
                                 </h2><input name="restaurant" type="text" ><input
                                  type="submit" value="Create"> </form>'''
                    output += "</body></html>"
                    self.write_page(output)

            if self.path.endswith("/edit"):
                field_restaurant = self.get_fieldname("newName")
                if field_restaurant:
                    restaurant = self.get_by_urlID_from_table(Restaurant)
                    restaurant.name = field_restaurant
                    session.add(restaurant)
                    session.commit()
                    self.redirect("/restaurants")
                else:
                    self.set_header(301)
                    output = "<html><body>"
                    output += "<h2>empty name, not cool!"
                    output += "</body></html>"
                    self.write_page(output)

            if self.path.endswith("/delete"):
                restaurant = self.get_by_urlID_from_table(Restaurant)
                session.delete(restaurant)
                session.commit()
                self.redirect("/restaurants")

        except:
            pass

    def set_header(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()  # sends empty line to tell end of header

    def redirect(self, location):
        self.send_response(301)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', '%s' % location)
        self.end_headers()
        return

    def write_page(self, output):
        self.wfile.write(output)
        return

    def get_by_urlID_from_table(self, table):
        url_id = self.path.split("/")[-2]
        try:
            return session.query(table).filter_by(id=url_id).one()
        except:
            return None

    def get_fieldname(self, fieldname):
        ctype, pdict = cgi.parse_header(self.headers.getheader(
                                        'content-type'))
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            return fields.get(fieldname)[0]


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s") % port
        server.serve_forever()

    # interrupts if user hits 'strg + c'
    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
        main()
