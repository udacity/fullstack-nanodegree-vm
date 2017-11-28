from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

#Create a DB connection and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
       
        if self.path.endswith("/restaurant"):
            #print self.path
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"                        
            output += "<h2><a href='http://localhost:8080/restaurant/new'>Make a New Restaurant Here</a></h2>"         
            RestaurantData = session.query(Restaurant).all()
            #print "Hello"
            for rest in RestaurantData:
                output += "<h2>"+rest.name
                output += "<br><a href='http://localhost:8080/restaurant/"+str(rest.id)+"/edit'>Edit</a><br>\
                <a href='http://localhost:8080/restaurant/"+str(rest.id)+"/delete'>Delete</a></h2>"
            output += "<h2><a href='http://localhost:8080/restaurant/new'>Make a New Restaurant Here</a></h2>"         
            output += "</body></html>"               
            self.wfile.write(output)
            #print output
            return                        
        elif self.path.endswith("/restaurant/new"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"                        
            output += "<h2>Make a New Restaurant Here</h2>"             
            output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/new'>\
                    <input type='text' name='newrestaurant'></input><input type='submit' value='Create'></input></form>"                                            
            output += "</body></html>"
            self.wfile.write(output)
            #print output
            return                                    
        elif self.path.endswith("/edit"):
            #restaurant_id= self.path[self.path.find('/',2)+1:self.path.find('/edit')]
            restaurant_id= self.path.split('/')[2]
            restaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"                        
            output += "<h2>"+restaurant.name+"</h2>"             
            output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/"+restaurant_id+"/edit'>\
                    <input type='text' name='editrestaurant' placeholder='"+restaurant.name+"'></input><input type='submit' value='Rename'></input></form>"                                            
            output += "</body></html>"
            self.wfile.write(output)
            #print output
            return                                    
        elif self.path.endswith("/delete"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            restaurant_id= self.path.split('/')[2]
            restaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()            
            output = ""
            output += "<html><body>"                        
            output += "<h2>Are you sure you want to delete "+restaurant.name+"?</h2>"             
            output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/delete'>\
                    </input><input type='submit' value='Delete'></input></form>" % restaurant_id                              
            output += "</body></html>"
            self.wfile.write(output)
            #print output
            return                                    
        elif self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += "Hello!"
            message += "<form method='POST' enctype='multipart/form-data' action='/hello'>\
                    <h2>What would you like me to say? </h2><input type='text' name='message'></input>\
                    <input type='submit' value='Submit'></input>\
                    </form>"            
            message += "</body></html>"            

            self.wfile.write(message)
            print message
            return
        elif self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += "!Hola! <a href='http://localhost:8080/hello'>Back 2 Hello page</a>" 
            message += "</body></html>"            
            self.wfile.write(message)
            print message
            return        
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        #print "Post In"
        try:
            if self.path.endswith("/new"):            
                ctype,pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile,pdict)
                    textcontent= fields.get('newrestaurant')

                newRestaurantData = Restaurant(name=textcontent[0])
                session.add(newRestaurantData)
                session.commit()                    

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()

                # output = ""
                # output += "<html><body>"                            
                # output += "<h2><a href='http://localhost:8080/restaurant/new'>Make a New Restaurant Here</a></h2>"         
                # RestaurantData = session.query(Restaurant).all()
                # for rest in RestaurantData:
                #     output += "<h2>"+rest.name
                #     output += "<br><a href='#'>Edit</a><br><a href='#'>Delete</a></h2>"
                #     print "Post In 3"
                # output += "<h2><a href='http://localhost:8080/restaurant/new'>Make a New Restaurant Here</a></h2>"         
                # output += "</body></html>"   
                # print "Post In 4"
                # self.wfile.write(output)
                # print output
            elif self.path.endswith("/edit"):            
                #restaurant_id= self.path[self.path.find('/',2)+1:self.path.find('/edit')]
                restaurant_id= self.path.split('/')[2]
                ctype,pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile,pdict)
                    textcontent= fields.get('editrestaurant')

                updatedRestaurantRow = session.query(Restaurant).filter_by(id=restaurant_id).one()
                if updatedRestaurantRow !=[]:
                    updatedRestaurantRow.name = textcontent[0]
                    session.add(updatedRestaurantRow)
                    session.commit()                    
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurant')
                    self.end_headers()
                return    
            elif self.path.endswith("/delete"):            
                #restaurant_id= self.path[self.path.find('/',2)+1:self.path.find('/delete')]
                restaurant_id= self.path.split('/')[2]
                deleteRestaurantRow = session.query(Restaurant).filter_by(id=restaurant_id).one()
                if deleteRestaurantRow !=[]:
                    session.delete(deleteRestaurantRow)
                    session.commit()                    
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurant')
                    self.end_headers()

                return
            else:
                self.send_response(301)
                self.end_headers()
                ctype,pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile,pdict)
                    messagecontent= fields.get('message')
                output = ""
                output += "<html><body>"
                output += "<h2>Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]
                
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>\
                            <h2>What would you like me to say? </h2><input type='text' name='message'></input>\
                            <input type='submit' value='Submit'></input>\
                            </form>"

                output += "</body></html>"
                self.wfile.write(output)
                print output
                
        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
