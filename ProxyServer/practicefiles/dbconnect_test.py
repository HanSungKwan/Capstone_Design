#사용할 코드#############################################

from sqlalchemy import SQLAlchemy, create_engine
from sqlalchemy import text, select
from sqlalchemy.orm import Session

engine = create_engine(
    "mysql+mysqldb://root:1234@localhost:3306/UserDB",
    echo=True)

session = Session(engine)
stmt = text("SELECT * FROM users WHERE id = :id AND password = :pw ;")
# :id와 :pw 자유롭게 입력 받을 수 있도록 함수화.

with engine.connect() as conn:
    #result = conn.execute(text("SELECT * FROM users"))
    #print(result.all())
    
###############################################################
    # db sql commit
    # conn.execute(
    #    text("INSERT INTO users("id", "password") VALUES ("testuser2", "1234"))
    # )
    # conn.commit()
    
from sqlalchemy import Metadata
from sqlalchemy import Table, Column, Integer, String
# "Models, DBSchemas" 둘 모두 metadata를 모아놓은 것.

metadata_obj = MetaData()

user_table = Table( #MetaData Container
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

user_table.c.name # talbe.c: attribute accessing via an associative array
user_table.c.keys()

from sqlalchemy import ForeignKey
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False), # nullable= False: NOT NULL
)

metadata_obj.create_all(engine) # 테이블 user_account, address_table 전부 쿼리화 및 실행
# metadata_obj.drop_all(engine)

from sqlalchemy.orm import registry # == from sqlalchemy import Metadata
mapper_registry = registry()
mapper_registry.metadata # == metadata_obj = MetaData()
Base = mapper_registry.generate_base() #we will now declare Tables indirectly
# 위의 Base 객체는 우리가 선언하는 ORM 매핑 클래스의 기본 클래스 역할을 할 Python 클래스입니다.

# 위 과정 한번에 해버리기
# from sqlalchemy.orm import declarative_base
# Base = declarative_base()

# 테이블 선언용 베이스를 선언해줬으니, 테이블을 선언해줄 것.
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__= "user_account"
    
    id= Column(Integer, primary_key= True)
    name= Column(String(30))
    fullname= Column(String)
    
    addresses= relationship("Address", back_populate= "user")
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__= "address"
    
    id= Column(Integer, primary_key= True)
    email_address= Column(String, nullable= False)
    user_id= Column(Integer, ForeignKey("user_account.id"))
    
    user= relationship("User", back_populate= "addresses")
    
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
# We can see mapped class using the .__table__ attribute
User.__table__

# orm mapped classes는 이런 특성을 가진다
# the classes have an automatically generated __init__() method

# orm방식으로 만든 테이블 전체 SQL화 및 Commit
mapper_registry.metadata.create_all(engine)
# 혹은
# Base.metadata.create_all(engine) 사용 가능.

#
# Table reflection 방법
some_table = Table("some_table", metadata_obj, autoload_with=engine)
# 원래는 Column과 조건 객체를 선언해주겠지만,
# 이 방법에서는 autoload_with 를 이용해 생략