from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

# connect to the database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # list of restaurants
            if self.path.endswith("/restaurant"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Restaurant List</h1>"
                output += "<hr>"
                output += '''<form method="POST" enctype="multipart/form-data" action="/restaurant"><p>Add a new restaurant</p>
                <input name="newRestaurantName" type="text" placeholder="New Restaurant Name"><input type="submit" value="Submit"></form>'''
                # output += "<a href='/restaurant/new'>Make a New Restaurant Here</a></br></br>"
                output += "<hr>"
                for restaurant in restaurants:
                    output += "<div>"
                    output += "%s <br>" %restaurant.name
                    output += "<a href='/restaurant/%s/edit'>Edit</a>" %restaurant.id
                    # output += '''<form method="POST" action="/restaurant">
                    # <button name="delete" value="Delete">delete</button></form><br>'''
                    output += "<br><a href='/restaurant/%s/delete'>Delete</a>" %restaurant.id
                    output += "</div>"
                    output += "<br>"
                output += "</body></html>"
                self.wfile.write(output.encode("utf-8"))
                return
            
            # edit page
            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split('/')[2]
                targetRestaurant = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if targetRestaurant != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>Rename %s</h1>" %targetRestaurant.name
                    output += '''<form method="POST" enctype="multipart/form-data" action="/restaurant/%s/edit">
                    <input name="Rename" type="text" placeholder=%s><input type="submit" value="Rename">
                    </form>''' %(restaurantIDPath, targetRestaurant.name)
                    output += "</body></html>"
                    self.wfile.write(output.encode("utf-8"))
                    return

            # delete page
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split('/')[2]
                targetRestaurant = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if targetRestaurant != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?</h1>" %targetRestaurant.name
                    output += '''<form method="POST" action="/restaurant/%s/delete">
                    <button name="Delete" value="Delete">delete</button></form>''' %restaurantIDPath
                    output += "</body></html>"
                    self.wfile.write(output.encode("utf-8"))
                    return


        except IOError:
            self.send_error(404, "File Not Found %s" %self.path)


    def do_POST(self):
        try:
            # create
            if self.path.endswith('/restaurant'):
                ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                pdict['CONTENT-LENGTH'] = int(self.headers.get('Content-length'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    # add a new restaurant to the database
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()
                restaurants = session.query(Restaurant).all()
                
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output = ""
                output += "<html><body>"
                output += "<h1>Restaurant List</h1>"
                output += "<hr>"
                output += '''<form method="POST" enctype="multipart/form-data" action="/restaurant"><p>Add a new restaurant</p>
                <input name="newRestaurantName" type="text" placeholder="New Restaurant Name"><input type="submit" value="Submit"></form>'''
                output += "<hr>"
                for restaurant in restaurants:
                    output += "<div>"
                    output += "%s <br>" %restaurant.name
                    output += "<a href='/restaurant/%s/edit'>Edit</a>" %restaurant.id
                    output += "<br><a href='/restaurant/%s/delete'>Delete</a>" %restaurant.id
                    output += "</div>"
                    output += "<br>"
                output += "</body></html>"
                self.wfile.write(output.encode("utf-8"))
            
            # update
            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                pdict['CONTENT-LENGTH'] = int(self.headers.get('Content-length'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('Rename')

                restaurantIDPath = self.path.split('/')[2]
                targetRestaurant = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if targetRestaurant != []:
                    targetRestaurant.name = messagecontent[0]
                    session.add(targetRestaurant)
                    session.commit()
            
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()

                return

            # delete
            if self.path.endswith('/delete'):
                restaurantIDPath = self.path.split('/')[2]
                targetRestaurant = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if targetRestaurant != []:
                    session.delete(targetRestaurant)
                    session.commit()
                
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurant')
                    self.end_headers()

                return


        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print("Web server running on port %s" %port)
        server.serve_forever()
    
    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    main()