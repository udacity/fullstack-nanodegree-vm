#server essentials
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

#database essentials
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)



class RestaurantServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "<table>"
				session = DBSession()
				restaurants = session.query(Restaurant).all()
				for r in restaurants:
					output += "<tr>"
					output += "<td>"
					output += r.name
					output += "</td>"
					output += "<td> <a href='%s/edit'>Edit</a></td>" % r.id
					output += "<td> <a href='%s/delete'>Delete</a></td>"
					output += "</tr>"

				output += "</table>"
				output += "<br /><br /><a href='/createNewRestaurant'>Create new restaurant</a>"
				output += "</body></html>"
				self.wfile.write(output)
				return

			if self.path.endswith('/createNewRestaurant'):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "Create a new Restaurant"
				output += '''<form method='POST' enctype='multipart/form-data' action='/create'><h2>Enter the name of the new restaurant:</h2><input name="res_name" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				return

			if self.path.endswith('/edit'):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				recv_id = self.path.split('/')[1]
				print recv_id
				session = DBSession()
				updateRestaurant = session.query(Restaurant).filter_by(id = recv_id).one()
				print updateRestaurant.name
				
				output = ""
				output += "<html><body>"
				output += "Create a new Restaurant"
				output += '''<form method='POST' enctype='multipart/form-data' action='/%s/update'><h2>Update the name of the restaurant:</h2><input name="res_name" type="text" value="%s" ><input type="submit" value="Submit"> </form>''' % (updateRestaurant.id, updateRestaurant.name)
				output += "</body></html>"
				self.wfile.write(output)
				return


		except:
			self.send_error(404, 'File Not Found %s' %self.path)

	def do_POST(self):
		try:
			if self.path.endswith('/create'):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('res_name')
				session = DBSession()
				newRestaurant = Restaurant(name = "%s" % messagecontent[0])
				session.add(newRestaurant)
				session.commit()
				print "Restaurant added!"
				self.send_response(301)
				self.send_header('Location', '/restaurants')
				self.end_headers()
				return

			if self.path.endswith('/update'):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('res_name')
				recv_id = self.path.split('/')[1]
				session = DBSession()
				newName = session.query(Restaurant).filter_by(id = recv_id).one()
				newName.name = messagecontent[0]
				session.add(newName)
				session.commit()
				print "Restaurant updated!"
				self.send_response(301)
				self.send_header('Location', '/restaurants')
				self.end_headers()
				return

		except:
			pass
				



def main():
	try:
		port = 8080
		server = HTTPServer(('', port), RestaurantServerHandler)
		print "Restaurant server is running on port %s" %port
		server.serve_forever();
	except KeyboardInterrupt:
		print "^C pressed. Closing server..."
		server.socket.close()

if __name__ == '__main__':
	main()