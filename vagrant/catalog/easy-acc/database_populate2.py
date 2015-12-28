#database connection for my easy-acc project

import sys
#from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

#defining constants
FLOW_DIRECTION = Enum( 'Credit', 'Debit', name='FLOW_DIRECTION')
ACCOUNT_TYPE = Enum('Balanco', 'Gestao', 'Especiais', name='ACCOUNT_TYPE')

#Class setup

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	permission = Column (String(10), nullable=False)

class Currency(Base):
	__tablename__ = 'currencies'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	international_code = Column(String(3), nullable=False)
	
class Movement(Base):
	__tablename__ = 'movements'
	id = Column(Integer, primary_key=True)
	date = Column( Date, nullable=False)

class AccountGroup(Base):
	__tablename__ = 'accountgroups'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	type= Column('ACCOUNT_TYPE', ACCOUNT_TYPE)
	
class AccountSubgroup(Base):
	__tablename__ = 'accountsubgroups'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	group_id = Column(Integer, ForeignKey('accountgroups.id'))
	group = relationship(AccountGroup)

class Account(Base):
	__tablename__ = 'accounts'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	subgroup= Column(String(5))
	group_id = Column(Integer, ForeignKey('accountgroups.id'))
	group = relationship(AccountGroup)
	subgroup_id = Column(Integer, ForeignKey('accountsubgroups.id'))
	subgroup = relationship(AccountSubgroup)
	currency_id = Column(Integer, ForeignKey('currencies.id'))
	currency = relationship(Currency)


class Flow(Base):
	__tablename__ = 'flows'
	id = Column(Integer, primary_key=True)
	value = Column(Float, nullable=False)
	direction = Column('FLOW_DIRECTION', FLOW_DIRECTION)
	account_id = Column(Integer, ForeignKey('accounts.id'))
	account = relationship(Account)
	
#insert at end of file

engine = create_engine('sqlite:///easy-acc.db')

Base.metadata.create_all(engine)