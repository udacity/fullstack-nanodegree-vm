from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    # @TODO - remove debug mode
    app.run(host='0.0.0.0', port=8000, debug=True)

