# Import the Flask Framework
from flask import Flask
from flask import request
from flask import render_template
import kabooblydoo
app = Flask(__name__)


@app.route('/')
def hello():
    render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
    
@app.route('/bobbym', methods=['GET'])
def bobbym(n=None):
    f = open('resources/bobbym_quotes').read()
    if request.args.get('n'):
        return kabooblydoo.kabooblydoo(f,int(request.args.get('n')))
    return kabooblydoo.kabooblydoo(f)