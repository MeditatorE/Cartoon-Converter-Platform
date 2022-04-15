from flask import Flask,render_template
from flask import redirect
from flask import url_for
from flask import request
from check_tools import is_existed,exist_user,is_null,add_user
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return redirect( url_for('user_login') )

@app.route('/user_login',methods=['GET','POST'])
def user_login():
    if request.method=='POST':  # 注册发送的请求为POST请求
        username = request.form['username']
        password = request.form['password']
        if is_null(username,password):
            login_massage = "username or password can't be empty"
            return render_template('login.html', message=login_massage)
        elif is_existed(username,password):
            return render_template('index.html', username=username)
        elif exist_user(username,password):
            login_massage = "password is not correct"
            return render_template('login.html', message=login_massage)
        else:
            login_massage = "user not exist"
            return render_template('login.html', message=login_massage)
    return render_template('login.html')

@app.route("/regiser",methods=["GET", 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if is_null(username,password):
            login_massage = "username and password can't be empty"
            return render_template('register.html', message=login_massage)
        elif exist_user(username,password):
            login_massage = "user already exist, please login"
            return render_template('register.html',message=login_massage)
        else:
            add_user(request.form['username'], request.form['password'])
            # register_massage = "Register Success! now you can turn to login page"
            # return render_template('register.html',message=register_massage)
            return render_template('index.html',username=username,password=password)
    return render_template('register.html')


def LoginWebPage():
    url = 'http://127.0.0.1:5000'
    webbrowser.open_new(url)
    app.run()


LoginWebPage()

