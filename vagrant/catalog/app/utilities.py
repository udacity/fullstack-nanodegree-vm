from flask import make_response, redirect
from functools import wraps
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import json
import random
import string

from werkzeug.contrib.atom import AtomFeed
from flask import session as login_session


def status(message, status_code, status_type):
    '''
        Returns message headers for both xml and json content type.
    '''
    response = {'json': {'function': json.dumps, 'data_type': 'application/json'},
                'xml': {'function': ET.tostring, 'data_type': 'application/xml'}}

    res = make_response(response[status_type]
                        ['function'](message), status_code)
    res.headers['Content-Type'] = response[status_type]['data_type']
    return res


def create_feed(name, request):
    return AtomFeed(name, feed_url=request.url, url=request.url_root)


def convert_object_to_xml(tag, content):
    '''
       Converts object content to xml
    '''
    root = Element(tag)
    for key, val in content.items():
        child = Element(key)
        child.text = str(val)
        root.append(child)
    return root


def convert_list_to_xml(tag, element):
    '''
       Converts element object onto xml object
    '''
    root = Element(tag)
    for val in element:
        root.append(val)
    return root


def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        '''
            Decorator for views that checks that the user is logged in, redirecting
            to the category page if necessary.
        '''
        email = login_session.get('access_token')
        if email is None:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function


def random_state():
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for x in xrange(32))
