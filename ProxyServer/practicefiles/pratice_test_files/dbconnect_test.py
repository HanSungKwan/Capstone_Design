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
    pass
    #result = conn.execute(text("SELECT * FROM users"))
    #print(result.all())
    
###############################################################