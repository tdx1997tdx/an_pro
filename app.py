from flask import Flask, request
from route.home_page import homepage_page
from route.login import login
from route.register import register
from route.file_page import file_page
from route.image import image
app = Flask(__name__)
app.register_blueprint(homepage_page)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(file_page)
app.register_blueprint(image)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return '欢迎来到cs_304期末project'


@app.route('/test',methods=['GET','POST'])
def test():
    if(request.form.get('data1')=="我好牛逼"):
        return '你好牛逼'
    return '你不牛逼'


if __name__ == '__main__':
    app.run(threaded=True)
