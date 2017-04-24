from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=''):
    return 'Hello there, %s' % name
