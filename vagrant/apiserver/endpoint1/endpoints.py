from flask import Flask
app = Flask(__name__) 
# Create the appropriate app.route functions. Test and see if they work

#Make an app.route() decorator here for when the client sends the URI "/puppies"
@app.route('/puppies')
def puppiesFunction():
  return "Yes, puppies!"
  
 
#Make another app.route() decorator here that takes in an integer named 'id' for when the client visits a URI like "/puppies/5"
@app.route('/puppies/<int:id>')
def puppiesFunctionId(id):
  return "This method will act on the puppy with id %s" % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)