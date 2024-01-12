from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from fastapi import HTTPException

username="root"
password="password"
database="web_db"
host="db"

db_url=f'mysql://{username}:{password}@{host}/{database}?charset=utf8mb4'

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except HTTPException as e:
        raise e
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(503, detail="データベースが混み合っています：　" + e)
    except Exception as e:
        raise e
    finally:
        db.close()