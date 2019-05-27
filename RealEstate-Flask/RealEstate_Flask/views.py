"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from RealEstate_Flask import app
import pandas as pd
import shutil
import linecache
from itertools import islice

def binary_search(filename,search,no):
    first = 2
    last = no+1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        key,index=linecache.getline(filename, mid).strip().split("|")
        if key == search :
            found = True
            return index
        else:
            if search < key:
                last = mid - 1
            else:
                first = mid + 1    
    return 0



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

@app.route('/land')
def land():
    df=pd.read_csv("land.csv",index_col=0)
    num=len(df.index)
    loca=df.Location.unique().tolist()
    
    return render_template(
        'land.html',
        num=num,
        df=df,
        loca=loca,
        num_loca=len(loca)
    )

@app.route('/buyhome')
def buyhome():
    df=pd.read_csv("buyhome.csv")
    num=len(df.index)
    loca=df.Location.unique().tolist()
    """Renders the contact page."""
    return render_template(
        'buyhome.html',
        num=num,
        df=df,
        loca=loca,
        num_loca=len(loca)
    )

@app.route('/apart')
def apart():
    df=pd.read_csv("apart.csv",index_col=0)
    num=len(df.index)
    loca=df.Location.unique().tolist()
    """Renders the contact page."""
    return render_template(
        'apart.html',
        num=num,
        df=df,
        loca=loca,
        num_loca=len(loca)
    )

@app.route('/build')
def build():
    df=pd.read_csv("build.csv",index_col=0)
    num=len(df.index)
    loca=df.Location.unique().tolist()
    """Renders the contact page."""
    return render_template(
        'build.html',
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
        Title="Search our Properties",
        
    )

@app.route('/search',methods=['POST'])
def search_post():
    llocation = request.form['llocation'] 
    lsize = request.form['lsize'] 
    hnumber = request.form['bhnumber'] 
    hname = request.form['bhname'] 
    btype = request.form['BuyType']
    bnumber = request.form['bnumber']
    bname = request.form['bname']
    anumber = request.form['anumber']
    aname = request.form['aname']
    rtype = request.form['RentType']

    
    if(btype=='1'):
        lloca=llocation.upper().strip().replace(" ","")
        index="".join(str(ord(c)) for c in lloca[1:])
        key=llocation[0].upper()+index+str(lsize)
        fh=open("landindex.txt")
        no=int(fh.readline())
        index=binary_search("landindex.txt",key,no)

        bdf = pd.read_csv("land.csv",index_col=0)
        try:
            print(bdf.loc[key])
        except:
            return render_template(
            'search.html',
            Title="Property Not Found"
        )
        return render_template(
                'searchdisplay.html',
                bdf=bdf,
                num=int(index)
        )

    if(btype=='2'):
        hname=hname.strip().upper().replace(" ","")
        key=str(hnumber)+str(hname)
        fh=open("buyhomeindex.txt")
        no=int(fh.readline())
        index=binary_search("buyhomeindex.txt",key,no)

        hdf=pd.read_csv("buyhome.csv",index_col=2)
        try:
            print(hdf.loc[key])
        except:
            return render_template(
            'search.html',
            Title="Property Not Found"
        )
        return render_template(
                'searchdisplayhome.html',
                hdf=hdf,
                num=int(index)
        )

    if(rtype=='1'):
        bname=bname.strip().upper().replace(" ","")
        key=str(bnumber)+str(bname)
        fh=open("buildindex.txt")
        no=int(fh.readline())
        index=binary_search("buildindex.txt",key,no)

        df=pd.read_csv("build.csv",index_col=0)
        try:
            print(df.loc[key])
        except:
            return render_template(
            'search.html',
            Title="Property Not Found"
        )
        return render_template(
                'searchdisplaybuild.html',
                df=df,
                num=int(index)
        )

    if(rtype=='2'):
        aname=aname.strip().upper().replace(" ","")
        key=str(anumber)+str(aname)
        fh=open("apartindex.txt")
        no=int(fh.readline())
        index=binary_search("apartindex.txt",key,no)
        
        df=pd.read_csv("apart.csv",index_col=0)
        try:
            print(df.loc[key])
        except:
            return render_template(
            'search.html',
            Title="Property Not Found"
        )
        return render_template(
                'searchdisplayapart.html',
                df=df,
                num=int(index)
        )
  
    return render_template(
                'search.html',
                Title="Property Not Found"
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
             'login-invalid.html',
             ) 
    else:
        fhand.close()
        return render_template(
             'login-invalid.html',
             title='About'
             ) 
  
    
#ADMIN PAGES

