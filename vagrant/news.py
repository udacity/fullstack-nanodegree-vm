#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from newsdb import get_allpercenterror, get_articlelogdatas, get_popularauthors, get_morethantwopercent

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title> News Error </title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
    </style>
  </head>
  <body>
    <h1>NEWS ERROR RATE</h1>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post>
    <em class=time>%s  </em> -----  %s<span>&#37;</span>  <span>error</span> <br>
    </div>
'''

HTML_WRAP1 = '''\
<!DOCTYPE html>
<html>
  <head>
    <title> News Error </title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
    </style>
  </head>
  <body>
    <h1>Number of Views</h1>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

POST1 = '''\
    <div class=post>
    <em class=time>%s  </em> -----  %s  <span>views</span> <br>
    </div>
'''

@app.route('/allerror', methods=['GET'])
def main():
    '''Main page of the forum.'''
    posts = "".join(POST % (date, percenterror)
                    for date, percenterror in get_allpercenterror())
    html = HTML_WRAP % posts
    return html

@app.route('/highesterror', methods=['GET'])
def highestError():
    '''Main page of the forum.'''
    posts = "".join(POST % (date, percenterror)
                    for date, percenterror in get_morethantwopercent())
    html = HTML_WRAP % posts
    return html

@app.route('/popularauthors', methods=['GET'])
def popularAuthors():
    '''Main page of the forum.'''
    posts = "".join(POST1 % (name, sum)
                    for name, sum in get_popularauthors())
    html = HTML_WRAP1 % posts
    return html