from flask import Flask,render_template,url_for,request,redirect,flash,jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

app = Flask(__name__)

#Create a DB connection and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Making and API endpoint (GET Request)
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menuItems = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
	listMenuItems=[]
	j=0
	for i in menuItems:
		if i.serialize !=[]:
			listMenuItems.append(i.serialize)
		j=j+1
	return jsonify(MenuItems=listMenuItems)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id,menu_id):
	menuItem = session.query(MenuItem).filter_by(id=menu_id,restaurant_id=restaurant_id).one()
	return jsonify(MenuItem=menuItem.serialize)

@app.route('/')
@app.route('/restaurant/')
@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menuItems = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
	#Old way to create HTML inside python file
	# output=''
	# for item in menuItems:
	# 	output += item.name +'</br>'+item.price+'</br>'+item.description
	# 	output += '</br>'*2
	#return output

	#Below code show how to use HTML Template to achieve the same dynamically
	return render_template('menu.html',restaurant=restaurant,menuItems=menuItems)

	#insted of getting URL inside render_template, we can pass here as well, it is equivalent to above line
	#return render_template('menu.html',restaurant=restaurant,menuItems=menuItems,restaurantURL=url_for('restaurantMenu'))
	

# Task 1: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/new/',methods=['GET','POST'])	
def newMenuItem(restaurant_id):
	print 'hello'
	if request.method == 'POST':
		newMenu = MenuItem(name=request.form['newmenu'],price=request.form['price'],description=request.form['description'],restaurant_id=restaurant_id)
		session.add(newMenu)
		session.commit()
		flash('New menu item created')
		return	redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
	else:
		print 'hello new'
		return render_template('newmenuitem.html',restaurant_id=restaurant_id)
	

# Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/',methods=['GET','POST'])		
def editMenuItem(restaurant_id,menu_id):
	editedMenu = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		if editedMenu !=[]:
			editedMenu.name=request.form['editmenu']
			session.add(editedMenu)
			session.commit()
			flash('MenuItem "'+editedMenu.name+'" updated successfully')
		return	redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))

	else:
		return render_template('editmenuitem.html',restaurant_id=restaurant_id,menu_id=menu_id,placeHolderMenu=editedMenu)

# Task 3: Create route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/',methods=['GET','POST'])		
def deleteMenuItem(restaurant_id,menu_id):	
	deletedMenu = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':		
		if deletedMenu !=[]:
			session.delete(deletedMenu)
			session.commit()
			flash('Menu "'+deletedMenu.name+'" deleted successfully')
		return	redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))

	else:
		return render_template('deletemenuitem.html',restaurant_id=restaurant_id,menu_id=menu_id,deleteItemMenu=deletedMenu)
# with app.test_request_context():
# 	print url_for('newMenuItem',new='new')
# 	print url_for('editMenuItem',edit='edit')
# 	print url_for('deleteMenuItem',delete='delete')


if __name__ == '__main__':
	app.secret_key = 'Super-Secret-Key'
	app.debug=True
	app.run(host='0.0.0.0',port=5000)
