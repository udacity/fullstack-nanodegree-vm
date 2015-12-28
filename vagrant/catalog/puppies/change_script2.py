#change script for puppyshelter database
from sqlalchemy import Base, Shelter, Column, Integer, String, MetaData, relationship


meta = MetaData()

#on shelter
def current_occupancy(self, session):
    return session.query(Puppy).join("shelter").filter(Puppy.shelter_id==self.id).count()


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    account = Table('account', meta, autoload=True)
    emailc = Column('email', String(128))
    emailc.create(account)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    account = Table('account', meta, autoload=True)
    account.c.email.drop()