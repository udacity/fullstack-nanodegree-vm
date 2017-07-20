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
				session = DBSession()
				restaurants = session.query(Restaurant).all()
				for r in restaurants:
					output += r.name
				output += "</body></html>"
				

				self.wfile.write(output)
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