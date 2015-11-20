from app import app


@app.route('/')
@app.route('/equipment')
def catalog():
    return "Hi - this is where the equipment catalog lives"


@app.route('/equipment/item/<int:id>/')
def getItem(id=1):
    return "This is where an item lives %s", id
