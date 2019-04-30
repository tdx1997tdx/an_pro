from flask import Blueprint, request
from mysql_op import welcome_mysql_op as wop

homepage_page=Blueprint("homepage_page",__name__)

@homepage_page.route('/update_infomation',methods=['GET','POST'])
def update_infomation():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)
    if(username or password):
        return 'NOTOK'
    return wop.login_mysql_op(username,password)
