# start : python application.py

#!/usr/bin/env python 
#coding: utf-8

# flask 구동과 db_sql을 분리하자.

from flask import Flask, request, session, redirect, url_for
import sqlalchemy as sqalc
from dbconnect_prac_automap import DBConnect

app = Flask(__name__)

app.secret_key = "6f889680e52605e7ffab427d59811231400beb70c7edbadd6d62640d5bdec49e"
 
@app.route("/")
def hello():
    if user_id in session:
        return f"Hello {user_id}!!"
    else:
        return "Hello John."

# 3) 로그인 url 개설 -> 클라와 flask세션 연결을 위해서
# 플라스크 세션 사용할 것; session.get
@app.route('/login', methods=['POST', 'GET'])
def login():
    # 사용자의 post -> 보안
    if request.method == 'POST': # post만 남길경우 삭제할 것.
        posted_json= request.get_json()
        user_id = posted_json['id'] # 4) 사용자의 '로그인 폼' 데이터 -> DB와 비교 예정
        user_pw = posted_json['password']
        # 5) DB 쿼리 요청 -> form 데이터 검증
        result_sig= dbconn.login_func(check_id= user_id, check_pw= user_pw) # 로그인 검사 신호
        # 6) 검증 결과(T)면, 로그인(신원 확인)완료 flask세션에 id 등록
        if result_sig:
            # 세션이 존재하는지 확인 후
            print(f'user_id: {user_id}, type: {str(type(user_id))}')
            #세션 등록
            session['userid'] = user_id
            return redirect(url_for('usermain', user= user_id))
        else: # 검증 결과 실패, 로그인 다시 하도록.
            return "your access denied."
    else:
        #return show_the_login_form()
        pass

@app.route("/user/<user>")
def usermain(user):
    print(user)
    tempid= session.get('userid', None)
    if user == tempid:
        return f"Hello {user}!!"
    else:
        return f"{str(user), str(type(user)), str(tempid), str(type(tempid))}"
    
if __name__ == "__main__":
    # 1) db_connect와 연결 설정 -> 쿼리 가능.
    # "mysql+mysqldb://root:1234@localhost:3306/UserDB"
    dbconn= DBConnect(DBMS_name='mysql',
                      DBMS_id= 'root',
                      DBMS_pw= '1234',
                      DBMS_host= 'localhost',
                      DBMS_port= '3306',
                      DBMS_useDB= 'UserDB')
    
    # 2) flask 구동 -> url 사용 가능.
    app.run(host='0.0.0.0', port=3833, debug=True)