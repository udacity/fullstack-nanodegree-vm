from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from database_connect import *
from html_strings import *


class webServerHandler(BaseHTTPRequestHandler):

    def print_restaurants(self, order):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #opens html
        output=HTML_HEADER + RESTAURANT_LAYOUT + RESTAURANT_TABLE
        #inputs content
        restaurant_list= Restaurant_list(order)
        for item in restaurant_list:
            output += "<tr><td>  " + str(item.id) + '''  </td><td class="restaurant-name"> ''' + item.name + "</td>"
            output += '''<td><a class="" role="button" href="/'''+ str(item.id) + '''/edit">Edit</a></td>'''
            output += '''<td><a class="" role="button" href="/'''+ str(item.id) + '''/delete">Delete</a></td></tr>'''
        #closes html and prints
        output += RESTAURNANT_TABLE_F + RESTAURANT_LAYTOUT_E +PAGE_CLOSER
        self.wfile.write(output)
        print output
        return


    def do_GET(self):
        try:
            if self.path.endswith("/restaurantOrdered"):
                order = True
                self.print_restaurants(order)
                return

            if self.path.endswith("/restaurant"):
                order = False
                self.print_restaurants(order)
                return

"""            if self.path.endswith(".css"):
                f = open(curdir+sep+self.path)
                print "\n\n\n"+ curdir + "  " + sep + "  " + self.path
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
"""
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

"""    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
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
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass
"""

def main():
    try:
        port = 8000
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
