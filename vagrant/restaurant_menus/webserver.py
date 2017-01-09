from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import cgi


# Create database
engine = create_engine('sqlite:///restaurantmenu.db')
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


class webserverHandler(BaseHTTPRequestHandler):
    """docstring for webserverHandler"""
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
                           "type='submit' value='Submit'> </form>")
                send_get_response(output)
                return

            if self.path.endswith("/hola"):
                # Handler for hola page
                output = ""
                output += ("&#161Hola! <a href = '/hello' > Back "
                           "to Hello </a>")
                output += ("<form method='POST' enctype='multipart/form-data' "
                           "action='/hello'><h2>What would you like me to say?"
                           "</h2><input name='message' type='text' ><input "
                           "type='submit' value='Submit'> </form>")
                send_get_response(output)
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

            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += ("<form method='POST' enctype='multipart/form-data' "
                       "action='/hello'><h2>What would you like me to say?"
                       "</h2><input name='message' type='text' ><input "
                       "type='submit' value='Submit'> </form>")
            
            output += "</body></html>"
            self.wfile.write(output)
            print output


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