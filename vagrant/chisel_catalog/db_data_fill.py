from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup_chisel_db import Parks, Trails

engine = create_engine('sqlite:///chisel.db')
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


# Create dummy Park
Park1 = Parks(name="Zion", lat="37.3222826", lon="-113.1833195",  
             description='Beautiful')
session.add(Park1)
session.commit()

# Menu for UrbanBurger
Trail1 = Trails(name="Butterfly", park_id="1", lat="37.210319", lon="-112.956579", description="A really cool trail")

session.add(Trial1)
session.commit()


print "added trails and parks!"