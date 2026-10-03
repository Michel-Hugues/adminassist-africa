from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

connect_args = {"check_same_thread": False}
engine =  create_engine(SQLALCHEMY_DATABASE_URL,connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base = declarative_base()


# Open a session, "lends" it to the road that needs it,
# and then automatically closes it afterward, whether the request succeeded or failed.
def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()
