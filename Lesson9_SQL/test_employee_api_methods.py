import pytest
import requests
from db import DBMethods
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
#------------------------------------------------------------------------------------------------------------------------------------
# Test data

valid_employee_data_api = {
            "id": 0,
            "firstName": "Alexandr",
            "lastName": "Byk",
            "middleName": "Olegovich",
            "companyId": 98,
            "email": "email@gmail.com",
            "url": "https://sanya.com",
            "phone": "88005553535",
            "birthdate": "1998-11-15T18:21:37.199Z",
            "isActive": True
        }
company_name = "Компания"
data_for_creating_five_employees_bd = [
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
    for x in data_for_creating_five_employees_bd:
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

def test_get_employee_from_non_existent_company():
    
    company_id = db.create_company(company_name)
    response = api.get_employees_by_company_id(company_id)
    assert response.status_code == 200, "Status code isn't 200"
    assert response.text == '[]', "Not empty body"
    db.delete_company_by_id(company_id)
    


#------------------------------------------------------------------------------------------------------------------------------------
# [post]/employee

def test_create_employee():
    
    company_id = db.create_company(company_name)

    api.create_employee()
    #assert requests.post(base_url + employee_url, headers = {"x-client-token" : f_test_auth}, json = employee_data).status_code == 201




#print(db.create_company("Горох"))
#for x in data_for_creating_five_employees_bd:
#    db.create_employee("141", x)
#list_db = db.get_company_employees("141")
#e = api.get_employees_by_company_id('141')


#for x in range (len(list_db) + 1):
#    assert e.json()[x]["id"] == list_db[x]
#    print(1)







