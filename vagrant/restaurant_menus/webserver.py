from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import cgi


# Create database
engine = create_engine('sqlite:///restaurantmenu.db', echo=True)
Base.metadata.create_all(engine)

# Create database connector
DBSession = sessionmaker(bind = engine)
session = DBSession()

def html_wrapper(html):
    """
    Returns a string wrapper with <html><body></body></html>.

    >>> output = html_wrapper("hello")
    >>> print output
    >>> <html><body>hello</body></html>
    """
    output = "<html><body>"
    output += html
    output += "</body></html>"
    return output

class RestuarantsHandler(object):
    """Class for handling actions related to restaurants."""

    @classmethod
    def get_restaurants(cls):
        """Returns a list of all the restuarants."""
        return session.query(Restaurant).all()

    @classmethod
    def get_restaurant_by_id(cls, id):
        """
        Return a restaurant with the given id.

        id (int)
        """
        return session.query(Restaurant).filter_by(id = id).all()[0]

    @classmethod
    def add_restuarant(cls, name):
        """Adds a restuarant with the given name."""
        session.add(Restaurant(name = name))
        session.commit()

    @classmethod
    def rename_restaurant(cls, id, name):
        """
        Renames the restaurant with the given id to the given name.

        id (int)
        name (string)
        """
        restaurant = cls.get_restaurant_by_id(id)
        restaurant.name = name
        session.add(restaurant)
        session.commit()

    @classmethod
    def delete_restaurant(cls, id):
        """
        Deletes the restaurant with the given id.

        id (int)
        """
        print "deleting restaurant"
        restaurant = cls.get_restaurant_by_id(id)
        session.delete(restaurant)
        session.commit()
        print "restaurant deleted"


class webserverHandler(BaseHTTPRequestHandler):
    """docstring for webserverHandler"""
    def render_restaurants(self):
        """
        Returns as a string the html necessary for rendering the
        restaurants page.
        """

        # Get all the restaurants
        restuarants = RestuarantsHandler.get_restaurants()

        output = ""
        for restaurant in restuarants:
            output += "<h1>%s</h1>\n" % restaurant.name
            output += ('<a href="/restaurant/%s/edit">Edit'
                       '</a><br>' % restaurant.id)
            output += ('<a href="/restaurant/%s/delete">Delete'
                       '</a><br>' % restaurant.id)
        output += ('<h2><a href="/restaurants/new">Make a New '
                   'Restaurant Here.</a></h2>')
        html_output = html_wrapper(output)
        return html_output

    def send_get_response(self, output):
        """
        Sends a 200 response and text/html header, then sends and
        prints the given output.

        >>> send_get_response("<html><body>hello</body></html>")
        >>> <html><body>hello</body></html>
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html_output = html_wrapper(output)
        self.wfile.write(html_output)
        print html_output

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                # Handler for hello page
                output = ""
                output += "Hello!"
                output += ("<form method='POST' enctype='multipart/form-data' "
                           "action='/hello'><h2>What would you like me to say?"
                           "</h2><input name='message' type='text' ><input "
                           "type='hidden' name='form' value='hello'><input "
                           "type='submit' value='Submit'> </form>")
                self.send_get_response(output)
                return

            if self.path.endswith("/hola"):
                # Handler for hola page
                output = ""
                output += ("&#161Hola! <a href = '/hello' > Back "
                           "to Hello </a>")
                output += ("<form method='POST' enctype='multipart/form-data' "
                           "action='/hello'><h2>What would you like me to say?"
                           "</h2><input name='message' type='text' ><input "
                           "type='hidden' name='form' value='hello'><input "
                           "type='submit' value='Submit'> </form>")
                self.send_get_response(output)
                return

            if self.path.endswith("/restaurants"):
                # Handler for restuarants page

                output = self.render_restaurants()
                self.send_get_response(output)
                return

            if self.path.endswith("/restaurants/new"):
                # Handler for restuarants page

                output = ""
                output += "<h1>Make a New Restaurant</h1><br>"
                output += ("<form method='POST' enctype='multipart/form-data'"
                           "action='/restaurants'><input name='name' "
                           "type='text' ><input type='hidden' name='form' "
                           "value='new_restaurant'><input type='submit' "
                           "value='Create'>"
                           "</form>")
                self.send_get_response(output)
                return

            if self.path.endswith("/edit"):
                # Handler for editing a restaurants name
                rest_id = int(self.path.split('/')[2])
                restaurant = RestuarantsHandler.get_restaurant_by_id(rest_id)
                output = ""
                output += "<h1>%s</h1><br>" % restaurant.name
                output += "<h2>Rename?<h2><br>"
                output += ("<form method='POST' enctype='multipart/form-data'"
                           "action='/restaurants'><input name='name' "
                           "type='text' ><input type='hidden' name='form' "
                           "value='rename'><input type='hidden' "
                           "name='restaurant_id' value='%s'><input "
                           "type='submit' value='Rename'></form>" % rest_id)
                self.send_get_response(output)
                return

            if self.path.endswith("/delete"):
                # Handler for deleting a restaurant
                rest_id = int(self.path.split('/')[2])
                restaurant = RestuarantsHandler.get_restaurant_by_id(rest_id)
                output = ""
                output += "<h1>%s</h1><br>" % restaurant.name
                output += "<h2>Are You Sure You Want To Delete?<h2><br>"
                output += ("<form method='POST' enctype='multipart/form-data'"
                           "action='/restaurants'><input type='hidden' "
                           "name='form' value='delete'><input type='hidden' "
                           "name='restaurant_id' value='%s'><input "
                           "type='submit' value='Delete'>"
                           "</form><br>" % rest_id)
                self.send_get_response(output)
                return



        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
                formcontent = fields.get('form')
                namecontent = fields.get('name')
                restaurant_id = int(fields.get('restaurant_id')[0])

            print formcontent
            print "form content equals rename?"
            print formcontent[0] == 'rename'
            print namecontent
            print restaurant_id

            if formcontent[0] == 'hello':
                output = ""
                output += "<html><body>"
                output += " <h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]

                output += ("<form method='POST' enctype='multipart/form-data' "
                           "action='/hello'><h2>What would you like me to say?"
                           "</h2><input name='message' type='text' ><input "
                           "type='hidden' name='form' value='hello'><input "
                           "type='submit' value='Submit'> </form>")
            
                output += "</body></html>"
                self.wfile.write(output)
                print output

            if formcontent[0] == 'new_restaurant':
                # Add new restaurant
                RestuarantsHandler.add_restuarant(namecontent[0])

                # Render restaurants page
                output = self.render_restaurants()
                self.wfile.write(output)

            if formcontent[0] == 'rename':
                # Rename restaurant
                print "renaming"
                RestuarantsHandler.rename_restaurant(
                    restaurant_id, namecontent[0])

                # Render restaurants page
                output = self.render_restaurants()
                self.wfile.write(output)

            if formcontent[0] == 'delete':
                # Delete the restaurant
                print "deleting"

                RestuarantsHandler.delete_restaurant(restaurant_id)

                # Render restaurants page
                output = self.render_restaurants()
                self.wfile.write(output)



        except:
            pass
        

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping webserver..."
        server.socket.close()


if __name__ == '__main__':
    main()