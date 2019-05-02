"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from RealEstate_Flask import app
import pandas as pd



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
        message='Your contact page.',
        i=[1,2,3,4]
    )

@app.route('/land')
def land():
    df=pd.read_csv("land.csv",index_col=0)
    num=len(df.index)
    loca=df.Location.unique().tolist()
    """Renders the contact page."""
    return render_template(
        'land.html',
        num=num,
        df=df,
        loca=loca,
        num_loca=len(loca)
    )

@app.route('/search')
def search():
    """Renders the contact page."""
    return render_template(
        'search.html',
        
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
             'adminindex.html'
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
  
    
#ADMIN PAGES

@app.route('/addland')
def addland():
    """Renders the addland page."""
    return render_template(
        'addland.html'
    )

@app.route('/addland',methods=['POST'])
def addland_post():
 
    location = request.form['location']
    price = int(request.form['price'])
    size = int(request.form['size'])
    cost=price*size

    df=pd.read_csv("land.csv",index_col=0)
    loca=location.strip().upper()
    index=int("".join(str(ord(c)) for c in loca))
    dic={'Location':location,'Price':price,'Size':size,'Cost':cost}
    add=pd.DataFrame(dic,index=[index])
    df=df.append(add)
    df.to_csv("land.csv")

    return render_template(
        'index.html'
    )

@app.route('/displand')
def displand():
    df=pd.read_csv("land.csv")
    num=len(df.index)
    """Renders the addland page."""
    return render_template(
        'displand.html',
        df=df,
        num=num
    )