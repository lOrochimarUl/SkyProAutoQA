import pytest
import requests
from support_functions import Support
from db_methods import DBMethods
from api_methods import APIMethods
from sqlalchemy import URL

url = URL.create(
    "postgresql",
    username="x_clients_user",
    password="axcmq7V3QLCQwgL39GymqgasJhUlDbH4",
    host="dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com",
    database="x_clients"
    )
db = DBMethods(url)
api = APIMethods()
support = Support()
#------------------------------------------------------------------------------------------------------------------------------------
# Test data

empl_data_for_api = {
            "id": 0,
            "firstName": "Michael",
            "lastName": "Byk",
            "middleName": "Michaelovich",
            "companyId": 0,
            "email": "email@gmail.com",
            "url": "https://misha.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True
        }
company_name = "Тест компания"
data_for_create_five_empls_db = [
    {
        "firstName" : "Alex",
        "lastName" : "1",
        "phone" : "88005553531"
    },{
        "firstName" : "Bary",
        "lastName" : "2",
        "phone" : "88005553532"
    },{
        "firstName" : "Citni",
        "lastName" : "3",
        "phone" : "88005553533"
    },{
        "firstName" : "Denis",
        "lastName" : "4",
        "phone" : "88005553534"
    },{
        "firstName" : "Ena",
        "lastName" : "5",
        "phone" : "88005553535"    
    }
]
employee_data_without_required_fields = [
        {
            #"id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            #"firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            #"lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            #"middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            #"companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            #"email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            #"url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            #"phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            #"birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True,
        },
        {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            #"isActive": "True",
        }]



#------------------------------------------------------------------------------------------------------------------------------------
# [get]/employee

def test_get_employees_by_company_id():

    # Подготовка
    company_id = db.create_company(company_name)
    for x in data_for_create_five_empls_db:
        db.create_employee(company_id, x)

    # Считывание
    employees_id_list_from_bd = db.get_company_employees(company_id)
    employee_list_from_api = api.get_employees_by_company_id(company_id)
    
    # Чистка
    db.delete_employees_by_company_id(company_id)
    db.delete_company_by_id(company_id)

    # Проверки
    assert employee_list_from_api.status_code == 200, "Status code isn't 200"
    try:
        for x in range (len(employees_id_list_from_bd)):
            assert employee_list_from_api.json()[x]["id"] == employees_id_list_from_bd[x]
    except IndexError:
        assert False, "Quantity of id from DB and API aren't equal"

def test_get_employee_without_company_id():
    assert api.get_employees_by_company_id(company_id=None).status_code == 500, "Status code isn't 500"



#------------------------------------------------------------------------------------------------------------------------------------
# [post]/employee

@pytest.mark.this
def test_create_employee(f_test_auth):
    
    # Подготовка
    global empl_data_for_api
    company_id = db.create_company(company_name)
    empl_data_for_api["companyId"] = company_id

    # Создание сотрудника
    employee_response = api.create_employee(empl_data_for_api, f_test_auth)
    
    #Подготовка к проверке
    employee_from_db = db.get_employee_by_id(employee_response.json()["id"])
    result_from_db_as_dict = employee_from_db.mappings().all()

    empl_data_for_api["birthdate"] = support.parse_date_from_api_body(empl_data_for_api["birthdate"])
    empl_data_for_api["id"] = employee_response.json()["id"]
    empl_data_for_api = support.change_api_data_to_db_view(empl_data_for_api)

    result = set(result_from_db_as_dict[0].items()).difference(set(empl_data_for_api.items()))

    # Чистка
    db.delete_employees_by_company_id(company_id)
    db.delete_company_by_id(company_id)

    # Проверки
    assert employee_response.status_code == 201 
    try:
        assert result == {}
    except AssertionError:
        print("Следующие поля отличаются от данных тела запроса")
        for x in result:
            print(x)
        assert False, "Данные из тела запроса и БД отличаются"



#------------------------------------------------------------------------------------------------------------------------------------
# [get]/employee/{id}




