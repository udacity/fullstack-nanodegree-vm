from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import func
import pprint

from database_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def get_all_puppies_name_asc():
    # Select all puppies name and order them by asc
    allPuppy = session.query(Puppy.name).order_by(Puppy.name.asc()).all()

    for p in allPuppy:
        print "{name}".format(name=p[0])


def get_youngest_puppies():
    # Select all puppies name and date of birth (dob), where puppies not older then 6 months and order them by desc
    today = datetime.date.today()
    deltaSixMonths = today - datetime.timedelta(days=182)

    allYoungestPuppy = session.query(Puppy.name, Puppy.dateOfBirth).filter(
        Puppy.dateOfBirth >= deltaSixMonths).order_by(Puppy.weight.desc()).all()

    for p in allYoungestPuppy:
        print "{name}: {dob}".format(name=p[0], dob=p[1])


def get_puppies_weight_asc():
    # Select all puppies name and their weight, order them by asc
    allPuppiesWeightAsc = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()

    for p in allPuppiesWeightAsc:
        print "{name}: {weight}".format(name=p[0], weight=p[1])


def get_puppies_shelter():
    # Select all shelters and their puppies
    allPuppiesShelter = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()

    for p in allPuppiesShelter:
        print "{shelterName}: {puppyCount}".format(shelterName=p[0].name, puppyCount=p[1])


get_all_puppies_name_asc()
get_youngest_puppies()
get_puppies_weight_asc()
get_puppies_shelter()
