from flask import Blueprint,render_template,make_response,send_from_directory,jsonify,session,redirect,url_for,json,request
import op_mysql as op
welcome=Blueprint("welcome",__name__)

@welcome.route('/login',methods=['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    result = [i for i in op.select("select * from user where username='%s' and password='%s'"%(username,password))]
    if(result==[]):
        return 'NOTOK'
    else:
        return 'OK'

@welcome.route('/register',methods=['GET','POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    result = [i for i in op.select("select * from user where username='%s'"%(username))]
    print(username,password)
    if(result==[]):
        if(op.insert("insert into user (username,password) values ('%s','%s')"%(username,password))):
            return 'ROK'
        else:
            return 'RNOTOK'
    else:
        return 'EXIST'