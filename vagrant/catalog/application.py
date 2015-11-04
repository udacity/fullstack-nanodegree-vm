"""  Start setting up flask framework """
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/meow")
def meow():
    return "Hello Kitty!!"

if __name__ == "__main__":
    app.config.update(
        DEBUG=True,
        SERVER='http://localhost:8000',
        TRAP_BAD_REQUEST_ERRORS=True,
        TRAP_HTTP_EXCEPTIONS=True
    )
    app.run(host='0.0.0.0')
