from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi


## import CRUD operations form Lesson 1
from database_setup import Restaurant, Base, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

## Create session an dconnect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
 

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output = ""
                output += "<html><body>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
                output +=        "<h1>Make a new restaurant</h1>"
                output +=        "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>"
                output +=        "<input type='submit' value='Create'></form>"
                output +="</body></html>"
                
                self.wfile.write(output)
                print output
                return
                
                
            if self.path.endswith('/edit'):
                #get ID from path
                restaurantIDPath = self.path.split('/')[2]
                #query restaurants, filter by id, result must be ONE!! 
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                if myRestaurantQuery != []
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    output ="<html><body>"
                    output +=        "<h1>%s</h1>" % myRestaurantQuery.name
                    output +=   "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath
                    output +=        "<input name='newRestaurantName' type='text' placeholder='%s'>" % myRestaurantQuery.name
                    output +=        "<input type='submit' value='Rename'></form>"
                    output +="</body></html>"
                    
                    self.wfile.write(output)
                    print output
                    return
                    
            if self.path.endswith("/restaurants"):
                #get all restaurants from DB
                restaurants = session.query(Restaurant).all()
                    
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                #generate page with all restaurants including links to 'edit' and 'delete' pages and a 'make new restaurant page'
                output = ""  
                output +="<html><body>"
                output += "<a href='/restaurants/new'> Make a new Restaurant Here </a></br></br>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    output += "<a href='/restaurants/%s/edit'>Edit</a>" % restaurant.id
                    output += "</br>"
                    output += "<a href='/restaurants/%s/delete'>Delete</a>" % restaurant.id
                    output +="</br>"
                    output +="</br>"
                output +="</body></html>"
                self.wfile.write(output)
                print output
                return
                
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "Hello!"
                output +='''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
                
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output = ""
                output +="<html><body>"
                output +="&#161Hola! <a href = '/hello'> Back to Hello</a>"
                output +='''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output +="</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
            
            
 '''
 TODO: Implement do_POST for /ID/edit and /ID/delete
 '''
 
    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                #Extract name from HTML FORM
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')
                
                #Create new Restaurant class
                newRestaurant = Restaurant(name = messagecontent[0])
                session.add(newRestaurant)
                session.commit()
                
                #respond and redirect to restaurants overview page
                self.send_response(301)
                self.send_header('content', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()
                
                return
        
            # self.send_response(301)
            # self.send_header('Content-type', 'text/html')
            # self.end_headers()
            # ctype, pdict = cgi.parse_header(
            #     self.headers.getheader('content-type'))
            # if ctype == 'multipart/form-data':
            #     fields = cgi.parse_multipart(self.rfile, pdict)
            #     messagecontent = fields.get('message')
            # output = ""
            # output += "<html><body>"
            # output += " <h2> Okay, how about this: </h2>"
            # output += "<h1> %s </h1>" % messagecontent[0]
            # output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            # output += "</body></html>"
            # self.wfile.write(output)
            # print output
        except:
            pass
            
            
 
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()