@app.route('/page-register')
def register():         
    return render_template(
             'page-register.html',
             )
@app.route('/page-register',methods=['POST'])
def register_post():         
    username = request.form['Username']
    password = request.form['password']

    fadmin=open("AdminLogin.txt",'r+')
    userlist=[]
    for line in fadmin:
        user_txt,pass_txt=line.split("|")
        userlist.append(user_txt)
    if (username in userlist):
        print("Username already exists")
    else:
        fadmin.write("\n"+username+"|"+password)
        print("Successfully Added")
    fadmin.close()

    return render_template(
             'page-register.html',
    )

@app.route('/addland')
def addland():
    """Renders the addland page."""
    return render_template(
        'addland.html',
        Title='Add Land'
    )

@app.route('/addland',methods=['POST'])
def addland_post():
    location = request.form['location'] 
    price = request.form['price'] != None
    size = int(request.form['size'])
    cost=int(price)*size

    df=pd.read_csv("land.csv")
    num=len(df.index)
    loca=location.strip().upper()
    index="".join(str(ord(c)) for c in loca[1:])
    index=loca[0]+index+str(size)
    fh=open("landindex.txt")
    flag=0
    entries=int(fh.readline())
    for line in islice(fh,1,entries):
        ind,no=line.strip().split("|")
        if(ind==index):
            flag=1
            break
    fh.close()
    if flag==0:
        dic={'Index':index,'Location':location,'Price':price,'Size':size,'Cost':cost}
        add=pd.DataFrame(dic,index=[num])
        df=df.append(add)
        df.to_csv("land.csv",index=False)
        shutil.copy('landindex.txt','temp.txt')
        fhand=open("temp.txt",'r')
        fent=open("landindex.txt",'w')
        entries+=1
        ent=0
        fent.write(str(entries)+'\n')
        fent.close()
        find=open("landindex.txt",'w')
        for line in fhand:
            try:
                ind,add=line.split("|")
            except:
                continue
            if(index>ind):
                find.write(line)
            else:
                ent=1
                find.write(index+'|'+str(num)+'\n')
                find.write(line)
                for line in fhand:
                    find.write(line)
                break
        if (ent==0):
            find.write(index+'|'+str(num)+'\n')
        fhand.close()
        find.close()
        return render_template(
        'addland.html'
        )

    return render_template(
        'addland-invalid.html'
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

@app.route('/deleteland')
def deleteland():
    """Renders the addland page."""
    return render_template(
        'deleteland.html',
    )

@app.route('/deleteland' , methods=['POST'])
def deleteland_post():
    location = request.form['location']
    size = int(request.form['size'])

    loca=location.strip().upper()
    index="".join(str(ord(c)) for c in loca[1:])
    index=loca[0]+index+str(size)
    flag=0
    fh=open("landindex.txt")
    _=fh.readline()
    for line in fh:
        ind,no=line.strip().split("|")
        if(ind==index):
            flag=1
            break
    if flag==1: 
        df=pd.read_csv("land.csv")
        df=df[df.Index != index]
        df.to_csv("land.csv",index=False)
        df=pd.read_csv("land.csv")
        ind=list(df.Index)
        num=list(df.index)
        entries=len(df.Index)
        dic=dict(zip(ind,num))
        fhind=open('landindex.txt','w')
        fhind.write(str(entries)+'\n')
        for i in sorted(dic) : 
            fhind.write(str(i)+'|'+str(dic[i])+'\n')
        fhind.close()
        return render_template(
        'deleteland.html',
        Title="Sucessfully Deleted"
    )

    """Renders the addland page."""
    return render_template(
        'deleteland.html',
        Title="Land Does not Exist"
    )


@app.route('/addhome')
def addhome():
    """Renders the addland page."""
    return render_template(
        'addhome.html',
        Title="Add Home"
    )

@app.route('/addhome',methods=['POST'])
def addhome_post():
    number = request.form['houseno']
    name = request.form['housename']
    location = request.form['location']
    price = request.form['price']
    bed = request.form['bed']
    bath = request.form['bath']
    

    df=pd.read_csv("buyhome.csv")
    num=len(df.index)
    hname=name.strip().upper().replace(" ","")
    index=str(number)+str(hname)
    fh=open("buyhomeindex.txt")
    flag=0
    entries=int(fh.readline())
    for line in islice(fh,0,entries):
        ind,no=line.strip().split("|")
        if(ind==index):
            print(ind)
            flag=1
            break
    fh.close()
    if flag==0:
        dic={'Index':index,'Number':number,'Name':name,'Location':location,'Price':price,'Bed':bed,'Bath':bath}
        add=pd.DataFrame(dic,index=[num])
        df=df.append(add)
        df.to_csv("buyhome.csv",index=False)
        shutil.copy('buyhomeindex.txt','temp.txt')
        fhand=open("temp.txt",'r')
        fent=open("buyhomeindex.txt",'w')
        entries+=1
        ent=0
        fent.write(str(entries)+'\n')
        fent.close()
        find=open("buyhomeindex.txt",'a')
        for line in fhand:
            try:
                ind,add=line.split("|")
            except:
                continue
            if(index>ind):
                find.write(line)
            else:
                ent=1
                find.write(index+'|'+str(num)+'\n')
                find.write(line)
                for line in fhand:
                    find.write(line)
                break
        if (ent==0):
            find.write(index+'|'+str(num)+'\n')        
        fhand.close()
        find.close()
        return render_template(
        'addhome.html',
        Title="Succesfully Added"
        )
    return render_template(
        'addhome-invalid.html'
    )



@app.route('/disphome')
def disphome():
    df=pd.read_csv("buyhome.csv")
    num=len(df.index)

    return render_template(
        'disphome.html',
        df=df,
        num=num
    )

@app.route('/deletehome')
def deletehome():
    """Renders the addland page."""
    return render_template(
        'deletehome.html',
    )

@app.route('/deletehome' , methods=['POST'])
def deletehome_post():
    number = request.form['number']
    name = request.form['name']

    hname=name.strip().upper().replace(" ","")
    index=str(number)+str(hname)
    flag=0
    fh=open("buyhomeindex.txt")
    _=fh.readline()
    for line in fh:
        ind,no=line.strip().split("|")
        if(ind==index):
            flag=1
            break 

    if flag==1:        
        df=pd.read_csv("buyhome.csv")
        df=df[df.Index != index]
        df.to_csv("buyhome.csv",index=False)
        ind=list(df.Index)
        num=list(df.index)
        entries=len(df.Index)
        dic=dict(zip(ind,num))
        fhind=open('buyhomeindex.txt','w')
        fhind.write(str(entries)+'\n')
        for i in sorted(dic) : 
            fhind.write(str(i)+'|'+str(dic[i])+'\n')
        fhind.close()
        return render_template(
        'deletehome.html',
        Title="Sucessfully Deleted"
    )

    return render_template(
        'deletehome.html',
        Title="House Does not Exist"
    )

@app.route('/addbuild')
def addbuild():
    """Renders the addland page."""
    return render_template(
        'addbuild.html',
        Title='Add Building'
    )

@app.route('/addbuild',methods=['POST'])
def addbuild_post():
    number = request.form['buildno']
    name = request.form['buildname']
    location = request.form['location']
    price = request.form['price']
    size = request.form['size']
    road = request.form['road']
    

    df=pd.read_csv("build.csv")
    num=len(df.index)
    hname=name.strip().upper().replace(" ","")
    index=str(number)+str(hname)
    fh=open("buildindex.txt")
    flag=0
    entries=int(fh.readline())
    for line in islice(fh,0,entries):
        ind,no=line.strip().split("|")
        if(ind==index):
            flag=1
            break
    fh.close()
    if flag==0:
        dic={'Index':index,'Number':number,'Name':name,'Location':location,'Price':price,'Size':size,'Main_Road_Access':road}
        add=pd.DataFrame(dic,index=[num])
        df=df.append(add)
        df.to_csv("build.csv",index=False)
        shutil.copy('buildindex.txt','temp.txt')
        fhand=open("temp.txt",'r')
        fent=open("buildindex.txt",'w')
        entries+=1
        ent=0
        fent.write(str(entries)+'\n')
        fent.close()
        find=open("buildindex.txt",'a')
        for line in fhand:
            try:
                ind,add=line.split("|")
            except:
                continue
            if(index>ind):
                find.write(line)
            else:
                ent=1
                find.write(index+'|'+str(num)+'\n')
                find.write(line)
                for line in fhand:
                    find.write(line)
                break
        if (ent==0):
            find.write(index+'|'+str(num)+'\n')
        fhand.close()
        find.close()
        return render_template(
            'addbuild.html',
            Title="Succesfully Added"
        )
    return render_template(
        'addbuild-invalid.html'
    )

@app.route('/dispbuild')
def dispbuild():
    df=pd.read_csv("build.csv",index_col=0)
    num=len(df.index)

    return render_template(
        'dispbuild.html',
        df=df,
        num=num
    )

@app.route('/deletebuild')
def deletebuild():
    """Renders the addland page."""
    return render_template(
        'deletebuild.html',
    )

@app.route('/deletebuild' , methods=['POST'])
def deletebuild_post():
    number = request.form['number']
    name = request.form['name']

    hname=name.strip().upper().replace(" ","")
    index=str(number)+str(hname)
    flag=0
    fh=open("buildindex.txt")
    _=fh.readline()
    for line in fh:
        ind,no=line.strip().split("|")
        if(ind==index):
            flag=1
            break 

    if flag==1:        
        df=pd.read_csv("build.csv")
        df=df[df.Index != index]
        df.to_csv("build.csv",index=False)
        df=pd.read_csv("build.csv")
        ind=list(df.Index)
        num=list(df.index)
        entries=len(df.Index)
        dic=dict(zip(ind,num))
        fhind=open('buildindex.txt','w')
        fhind.write(str(entries)+'\n')
        for i in sorted(dic) : 
            fhind.write(str(i)+'|'+str(dic[i])+'\n')
        fhind.close()
        return render_template(
        'deletebuild.html',
        Title="Sucessfully Deleted"
    )

    return render_template(
        'deletebuild.html',
        Title="Building Does not Exist"

    )

@app.route('/addapart')
def addapart():
    """Renders the addland page."""
    return render_template(
        'addapart.html',
        Title='Add Apartment'
    )

@app.route('/addapart',methods=['POST'])
def addapart_post():
    number = request.form['apartno']
    name = request.form['apartname']
    location = request.form['location']
    price = request.form['price']
    bed = request.form['bed']
    bath = request.form['bath']
    floor = request.form['floor']
    

    df=pd.read_csv("apart.csv")
    num=len(df.index)
    hname=name.strip().upper().replace(" ","")
    index=str(number)+str(hname)
    fh=open("apartindex.txt")
    flag=0
    entries=int(fh.readline())
    for line in islice(fh,0,entries):
        ind,no=line.strip().split("|")
        if(ind==index):
            flag=1
            break
    fh.close()
    if flag==0:
        dic={'Index':index,'Number':number,'Name':name,'Location':location,'Rent':price,'Bed':bed,'Bath':bath,'Apartment_Floor':floor}
        add=pd.DataFrame(dic,index=[num])
        df=df.append(add)
        df.to_csv("apart.csv",index=False)
        shutil.copy('apartindex.txt','temp.txt')
        fhand=open("temp.txt",'r')
        fent=open("apartindex.txt",'w')
        entries+=1
        ent=0
        fent.write(str(entries)+'\n')
        fent.close()
        find=open("apartindex.txt",'a')
        for line in fhand:
            try:
                ind,add=line.split("|")
            except:
                continue
            if(index>ind):
                find.write(line)
            else:
                ent=1
                find.write(index+'|'+str(num)+'\n')
                find.write(line)
                for line in fhand:
                    find.write(line)
                break
        if (ent==0):
            find.write(index+'|'+str(num)+'\n')
        fhand.close()
        find.close()
        return render_template(
            'addapart.html',
            Title="Succesfully Added"
        )
    return render_template(
        'addapart-invalid.html'
    )

@app.route('/dispapart')
def dispapart():
    df=pd.read_csv("apart.csv",index_col=0)
    num=len(df.index)

    return render_template(
        'dispapart.html',
        df=df,
        num=num
    )

@app.route('/deleteapart')
def deleteapart():
    """Renders the addland page."""
    return render_template(
        'deleteapart.html',
        Title="Delete Apartment"
    )

@app.route('/deleteapart' , methods=['POST'])
def deleteapart_post():
    number = request.form['number']
    name = request.form['name']
        
    hname=name.strip().upper().replace(" ","")
    index=str(number)+str(hname)
    flag=0
    fh=open("apartindex.txt")
    _=fh.readline()
    for line in fh:
        ind,no=line.strip().split("|")
        if(ind==index):
            flag=1
            break           

    if flag==1:
        df=pd.read_csv("apart.csv")
        df=df[df.Index != index]
        df.to_csv("apart.csv",index=False)
        df=pd.read_csv("apart.csv")
        ind=list(df.Index)
        num=list(df.index)
        entries=len(df.Index)
        dic=dict(zip(ind,num))
        fhind=open('apartindex.txt','w')
        fhind.write(str(entries)+'\n')
        for i in sorted(dic) : 
            fhind.write(str(i)+'|'+str(dic[i])+'\n')
        fhind.close()
        return render_template(
            'deletebuild.html',
            Title="Sucessfully Deleted"
        )
    return render_template(
        'deletebuild.html',
        Title="Apartment Does not Exist"
    )
    
    