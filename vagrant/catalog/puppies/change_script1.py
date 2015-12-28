#change script for puppyshelter database
from sqlalchemy import Column, Integer, String, MetaData
from migrate.changeset.constraint import ForeignKeyConstraint
from database_setup import Base, Puppy

meta = MetaData()

#new table puppypage
class PuppyPage(Base):
    __tablename__ = 'puppypage'
    id = Column(Integer, primary_key=True)
    url = Column(String(), nullable=False)
    puppy_description = Column(String(140))
    special_needs = Column(String(250))
    #puppy_id = Column(Integer, ForeignKey('puppy.id'), primary_key=True)
    #puppy = relationship(Puppy)
    puppy_id = ForeignKeyConstraint('puppy_id', 'puppy.id', Puppy)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    PuppyPage.create()
    print "Upgrade OK!\n"


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    PuppyPage.drop()
    print "Downgrade ok!\n"



"""    
cons = ForeignKeyConstraint([table.c.fkey], [othertable.c.id])
"""
# Create the constraint
#cons.create()

# Drop the constraint
#cons.drop()