from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy
import datetime

engine = create_engine('sqlite:///puppyshelter2.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def diff_month(d1, d2):
    return (d1.year - d2.year)*12 + d1.month - d2.month

#item 1
items = session.query(Puppy).join("shelter").order_by(Puppy.name).all()

for item in items:
    pass
#    print item.name + "   " + item.gender + ".........." + item.shelter.name +"\n"

#item 2
today = datetime.date.today()
limit_date = today - datetime.timedelta(days=3*60)
print limit_date
items = session.query(Puppy).filter(Puppy.dateOfBirth >= limit_date).join("shelter").order_by(desc(Puppy.dateOfBirth)).all()

for item in items:
#    print item.name +  "  age:  "+ str(diff_month(today, item.dateOfBirth)) +"   "+ str(item.dateOfBirth)
    #+ "    Sex: "+ "  " + item.gender + ".........." + item.shelter.name +"\n"
    
 #item 3  
 items = session.query(Puppy).join("shelter").order_by( Puppy.shelter_id, desc(Puppy.dateOfBirth)).all()
 
for item in items:
    print item.name + "   " + item.gender + ".........." + item.shelter.name + "  "+str(item.shelter.current_occupancy(session)) +"\n"