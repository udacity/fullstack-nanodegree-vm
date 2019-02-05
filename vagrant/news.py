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