# start : python application.py

#!/usr/bin/env python 
#coding: utf-8

from flask import Flask
import sqlalchemy as sqalc

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/db")
def db():
    return "db  DB"

if __name__ == "__main__":
    print(f"sqlAchemy version is {sqalc.__version__}")
    application.run(host='0.0.0.0', port=3833)