# Import the Flask Framework
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from string import printable
import kabooblydoo, urllib2, re
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


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
    
@app.route('/kabooblydoo', methods=['GET', 'POST'])
def nonsense():
    n = int(request.form['n'])
    w = int(request.form['words'])
    if request.form['source']=='url':
        s = filter(lambda x: x in printable, urllib2.urlopen(request.form['url']).read())
    elif request.form['source']=='book':
        if request.form['books']=='bobbym':
            s = open('resources/bobbym_quotes').read()
        elif request.form['books']=='aesop':
            s = open('resources/aesop').read()
        elif request.form['books']=='word':
            s = open('resources/word').read()
        elif request.form['books']=='alice':
            s = open('resources/alice').read()
        elif request.form['books']=='benjamin':
            s = open('resources/benjamin').read()
    else:
        s = request.form['message']
    return render_template('output.html', error=None, output=kabooblydoo.kabooblydoo(s,n,w))
    
@app.route('/youtubedl', methods = ['GET'])
def generate_link():
    search_link = "http://www.youtube.com/results?search_query="+request.args.get('query')
    youtube_id = re.findall(r'href=\"\/watch\?v=(.{11})',urllib2.urlopen(search_link).read())[0]
    link = "http://www.youtubeinmp3.com/fetch/?video="+"http://www.youtube.com/watch?v=" + youtube_id
    return redirect(link, code=302)