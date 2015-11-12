from flask import make_response, redirect
from functools import wraps
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import json
import random
import string


def status(message, status_code, status_type):
    response = {'json': {'function': json.dumps, 'data_type': 'application/json'},
                'xml': {'function': ET.tostring, 'data_type': 'application/xml'},
                'rss': {'function': ET.tostring, 'data_type': 'application/rss+xml'}}
    res = make_response(response[status_type]
                        ['function'](message), status_code)
    res.headers['Content-Type'] = response[status_type]['data_type']
    return res


def random_state():
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for x in xrange(32))
