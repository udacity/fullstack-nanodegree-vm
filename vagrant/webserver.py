from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi  # common gateway interface

# indicate what code to execute based on the type of HTTP request that is sent to the server
class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)  # indicate a successful GET request
                self.send_header('Content-type', 'text/html')  # indicate replying with text in the form of HTML to the client
                self.end_headers()  # send a blank line, indicating the end of our HTTP headers in the responses

                # create response
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>
                <input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode("utf-8"))  # send a message back to the client
                print(output)  # for checking in the terminal
                return  # exit from if statement, comming in handy for debugging

            # Spanish
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                # output += "<a href='/hello' >Back to Hello</a>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>
                <input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode("utf-8"))
                print(output)
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)  # notify me 404 or file not found error


    # override the method in BaseHTTPRequestHandler 
    def do_POST(self):
        try:
            self.send_response(301)  # send the response indicating successful post
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # print("headers:\n", self.headers)

            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))  # parse an HTML form from headers
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            pdict['CONTENT-LENGTH'] = int(self.headers.get('Content-length'))
            if ctype == 'multipart/form-data':  # if this is form-data being received
                fields = cgi.parse_multipart(self.rfile, pdict)  # collect all of the fields in a form
                messagecontent = fields.get('message')  # get out the value of a specific field or set of fields and store them in an array

            # what to tell the client with the new information I've received
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>
            <input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output.encode("utf-8"))
            print(output)

        except:
            pass


# instantiate a server and specify what port it will listen on
def main():
    try:
        port = 8080
        # build a server instance based on webServerHandler
        server = HTTPServer(('', port), webServerHandler)  # (server_address=(host, port), RequestHandlerClass)
        print("Web server running on port %s" % port)
        server.serve_forever()  # to keep constantly listening until I call Ctrl+C or exit the application


    except KeyboardInterrupt:  # triggered when the users holds Ctrl+C on the keyboard
        print("^C entered, stopping web server...")
        server.socket.close()  # shutdown


if __name__ == '__main__':
        main()



