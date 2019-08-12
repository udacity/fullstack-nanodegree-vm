import http.server
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import re
import sys

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.bind = engine


class WebServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/restaurants'):
                try:
                    global session
                    restaurants = session.query(Restaurant).all()
                    restauraunt_names = [
                        '<div>{0}</div><a href="/restaurants/{1}/edit">Edit</a><br><a href="/restaurants/{1}/delete">Delete</a><br><br>'.format(restaurant.name, restaurant.id)
                        for restaurant in restaurants]

                except:
                    print(sys.exc_info()[0])
                    raise ValueError('Something went wrong retrieving the restauraunts.')

                res = '''
                    <html>
                        <body>
                            <h1>Restauraunts For You!</h1>
                            <div><a href="/restaurants/new">Create a new restaurant</a></div><br><br>
                            {}
                        </body>
                    </html>
                    '''.format(''.join(restauraunt_names) if restauraunt_names else '<div>None available<div>')

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(res.encode('utf-8'))
                return

            elif self.path.endswith('/restaurants/new'):
                res = '''
                    <html>
                        <body>
                            <form method="POST" enctype="multipart/form-data" action="new">
                                <h2>Add a Restaurant</h2>
                                <input name="newRestaurantName" type="text" placeholder="New Restaurant Name">
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                    </html>
                    '''

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(res.encode('utf-8'))
                return

            elif re.fullmatch('/restaurants/[0-9]+/edit/?', self.path):
                restaurant_id = self.path.split('/')[2]
                try:
                    selected_restaurant = session.query(Restaurant).filter_by(id=int(restaurant_id)).one()
                except:
                    self.send_error(404, 'Resource not found: restaurant.id = {}'.format(restaurant_id))
                    return

                res = '''
                    <html>
                        <body>
                            <h2>Edit Restaurant Name</h2>
                            <form method="POST" enctype="multipart/form-data" action="/restaurants/{}/edit">
                                <h3>Update name for {}</h3>
                                <input type="text" name="newRestaurantName" placeholder="New Restaurant Name">
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                    </html>
                    '''.format(restaurant_id, selected_restaurant.name)

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(res.encode('utf-8'))
                return

            elif re.fullmatch('/restaurants/[0-9]+/delete/?', self.path):
                restaurant_id = self.path.split('/')[2]
                try:
                    selected_restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
                except:
                    self.send_error(404, 'Resource not found: restaurant.id = {}'.format(restuarant_id))

                res = '''
                    <html>
                        <body>
                            <form method="POST" enctype="multipart/form-data" action="/restaurants/{}/delete">
                                <h3>Are you sure you want to delete {}?</h3>
                                <input type="submit" value="Delete it!">
                            </form>
                        </body>
                    </html>
                    '''.format(restaurant_id, selected_restaurant.name)

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(res.encode('utf-8'))
                return

            else:
                self.send_error(404, 'File Not Found: {}'.format(self.path))
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[0].value)
            self.send_error(500, 'Internal server error.')

    def do_POST(self):
        try:
            if self.path.endswith('/restaurants/new'):
                content_type, property_dict = cgi.parse_header(self.headers.get('Content-type'))
                property_dict['boundary'] = bytes(property_dict['boundary'], 'utf-8')
                content_len = int(self.headers.get('Content-length'))
                property_dict['CONTENT-LENGTH'] = content_len

                new_restaurant_name = None
                if content_type == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, property_dict)
                    new_restaurant_name = fields.get('newRestaurantName')[0]

                if not new_restaurant_name:
                    raise ValueError('No restaurant name provided')

                try:
                    new_restaurant = Restaurant(name=new_restaurant_name)
                    session.add(new_restaurant)
                    session.commit()
                except:
                    raise Exception('Unable to add to DB')

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            elif re.fullmatch('/restaurants/[0-9]+/edit', self.path):
                restaurant_id = self.path.split('/')[2]

                content_type, property_dict = cgi.parse_header(self.headers.get('Content-type'))
                property_dict['boundary'] = bytes(property_dict['boundary'], 'utf-8')
                content_len = int(self.headers.get('Content-length'))
                property_dict['CONTENT-LENGTH'] = content_len

                new_restaurant_name = None
                if content_type == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, property_dict)
                    new_restaurant_name = fields.get('newRestaurantName')[0]

                if not new_restaurant_name:
                    raise ValueError('No restaurant name provided')

                try:
                    selected_restaurant = session.query(Restaurant).filter_by(id=int(restaurant_id)).one()
                    selected_restaurant.name = new_restaurant_name.decode('utf-8')
                    session.add(selected_restaurant)
                    session.commit()

                except:
                    self.send_error(404, 'Resource not found: restaurant.id = {}'.format(restaurant_id))
                    return

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            elif re.fullmatch('/restaurants/[0-9]+/delete', self.path):
                restaurant_id = self.path.split('/')[2]

                try:
                    selected_restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
                    session.delete(selected_restaurant)
                    session.commit()
                except:
                    self.send_error(404, 'Resource not found: restaurant.id = {}'.format(restaurant_id))
                    return

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()
                return

        except:
            self.send_error(400, 'Bad request')


def main():
    try:
        server = http.server.HTTPServer(('', 8080), WebServerHandler)
        print('Web server running on port 8080...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Stopping web server')
        server.socket.close()

if __name__ == '__main__':
    main()