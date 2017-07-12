from sqlalchemy.engine.reflection import Inspector
from db import Category, DBSession, engine, Base

categories = [
    "Alternative",
    "Blues",
    "Acoustic Blues",
    "Children's Music",
    "Christian Gospel",
    "Classical",
    "Country",
    "Dance",
    "Easy Listening",
    "Electronic",
    "Hip Hop/Rap",
    "Holiday",
    "Industrial",
    "Jazz",
    "New Age",
    "Opera",
    "Pop",
    "R&B/Soul",
    "Reggae",
    "Rock",
    "Soundtrack",
    "World",
]

# @TODO create db if doesn't exist

inspector = Inspector.from_engine(engine)

# create tables if they don't exist yet
if not "categories" in inspector.get_table_names():
    Base.metadata.create_all(engine)
    session = DBSession()

    for category in categories:
        new_category = Category(name=category)
        session.add(new_category)

    session.commit()
    session.close()

# create Session instance




