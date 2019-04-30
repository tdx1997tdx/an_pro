from flask import Blueprint, request
from mysql_op import welcome_mysql_op as wop

welcome_page=Blueprint("welcome_page",__name__)

@welcome_page.route('/login',methods=['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)
    if(username or password):
        return 'NOTOK'
    return wop.login_mysql_op(username,password)


@welcome_page.route('/register',methods=['GET','POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if (username or password):
        return 'RNOTOK'
    return wop.register_mysql_op(username,password)