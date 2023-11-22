from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select, delete
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from support_functions import Support 
from sqlalchemy import URL

support = Support()

class Base(DeclarativeBase): pass

class Company(Base):

    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)

class Employee(Base):
    
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    company_id = Column(Integer)
    is_active = Column(Boolean, default=True)


class DBMethods:

    def __init__(self, url):
        self.db = create_engine(url)

    def create_company(self, company_name):

        insert_statement = (insert(Company.__table__).values(name=company_name))
        with self.db.engine.begin() as conn:
            return conn.execute(insert_statement).inserted_primary_key._data[0]

    def create_employee(self, company, employee_data: dict ):

        insert_statement = (insert(Employee.__table__)
                            .values(
                                first_name=employee_data["firstName"],
                                last_name=employee_data["lastName"],
                                phone=employee_data["phone"],
                                company_id = company
                            ))
        with self.db.engine.begin() as conn:
            conn.execute(insert_statement)

    def get_company_employees(self, company):
        
        select_statement = select(Employee).where(Employee.company_id == company)
        with self.db.engine.begin() as conn:
            company_employees = conn.execute(select_statement).fetchall()
            employees_id_list = []
            for x in range (0, len(company_employees)):
                employees_id_list.append(company_employees[x]._data[0])
            return employees_id_list

    def delete_employees_by_company_id(self, company_id):
        
        delete_statement = delete(Employee).where(Employee.company_id == company_id)
        with self.db.engine.begin() as conn:
            conn.execute(delete_statement)

    def delete_company_by_id(self, company_id):

        delete_statement = delete(Company).where(Company.id == company_id)
        with self.db.engine.begin() as conn:
            result = conn.execute(delete_statement)
            print(result)
        

url = URL.create(
    "postgresql",
    username="x_clients_user",
    password="axcmq7V3QLCQwgL39GymqgasJhUlDbH4",
    host="dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com",
    database="x_clients"
    )
#methods = DBMethods(url)
#methods.delete_company_by_id(171)
#methods.delete_employees_by_company_id(98)