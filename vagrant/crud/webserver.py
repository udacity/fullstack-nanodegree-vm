from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = '<html><body>Hello!</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = '<html><body>&#161Hola!<a href="/hello">Back to Hello</a></body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
        except IOError:
            self.send_error(404, 'File Not Found {}'.format(self.path))

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                message_content = fields.get('message')
        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print('WebServer: Server running on port {}'.format(port))
        server.serve_forever()
    except KeyboardInterrupt:
        print('WebServer: ^C entered, stopping web server')
        pass

if __name__ == '__main__':
    main()