from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

FORM = "<form method='POST' enctype='multipart/form-data' action='/hello'>" + \
    "<h2>What would you like to say?</h2><input name='message' type='text'>" + \
    "<input type='submit' Value='Submit'></form>"

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!</body></html>"
                output += FORM
                self.wfile.write(output)
                print(output)
                return
            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>&#161Hola!<a href='/hello'>Back to Hello</a></body></html>"
                output += FORM
                self.wfile.write(output)
                print(output)
                return

        except:
            self.send_header(404, 'File Not Found {}'.format(self.path))


    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messageContent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this:</h2>"
            output += "<h1> {} </h1>".format(messageContent[0])
            output += FORM
            output += "</body></html>"
            self.wfile.write(output)
            print(output)
            return

        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print('Web server running on port {}'.format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C entered, stopping web server...')
        server.socket.close()

if __name__ == '__main__':
    main()