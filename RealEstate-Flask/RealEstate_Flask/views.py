"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from RealEstate_Flask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/page-login')
def login():         
    return render_template(
             'page-login.html',
             title='About'
             )

@app.route('/page-login',methods=['POST'])
def login_post():         
    username = request.form['Username']
    password = request.form['password']
    fhand = open("AdminLogin.txt",mode='r')
    for line in fhand:
        user_txt,pass_txt=line.split("|")
        if(user_txt!=username):
            continue
        if(password==pass_txt.strip()):
            return render_template(
             'index.html',
             title='About'
             ) 
        else:
            fhand.close()
            return render_template(
             'page-login.html',
             title='About'
             ) 
    else:
        fhand.close()
        return render_template(
             'page-login.html',
             title='About'
             ) 
    