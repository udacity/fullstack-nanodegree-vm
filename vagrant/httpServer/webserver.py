from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		
		if self.path.endswith("/hello"):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			output = ""
			output += "<html></body>Hello!</body></html>"
			self.wfile.write(output)
			print output
			return

		if self.path.endswith("/hola"):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			output = ""
			output += "<html></body>Hello in spanish!<br/><a href='/hello'>Back to hello</a></body></html>"
			self.wfile.write(output)
			print output
			return

		else:	
			self.send_error(404, 'File Not Found: %s' % self.path)

def main():
	try:
		port = 8080
		server = HTTPServer(('', port), WebServerHandler)
		print "Web server running on port %s" % port
		server.serve_forever()
	except KeyboardInterrupt:
		print "^C entered. Stopping web server..."
		server.socket.close()

if __name__ == '__main__':
	main()