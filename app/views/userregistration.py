#for user signup
import json
from app.app import login_manager
from app.models.usermodel import User
from flask_restful import Resource
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user
def userlogin():
    #user login
    if request.method == 'POST':
        user = User.objects.get(usermailid=request.form["usermailid"])
        if (user.userpassword==request.form["password"]):
            login_user(user)
            flash('You were successfully logged in')
            return render_template('task.html')
        else:
            render_template('login.html')
    return render_template('login.html')

def userregister():
    #user register
    if request.method == 'POST':
        username = request.form["username"]
        userpassword = request.form["userpassword"]
        usermailid = request.form["usermailid"]
        userrole = request.form["userrole"]
        userphoneno = request.form["userphoneno"]
        print(request.form)
        User.objects.create(username=username,userpassword=userpassword,
            usermailid=usermailid,userrole=userrole,userphoneno=userphoneno)
        return redirect(url_for('userlogin'))
    else:
        return render_template('register.html')
def logout():
    logout_user()
    return redirect(url_for('userlogin'))
