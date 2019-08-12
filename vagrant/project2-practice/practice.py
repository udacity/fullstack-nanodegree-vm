from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Boilerplate.
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

# query = session.query(Restaurant)
# print('Restaurants in the DB ({}):'.format(query.count()))
# for restaurant in query.all():
#     print('{} - {}'.format(restaurant.id, restaurant.name))

# print(query.column_descriptions)

# print('\n\n\n')

# query = session.query(MenuItem).filter_by(name='Veggie Burger')
# print('All veggie burgers ({}):'.format(query.count()))
# for burger in query.all():
#     print('{}: {} from {}'.format(burger.id, burger.price, burger.restaurant.name))

# urban_veggie_burger1 = session.query(MenuItem).filter_by(id=1).one()
# print(urban_veggie_burger1.price)
# urban_veggie_burger1.price = '$2.50'
# session.add(urban_veggie_burger1)

# session.commit()

# urban_veggie_burger1 = session.query(MenuItem).filter_by(id=1).one()
# print(urban_veggie_burger1.price)


