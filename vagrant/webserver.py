from http.server import HTTPServer, BaseHTTPRequestHandler


class webserverHandler(BaseHTTPRequestHandler):  # webserverHandler inheriting from BaseHTTPRequestHandler
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!<body><html>"
            self.wfile.write(message.encode())
            print(message)
            return

        if self.path == '/hola':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body> &#161Hola! <a href='/hello'>Back to Hello</a><body><html>"
            self.wfile.write(message.encode())
            print(message)
            return

        else:
            self.send_error(404, 'File {} not found'.format(self.path[1:]))


def main():
    try:
        port = 9000
        serverAddress = ('', port)
        server = HTTPServer(serverAddress, webserverHandler)  # Handler class webserverHandler
        print("Web server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server ...")
        server.socket.close()


if __name__ == '__main__':
    main()
