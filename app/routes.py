from app import app

  
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
