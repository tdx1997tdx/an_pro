from flask import Blueprint,render_template,make_response,send_from_directory,jsonify,session,redirect,url_for,json,request
import op_mysql as op
welcome=Blueprint("welcome",__name__)

@welcome.route('/login',methods=['GET','POST'])
def name_search():
    username = request.form.get('username')
    password = request.form.get('password')
    result = [i for i in op.select("select * from user where username='%s' and password='%s'"%(username,password))]
    print(username,password)
    if(result==[]):
        return 'NOTOK'
    else:
        return 'OK'