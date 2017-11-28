from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

#You will use this secret key to create and verify your tokens
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    
    #Add a method to generate auth tokens here
    def generate_auth_token(self,expiration=600):
		s = Serializer(secret_key,expires_in=expiration)    
		return s.dumps({'id': self.id})
    
    #Add a method to verify auth tokens here
    @staticmethod
    def verify_auth_token(token):
    	s = Serializer(secret_key)
    	try:
    		data = s.loads(token)
    	except SignatureExpired:
    		return None
    	except BadSignature:
    		return None
    	user_id = data['id']
    	return user_id

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(String)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'name' : self.name,
        'category' : self.category,
        'price' : self.price
            }

engine = create_engine('sqlite:///regalTree.db')
 

Base.metadata.create_all(engine)