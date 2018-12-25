from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi

# handler
class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '''
                    <!doctype html>
                    <html lang="en">
                        <title>FSF - Hello</title>
                        <body>
                            <p>Hello, world from Full Stack Foundations!</p>
                            <form method="POST" enctype="multipart/form-data" action="/hello">
                                <p>What would you like me to say?</p>
                                <input name="message" type="text">
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                    </html>'''

                self.wfile.write(output)
                # print(output)
                return

            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '''
                    <html>
                        <title>FSF - Hola</title>
                        <body>
                            <p>&#161 Hola, world from Full Stack Foundations!</p>
                            <a href="/hello">Back to Hello</a>
                            <form method="POST" enctype="multipart/form-data" action="/hello">
                                <p>What would you like me to say?</p>
                                <input name="message" type="text">
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                    </html>'''

                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, 'file not found %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                message_content = fields.get('message')

            output = ''
            output += '''
                <!doctype html>
                <html lang="en">
                    <title>FSF</title>
                    <body>
                        <p>Okay, how about this:</p>
                        <h1>%s</h1>
                        <form method="POST" enctype="multipart/form-data" action="/hello">
                            <p>What would you like me to say?</p>
                            <input name="message" type="text">
                            <input type="submit" value="Submit">
                        </form>
                    </body>
                </html>''' % message_content[0]

            self.wfile.write(output)
            return

        except:
            pass

# main
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print('web server running on port %s' % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C entered, stopping web server')
        server.socket.close()

if __name__ == '__main__':
    main()