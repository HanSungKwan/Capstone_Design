# orm을 활용하자.
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy import text, select, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

class DBConnect:
    __dbms_name, __dbms_id, __dbms_pw, __dbms_host, __dbms_port, __dbms_useDB= '', '', '', '', '', ''
    __engine= None
    __Base= None
    __Users= None
    def __init__(self, DBMS_name:str='',
                 DBMS_id:str='', DBMS_pw:str='',
                 DBMS_host:str='', DBMS_port:str='',
                 DBMS_useDB:str=''):
        self.__dbms_name, self.__dbms_id, self.__dbms_pw= DBMS_name, DBMS_id, DBMS_pw
        self.__dbms_host, self.__dbms_port, self.__dbms_useDB= DBMS_host, DBMS_port, DBMS_useDB
        
        self.__Base = automap_base() # 데이터orm 토대 생성
        
        # DBMS_name 입력시 사용할 URL지정
        # temp코드; DBMS별 코드 추가 예정
        if self.__dbms_name == 'mysql' or self.__dbms_name == 'MYSQL':
            self.__engine = create_engine( # orm매핑을 위한 db설정
                #"mysql+mysqldb://root:1234@localhost:3306/UserDB"
                f"mysql+pymysql://{self.__dbms_id}:{self.__dbms_pw}@{self.__dbms_host}:{self.__dbms_port}/{self.__dbms_useDB}?charset=utf8mb4",
                echo=True)
        
        self.__Base.prepare(autoload_with= self.__engine) # 기존 DB에서 리플렉트
        self.__Users = self.__Base.classes.users
        self.__session = Session(self.__engine)
        
    def login_func(self, check_id:str, check_pw:str): #로그인 기능 메소드, 나중에 수정할 것.
        if self.__Users != None:
            # Base가 설정되었다면, 테이블에 세션생성 후 쿼리
            self.__session.begin()
            result= self.__session.execute(
                select(self.__Users.id).where((self.__Users.id== check_id)&(self.__Users.password== check_pw))
            ).scalars()
            
            # for info in result:
            #     print(f"{type(info)}")
            if len(result.all())== 1: # id는 pk이므로, id만 검색하더라도 '한 줄'이 나와야함
               return True            # 따라서, 안전장치로 비밀번호와 같이 검색해도 '한 줄'이면 허가.
            else: 
               return False # '한 줄'이 아니면 어딘가에 문제 있음
            
        else:
            # Base 설정 안되었을 시, 오류 처리(나중에 수정할 것)
            print("error occured")
        self.__session.commit()
        self.__session.close()