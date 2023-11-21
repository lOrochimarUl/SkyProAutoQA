from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase

url = URL.create(
    "postgresql",
    username="x_clients_user",
    password="axcmq7V3QLCQwgL39GymqgasJhUlDbH4",
    host="dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com",
    database="x_clients"
    )

class Base(DeclarativeBase): pass

class Company(Base):

    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)


class DBMethods:

    def __init__(self, url):
        self.db = create_engine(url)

    def create_company(self, company_name):

        insert_stmt = (insert(Company.__table__).values(name=company_name))
        with self.db.engine.begin() as conn:
            conn.execute(insert_stmt) 

    

methods = DBMethods(url)

#methods.create_company("Царь горох")

