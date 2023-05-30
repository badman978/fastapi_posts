from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings



DB_PORT = settings.DB_PORT


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOSTNAME}:{DB_PORT}/{settings.DB_NAME}"



engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





#while True:

   # try:
    #    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='d3spicabl3', cursor_factory=RealDictCursor)
     #   conn
      #  cursor= conn.cursor()
     #   print('Database connection was successfull')
       # break

    #except Exception as error:
     #   print('connecting to database failed')
      #  print("The error :", error)
       # time.sleep(3)
