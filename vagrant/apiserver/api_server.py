#THIS IS A WEBSERVER FOR DEMONSTRATING THE TYPES OF RESPONSES WE SEE FROM AN API ENDPOINT
from flask import Flask
app = Flask(__name__)

#GET REQUEST

@app.route('/readHello')
def getRequestHello():
	return "Hi, I got your GET Request!"

#POST REQUEST
@app.route('/createHello', methods = ['POST'])
def postRequestHello():
	return "I see you sent a POST message :-)"
#UPDATE REQUEST
@app.route('/updateHello', methods = ['PUT'])
def updateRequestHello():
	return "Sending Hello on an PUT request!"

#DELETE REQUEST
@app.route('/deleteHello', methods = ['DELETE'])
def deleteRequestHello():
	return "Deleting your hard drive.....haha just kidding! I received a DELETE request!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	