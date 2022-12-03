# start : python application.py

#!/usr/bin/env python 
#coding: utf-8

# flask 구동과 db_sql을 분리하자.

from flask import Flask, request, session
import sqlalchemy as sqalc

app = Flask(__name__)

app.secret_key = "6f889680e52605e7ffab427d59811231400beb70c7edbadd6d62640d5bdec49e"
 
@app.route("/")
def hello():
    return "Hello goorm!"

# 3) 로그인 url 개설 -> 클라와 flask세션 연결을 위해서
# 플라스크 세션 사용할 것; session.get
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 사용자의 post -> 보안
    if request.method == 'POST': # post만 남길경우 삭제할 것.
        user_id = request.form['id'] # 4) 사용자의 '로그인 폼' 데이터 -> DB와 비교 예정
        user_pw = request.form['password']
        # 5) DB 쿼리 요청 -> form 데이터 검증
        # 6) 검증 결과(T)면, flask세션에 id 등록
        session['id'] = user_id
        return f'{test.get_json()}'
    else:
        #return show_the_login_form()
        pass
    
if __name__ == "__main__":
    # 1) db_connect와 연결 설정 -> 쿼리 가능.
    # 2) flask 구동 -> url 사용 가능.
    app.run(host='0.0.0.0', port=3833)