from sqlalchemy import create_engine

# @TODO - disable extra logging
engine = create_engine("postgresql://vagrant:vagrant@localhost/forum", echo=True)

con = engine.connect()
print con