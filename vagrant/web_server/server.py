#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from http.server import BaseHTTPRequestHandler, HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = '''
                    <html>
                        <body>
                            <h1>Hello!</h1>
                            <form method='POST' enctype='multipart/form-data' action='/hello'>
                                <h2>What would you like me to say?</h2>
                                <input name="message" type="text" >
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                    </html>
                '''

                self.wfile.write(output)
                print(output)
                return

            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = '''
                    <html>
                        <body>
                            <h1>Hello!</h1>
                            <form method='POST' enctype='multipart/form-data' action='/hello'>
                                <h2>What would you like me to say?</h2>
                                <input name="message" type="text" >
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                    </html>
                '''

                self.wfile.write(output)
                print(output)
                return

        except IOError:
            self.sen_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type')
            )

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                message_content = fields.get('message')

            output = '''
                <html>
                    <body>
                        <h2>OK, How about this?</h2>
            '''
            output += '<h1>%s</h1>' % message_content[0]
            output += '''
                    <form method='POST' enctype='multipart/form-data' action='/hello'>
                        <input name="message" type="text" >
                        <input type="submit" value="Submit">
                    </form>
                </body>
            </html>
            '''

            self.wfile.write(output)
            print(output)

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print('server running on port: %s' % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C entered, server stopping...')
        server.socket.close()

if __name__ == '__main__':
    main()
