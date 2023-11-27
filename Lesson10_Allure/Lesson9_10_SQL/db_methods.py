import allure
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select, delete
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import CursorResult

class Base(DeclarativeBase): pass

class Company(Base):
    """Таблица Company"""

    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)

class Employee(Base):
    """Таблица Employee"""

    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    company_id = Column(Integer)
    email = Column(String)    
    avatar_url = Column(String)
    phone = Column(String)
    birthdate = Column(Date)
    is_active = Column(Boolean, default=True)


class DBMethods:
    """Класс с методами взаимодействияс БД"""

    def __init__(self, url) -> None:
        self.db = create_engine(url)

    @allure.step("Создать компанию с название {company_name}")
    def create_company(self, company_name: str) -> CursorResult:
        """
        Посылает INSERT запрос в БД на создание записи в таблице Company
        
        :param company_name: название создаваемой компании 
        """

        insert_statement = (insert(Company.__table__).values(name=company_name))
        with self.db.engine.begin() as conn:
            return conn.execute(insert_statement).inserted_primary_key._data[0]

    @allure.step("Создать сотрудника в компании с id {company}")
    def create_employee(self, company: int, employee_data: dict ) -> CursorResult:
        """
        Посылает INSERT запрос в БД на создание записи в таблице Employee
        
        :param company: id компании

        :param employee_data: набор данных для создания пользователя 
        """

        insert_statement = (insert(Employee.__table__)
                            .values(
                                first_name=employee_data["firstName"],
                                last_name=employee_data["lastName"],
                                phone=employee_data["phone"],
                                company_id = company
                            ))
        with self.db.engine.begin() as conn:
            return conn.execute(insert_statement)

    @allure.step("Получить список сотрудников компании с id {company}")
    def get_company_employees(self, company: int) -> list:
        """
        Посылает SELECT запрос в БД на получение списка id сотрудников компании
        
        :param company: id компании
        """

        select_statement = select(Employee).where(Employee.company_id == company)
        with self.db.engine.begin() as conn:
            company_employees = conn.execute(select_statement).fetchall()
            employees_id_list = []
            for x in range (0, len(company_employees)):
                employees_id_list.append(company_employees[x]._data[0])
            return employees_id_list

    @allure.step("Получить данные сотрудника с id {id}")
    def get_employee_by_id(self, id: int) -> CursorResult:
        """
        Посылает SELECT запрос в БД на получение сотрудника с указаным id
        
        :param id: id сотрудника
        """
        
        select_statement = select(Employee).where(Employee.id == id)
        with self.db.engine.begin() as conn:
            return conn.execute(select_statement)
            
    @allure.step("Получить данные сотрудника с максимальным id")
    def get_employee_with_max_id(self) -> CursorResult:
        """Посылает SELECT запрос в БД на получение сотрудника с макимальным id"""

        select_statement = select(Employee).where(Employee.id, max())
        with self.db.engine.begin() as conn:
            return conn.execute(select_statement)

    @allure.step("Удалить сотрудников компании с id {company_id}")
    def delete_employees_by_company_id(self, company_id: int) -> None:
        """
        Посылает DELETE запрос в БД на удаление сотрудников компании с указанным id
        
        :param company_id: id компании
        """
        delete_statement = delete(Employee).where(Employee.company_id == company_id)
        with self.db.engine.begin() as conn:
            conn.execute(delete_statement)

    @allure.step("Удалить компанию с id {company_id}")
    def delete_company_by_id(self, company_id) -> None:
        """
        Посылает DELETE запрос в БД на удаление компании с указанным id
        
        :param company_id: id компании
        """

        delete_statement = delete(Company).where(Company.id == company_id)
        with self.db.engine.begin() as conn:
            result = conn.execute(delete_statement)
            print(result)
        
