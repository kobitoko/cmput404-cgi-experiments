#!/usr/bin/env python
# accidental !/usr/bin/env/ python  causes bug. That extra slash at end of env.

import cgi
import os
import json
import sys

form = cgi.FieldStorage()
loggedinok = False

# extra: How to delete cookies from http://www.perlmonks.org/?node_id=18718
# and http://raspberrywebserver.com/cgiscripting/using-python-to-set-retreive-and-clear-cookies.html
# Use "expires" or you can send the cookie again with a null value "";

if(form.getvalue('user')=="bob" and form.getvalue('password')=="123"
    or 'loggedin' in os.environ['HTTP_COOKIE']):
    loggedinok = True

# http://localhost:8000/cgi_script.py
# Anything you print in CGI will get send to the output html in the client's browser
print "Content-type: text/html"
if(loggedinok):
    print "Set-Cookie: loggedin=true"
# Header end
print

print "<HTML><BODY>Hi."

# Make a form.
print "<FORM method='POST'><INPUT name='user'/>"
print "<INPUT name='password' type='password'/>"
print "<BUTTON type='submit'>Log in</BUTTON>"
print "</Form>"

# You can access the environment vars with os really easy like so:
print "<P>Query string was: " + os.environ['QUERY_STRING'] + "</P>" 
print "<p>Your browser is:" + os.environ['HTTP_USER_AGENT'] + "</p>"

# NOT used cuz using python module that handles this and symbols so we dont need to deal with %20 etc.
# Check content len because when first visting, it is empty.
#if os.environ['CONTENT_LENGTH']:
#    print "Standard input is: " + sys.stdin.read(int(os.environ['CONTENT_LENGTH'])) 

# Check for just GETS so values are empty.
if(form.getvalue('user') != None):
    print "<p>"
    print "User name was: " + form.getvalue('user') + "."
    print "Password name was: " + form.getvalue('password') + "."
    print "</p>"

if(loggedinok):
    print "<H2>Logged in ok</H2>"

# Prints shell environment and http headers
cgi.print_environ()
# Json formatted env vars.
print json.dumps(dict(os.environ), indent=4)

print "</BODY></HTML>"

