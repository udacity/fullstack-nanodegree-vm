#!/usr/bin/env python3

from flask import Flask

def main():
    app = Flask(__name__)

    @app.route('/restaurants/', methods=['GET'])
    def restaurants():
        res = '/restaurants'
        return res

    @app.route('/restaurant/new/', methods=['GET', 'POST'])
    def restaurant_new():
        res = '/restaurant/new'
        return res

    @app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET','POST'])
    def restaurant_edit(restaurant_id):
        res = '/restaurant/{}/edit'.format(restaurant_id)
        return res

    @app.route('/restaurant/<int:restaurant_id>/delete/',
        methods=['GET','POST'])
    def restaurant_delete(restaurant_id):
        res = '/restaurant/{}/delete'.format(restaurant_id)
        return res

    @app.route('/restaurant/<int:restaurant_id>/menu/', methods=['GET'])
    @app.route('/restaurant/<int:restaurant_id>', methods=['GET'])
    def restaurant_menu(restaurant_id):
        res = '/restaurant/{}/menu'.format(restaurant_id)
        return res

    @app.route('/restaurant/<int:restaurant_id>/menu/new/',
        methods=['GET', 'POST'])
    def restaurant_menu_item_new(restaurant_id):
        res = '/restaurant/{}/menu/new'.format(restaurant_id)
        return res

    @app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit/',
        methods=['GET', 'POST'])
    def restaurant_menu_item_edit(restaurant_id, menu_item_id):
        res = '/restaurant/{}/menu/{}/edit'.format(restaurant_id, menu_item_id)
        return res

    @app.route(
        '/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/delete/',
        methods=['GET', 'POST'])
    def restaurant_menu_item_delete(restaurant_id, menu_item_id):
        res = \
            '/restaurant/{}/menu/{}/delete'.format(restaurant_id, menu_item_id)
        return res

    app.secret_key = 'debug_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
