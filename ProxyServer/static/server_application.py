# start : python application.py

#!/usr/bin/env python 
#coding: utf-8

from flask import Flask, jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    data={'title':'서버 연동 성공'}
    return jsonify(data)

@application.route("/db")
def db():
    return "db  DB"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
    