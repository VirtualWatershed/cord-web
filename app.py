from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap


nav = Nav()

# registers the "top" menubar
nav.register_element('top', Navbar(
    View('CoRD Dashboard', 'home'),
    View('Cluster Modeling Progress', 'status'),
    View('Completed Model Runs (2 new)', 'completed'),
    View('Analyze Output Data', 'analyze'),
    View('Share Modelrun', 'share'),
))


app = Flask(__name__)
Bootstrap(app)
# [...] (view definitions)

nav.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    return render_template('index.html')

@app.route('/share')
def share():
    return render_template('index.html')

@app.route('/completed')
def completed():
    return render_template('index.html')
