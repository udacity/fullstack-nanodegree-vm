from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://quantel@localhost/jira_customers_test?charset=utf8', pool_recycle=3600)
Base = declarative_base(engine)
########################################################################
class Customer(Base):
    """"""
    __tablename__ = 'customer'
    __table_args__ = {'autoload':True}

class Customer_codes(Base):
    """"""
    __tablename__ = 'customer_coes'
    __table_args__ = {'autoload':True}

class Serial(Base):
    """"""
    __tablename__ = 'serial'
    __table_args__ = {'autoload':True}

#----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == "__main__":
    session = loadSession()
    res = session.query(Customer).all()
    print res[1].title
