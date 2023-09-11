from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/<name>')
def user(name):
    return '<h1> Your called %s</h1>' %name

user('Philemon Tebo')