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

            """if self.path.endswith(".css"):
                f = open(curdir+sep+self.path)
                print "\n\n\n"+ curdir + "  " + sep + "  " + self.path
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            """

            if self.path.endswith("/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = HTML_HEADER + RESTAURANT_LAYOUT
                output += RESTAURANT_NEW
                output += RESTAURANT_LAYTOUT_E + PAGE_CLOSER
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/edit"):
                get_id = self.path[ self.path.find("/") + 1 : self.path.find("/", self.path.find("/") + 1 ) ]
                print get_id+"\n\n"
                session = dbConnect()
                isaRestaurant = session.query(Restaurant).filter_by(id = int(get_id) ).first()
                if isaRestaurant is not None:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = HTML_HEADER + RESTAURANT_LAYOUT
                    output += RESTAURANT_EDIT
                    output +="<h2>Modificando restaurante" + isaRestaurant.name
                    output += " (" + str(isaRestaurant.id) +"). </h2>"
                    output += RESTAURANT_EDIT_FORM
                    output += RESTAURANT_LAYTOUT_E + PAGE_CLOSER
                    self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            # Code for new restaurant
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                form_new_name = fields.get('restaurant-new')
                form_edit_name = fields.get('restaurant-edit')
            session= dbConnect()

            if form_new_name is not None:
                new_restaurant = Restaurant(name = form_new_name[0] )
                new_restaurant.add(session)
                aux = new_restaurant.find(session)
                output = HTML_HEADER + RESTAURANT_LAYOUT
                output += "<h1> Restaurant " + new_restaurant.find(session).name + " added</h1>"
                output += "<h2>Restaurant id is" + str(new_restaurant.find(session).id)
                output += "</h2>"
                output += RESTAURANT_LAYTOUT_E + PAGE_CLOSER

            elif form_edit_name is not None:
                get_id = self.path[ self.path.find("/") + 1 : self.path.find("/", self.path.find("/") + 1 ) ]
                this_restaurant = session.query(Restaurant).filter_by(id = int(get_id) ).one()
                output = HTML_HEADER + RESTAURANT_LAYOUT
                output += "<h1> Changed Restaurant name from " + this_restaurant.name +"</h1>"
                this_restaurant.update(session, form_edit_name[0])
                output += "<h1>to  "+ this_restaurant.name + " </h1>"
                output += "<h2>Restaurant id is " + str(this_restaurant.id)
                output += "</h2>"
                output += RESTAURANT_LAYTOUT_E + PAGE_CLOSER
            self.wfile.write(output)
            print output
        except:
            pass

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
