# Import the Flask Framework
from flask import Flask
import kabooblydoo
app = Flask(__name__)
app.debug = True


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
    
@app.route('/bobbym/<int:n>')
def bobbym(n=None):
    f = open('resources/bobbym_quotes').read()
    if n:
        return kabooblydoo.kabooblydoo(f,n)
    return kabooblydoo.kabooblydoo(f)