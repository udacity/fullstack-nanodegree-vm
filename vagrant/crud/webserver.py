from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class webserverHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self._set_headers()
                output = '<html><body>Hello!'
                output += '<form method="POST" enctype="multipart/form-data" '
                output += 'action="/hello">'
                output += '<h2>What would you like me to say?</h2>'
                output += '<input name="message" type="text">'
                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
            if self.path.endswith('/hola'):
                self._set_headers()
                output = '<html><body>&#161Hola!'
                output += '<a href="/hello">Back to Hello</a>'
                output += '<form method="POST" enctype="multipart/form-data" '
                output += 'action="/hello">'
                output += '<h2>What would you like me to say?</h2>'
                output += '<input name="message" type="text">'
                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'
                print(output)
                response = bytes(output, 'UTF-8')
                self.wfile.write(response)
        except IOError:
            self.send_error(404, 'File Not Found {}'.format(self.path))

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            print(form.getvalue("message"))
            output = ''
            output += '<html><body>'
            output += '<h2>Okay,</h2>'
            output += '<h1>{}</h1>'.format(form.getvalue("message"))
            output += '<form method="POST" enctype="multipart/form-data" '
            output += 'action="/hello">'
            output += '<h2>What would you like me to say?</h2>'
            output += '<input name="message" type="text">'
            output += '<input type="submit" value="Submit">'
            output += '</form>'
            output += '</body></html>'
            print(output)
            response = bytes(output, 'UTF-8')
            self.wfile.write(response)
        except Exception as exc:
            print(exc)

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