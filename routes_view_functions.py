from flask import Flask, render_template, url_for, request
from flask import make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.google.com')


@app.route('/<user>')
def new_user(user):
    return '<h2> Welcome %s' %user

new_user('baller')

if __name__ == '__main__':
    app.run(debug=True)