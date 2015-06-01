"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
import random
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
    
@app.route('/bobbym')
def bobbym():
    return markov()

def markov():
    chain = {}
    
    data = open('resources/bobbym_quotes').read().split('\n')
    data = ' '.join(data)
    data = data.split(' ')
    words = data
    
    prefix = " "
    
    for i in xrange(len(words)):
    	prefix = words[i]
    	try:
    		suffix = words[i+1]
    	except:
    		suffix = ""
    	if prefix in chain:
    		chain[prefix].append(suffix)
    	else:
    		chain[prefix] = [suffix]
    
    text = ""
    
    state = random.choice(chain.keys())
    for i in xrange(1000):
    	text += " " + state
    	print state, 
    	if state not in chain:
    		break
    	state = random.choice(chain[state])
    
    return text

