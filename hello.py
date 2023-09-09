from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the index page'

@app.route('/index')
def hello():
    return 'This is the home page'