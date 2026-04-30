from sqlalchemy import create_engine
#create connection to our db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Normally done in env
MYSQL_USER = "root"
MYSQL_PASSWORD = "248624"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "fastapi_db"

DATABASE_URL = F"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

##connection

engine = create_engine(DATABASE_URL)

## Session
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

## Base
Base = declarative_base()