from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
base.metadata.bind = create_engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
firstResult = session.query(Restaurant).first()
firstResult.name
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
for veggieBurger in veggieBurgers:
    if veggieBurger.price !='$2.99':
        veggieBurger.price = '$2.99'
            session.add(veggieBurger)
            session.commit()

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit()
