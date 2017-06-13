#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Restaurant, MenuItem, Base

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

def add_restaurant_to_db(name):
    restaurant_name = Restaurant(name = name)
    session.add(restaurant_name)
    session.commit()
    return restaurant_name


def add_menu_item_to_db(menu, description, price, course, restaurant):
    menu_name = MenuItem(
        name = menu,
        description = description,
        price = price,
        course = course,
        restaurant = restaurant
    )
    session.add(menu_name)
    session.commit()

firstRestaurant = add_restaurant_to_db('restaurant_beta')
add_menu_item_to_db(
    'Veggie Burger',
    'Juicy grilled veggie patty with tomato mayo and lettuce',
    '$7.50',
    'Entree',
    firstRestaurant
)
