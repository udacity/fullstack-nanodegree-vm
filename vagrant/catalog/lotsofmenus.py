from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Sport, Base, SportItem, User

engine = create_engine('sqlite:///sports.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Items for Baseball
sport1 = Sport(user_id=1, name="Baseball")

session.add(sport1)
session.commit()

sportItem2 = SportItem(user_id=1, name="Baseball", description="Cow Hide covered ball with wool laces.", sport=sport1)

session.add(sportItem2)
session.commit()


sportItem1 = SportItem(user_id=1, name="Baseball Bat", description="Metal or wood.", sport=sport1)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(user_id=1, name="Batting Glove", description="Used by hitters to keep their hands from getting blisters.", sport=sport1)

session.add(sportItem2)
session.commit()

sportItem3 = SportItem(user_id=1, name="Glove", description="Padded glove used to catch ball on defense.", sport=sport1)

session.add(sportItem3)
session.commit()

sportItem4 = SportItem(user_id=1, name="Cleats", description="Shoes with metal spikes for better traction.", sport=sport1)

session.add(sportItem4)
session.commit()

# Items for Football
sport2 = Sport(user_id=1, name="Football")

session.add(sport2)
session.commit()

sportItem1 = SportItem(user_id=1, name="Football", description="Oval shaped ball, made of pigskin.", sport=sport2)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(user_id=1, name="Pads", description="Used to protect from injuries by tackle.", sport=sport2)

session.add(sportItem2)
session.commit()

print "added items!"
