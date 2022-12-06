# start : python application.py

#!/usr/bin/env python 
#coding: utf-8

from flask import Flask, request, session
import sqlalchemy as sqalc

app = Flask(__name__)

app.secret_key = "6f889680e52605e7ffab427d59811231400beb70c7edbadd6d62640d5bdec49e"

@app.route("/")
def hello():
    return "Hello goorm!"

# @app.route("/db")
# def db():
#     return "db  DB"

# 플라스크 세션 사용; session.add
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method:
        pass

# 플라스크 세션 사용할 것; session.get
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #return do_the_login()
        #test= request.form["test"]
        test= request.get_json()
        #test= request.is_json()
        #test = request.host_url
        return f'{test}'
    else:
        #return show_the_login_form()
        pass

if __name__ == "__main__":
    #print(f"sqlAchemy version is {sqalc.__version__}")
    app.run(host='0.0.0.0', port=3833)