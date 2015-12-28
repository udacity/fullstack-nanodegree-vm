"""
This code makes the starting population for the easy-acc web app
"""
#importing all dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Currency, Movement, AccountGroup, AccountSubgroup, Account, Flow

#linking db
engine = create_engine('sqlite:///easy-acc.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#Here starts the code to populate the database with some values

# Create a unique User
user1 = User(name = "Avatar", permission="all")
session.add(user1)
session.commit()

# Creating all 7 account groups
for aux in range(1,8):
    acc_name="Grupo de contas " + str(aux) + " - fluxo de XXXX"
    acc_list = AccountGroup(name=acc_name, id=aux)
    session.add(acc_list)
    session.commit()

# Adding currencies EUR and BRL
currency1 = Currency(name="Euro", international_code="EUR")
currency2 = Currency(name="Real", international_code="BRL")
session.add(currency1)
session.add(currency2)
session.commit()




