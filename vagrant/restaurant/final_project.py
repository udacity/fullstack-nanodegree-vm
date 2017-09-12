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

# Making an API endpoint for Restaurant Menu(GET Request)
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

# Making and API endpoint for a single MenuItem(GET Request)
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id,menu_id):
	menuItem = session.query(MenuItem).filter_by(id=menu_id,restaurant_id=restaurant_id).one()
	return jsonify(MenuItem=menuItem.serialize)

# Task 1: Create route for Restaurant function here
@app.route('/')
@app.route('/restaurant/')
def restaurantList():
	restaurants = session.query(Restaurant).all()
	#Below code show how to use HTML Template to achieve the same dynamically
	return render_template('restaurant.html',restaurants=restaurants)


# Task 1: Create route for newRestaurant function here
@app.route('/restaurant/new/',methods=['GET','POST'])	
def newRestaurant():
	if request.method == 'POST':
		newRestaurant = Restaurant(name=request.form['restaurantname'])
		session.add(newRestaurant)
		session.commit()
		flash('New Restaurant created')
		return	redirect(url_for('restaurantList'))
	else:
		return render_template('newrestaurant.html')
	

# Task 2: Create route for editRestaurant function here
@app.route('/restaurant/<int:restaurant_id>/edit/',methods=['GET','POST'])		
def editRestaurant(restaurant_id):
	editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		if editedRestaurant !=[]:
			editedRestaurant.name=request.form['restaurantname']
			session.add(editedRestaurant)
			session.commit()
			flash('Restaurant "'+editedRestaurant.name+'" updated successfully')
		return	redirect(url_for('restaurantList',restaurant_id=restaurant_id))

	else:
		return render_template('editrestaurant.html',restaurant_id=restaurant_id,editedRestaurant=editedRestaurant)

# Task 3: Create route for deleteRestaurant function here
@app.route('/restaurant/<int:restaurant_id>/delete/',methods=['GET','POST'])		
def deleteRestaurant(restaurant_id):	
	deletedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':		
		if deletedRestaurant !=[]:
			session.delete(deletedRestaurant)
			session.commit()
			flash('Restaurant "'+deletedRestaurant.name+'" deleted successfully')
		return	redirect(url_for('restaurantList',restaurant_id=restaurant_id))

	else:
		return render_template('deleterestaurant.html',restaurant_id=restaurant_id,deletedRestaurant=deletedRestaurant)

# Task 5: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menuItems = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
	#Below code show how to use HTML Template to achieve the same dynamically
	return render_template('menu.html',restaurant=restaurant,menuItems=menuItems)
	

# Task 6: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/new/',methods=['GET','POST'])	
def newMenuItem(restaurant_id):
	if request.method == 'POST':
		newMenu = MenuItem(name=request.form['newmenu'],price=request.form['price'],description=request.form['description'],restaurant_id=restaurant_id)
		session.add(newMenu)
		session.commit()
		flash('New menu item created')
		return	redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
	else:
		return render_template('newmenuitem.html',restaurant_id=restaurant_id)
	

# Task 7: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/',methods=['GET','POST'])		
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

# Task 8: Create route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/',methods=['GET','POST'])		
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


if __name__ == '__main__':
	app.secret_key = 'Super-Secret-Key'
	app.debug=True
	app.run(host='0.0.0.0',port=8000)
