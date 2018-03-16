#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbset import Base, User, Category, Item

engine = create_engine('sqlite:///data.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(name='Abhishek Suri', email='kehsihbairus@gmail.com')
session.add(user1)
session.commit()

category1 = Category(name='Soccer', user=user1)
session.add(category1)
session.commit()
item1 = Item(name='Ball',
             description="A football, soccer ball, or association football ball is the \
              ball used in the sport of association football. \
               The ball's spherical shape, as well as its size, weight, \
                and material composition, are specified by Law 2 of the \
                 Laws of the Game maintained by the International Football Association Board.", category=category1, user=user1)
session.add(item1)
session.commit()

item2 = Item(name='Net',
             description="To score a goal, the ball must pass completely over\
              the goal line between the goal posts and under the crossbar\
               and no rules may be violated on the play (such as touching the\
                ball with the hand or arm). See also offside.\
              The goal structure is defined as a frame 24 feet (7.32 m) wide by 8 feet (2.44 m) tall.", category=category1, user=user1)
session.add(item2)
session.commit()

item3 = Item(name='Jersey',
             description="In association football, kit (also referred to as a strip or uniform)\
              is the standard equipment and attire worn by players. ... Football kit has\
               evolved significantly since the early days of the sport when players typically \
             wore thick cotton shirts, knickerbockers and heavy rigid leather boots.", category=category1, user=user1)
session.add(item3)
session.commit()

category2 = Category(name='BasketBall', user=user1)
session.add(category2)
session.commit()
item21 = Item(name='Ball',
              description="A basketball is a spherical ball used in basketball games.\
               Basketballs typically range in size from very small promotional items only a few\
               inches in diameter to extra large balls nearly a foot in diameter used in training\
                exercises.", category=category2, user=user1)
session.add(item21)
session.commit()

item22 = Item(name='Hoop',
              description="To score a goal, the ball must pass completely over\
               the goal line between the goal posts and under the crossbar\
                and no rules may be violated on the play (such as touching the\
                 ball with the hand or arm). See also offside.\
               The goal structure is defined as a frame 24 feet (7.32 m) wide by 8 feet (2.44 m) tall."
, category=category2, user=user1)
session.add(item22)
session.commit()

category3 = Category(name='Cricket', user=user1)
session.add(category3)
session.commit()
item31 = Item(name='Bat',
              description="A cricket bat is a specialised piece of equipment used by\
               batsmen in the sport of cricket to hit the ball, typically consisting\
                of a cane handle attached to a flat-fronted willow-wood blade.", category=category3, user=user1)
session.add(item31)
session.commit()

item32 = Item(name='Helmet',
              description="In the sport of cricket, batsmen often wear a helmet to protect\
               themselves from injury or concussion by the cricket ball, which is very hard\
                and can be bowled to them at speeds over 90 miles per hour (140 km/h).", category=category3, user=user1)
session.add(item32)
session.commit()
