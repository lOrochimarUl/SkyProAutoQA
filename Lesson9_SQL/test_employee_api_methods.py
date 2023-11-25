import pytest
from support_functions import Support
from db_methods import DBMethods
from api_methods import APIMethods
from sqlalchemy import URL



#------------------------------------------------------------------------------------------------------------------------------------
# Preparing

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

emp_data_for_api = {
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
emp_data_to_change  = {
            "lastName": "new last name",
            "email": "new@email.com",
            "url": "new url",
            "phone": "new phone",
            "isActive": False
    }
emp_data_bad_email = {
    "lastName": "new last name",
    "email": "new email",
    "url": "new url",
    "phone": "new phone",
    "isActive": False
}
list_data_to_change = [
    {"lastName": "new last name"},
    {"email": "new@email.com"},
    {"url": "new url"},
    {"phone": "88005553636"},
    {"isActive": False}
]

#------------------------------------------------------------------------------------------------------------------------------------
# [get]/employee

@pytest.mark.l9
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

@pytest.mark.l9
def test_get_employee_without_company_id():
    assert api.get_employees_by_company_id(company_id=None).status_code == 500, "Status code isn't 500"



#------------------------------------------------------------------------------------------------------------------------------------
# [post]/employee

@pytest.mark.l9
@pytest.mark.parametrize("empl_data_s", [emp_data_for_api])
def test_create_employee(empl_data_s: dict, f_test_auth):
    
    # Подготовка
    empl_data = empl_data_s.copy()
    company_id = db.create_company(company_name)
    empl_data["companyId"] = company_id

    # Создание сотрудника
    employee_response = api.create_employee(empl_data, f_test_auth)
    
    #Подготовка к проверке
    employee_from_db = db.get_employee_by_id(employee_response.json()["id"])
    result_from_db_as_dict = employee_from_db.mappings().all()

    empl_data["birthdate"] = support.parse_date_from_api_body(empl_data["birthdate"])
    empl_data["id"] = employee_response.json()["id"]
    empl_data = support.change_api_data_to_db_view(empl_data)

    result = set(result_from_db_as_dict[0].items()).difference(set(empl_data.items()))

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

@pytest.mark.l9
@pytest.mark.parametrize("emp_data", [emp_data_for_api])
def test_get_employee_by_id(emp_data):

    company_id = db.create_company(company_name)
    emp_data["companyId"] = company_id
    employee_id = db.create_employee(company_id, emp_data).returned_defaults._data[0]

    response = api.get_employee_by_id(employee_id)

    db.delete_employees_by_company_id(company_id)
    db.delete_company_by_id(company_id)

    assert response.status_code == 200

@pytest.mark.l9
@pytest.mark.parametrize("emp_data", [emp_data_for_api])
def test_get_non_existinct_employee_by_id(emp_data):

    company_id = db.create_company(company_name)
    emp_data["companyId"] = company_id
    employee_id = int(db.create_employee(company_id, emp_data).returned_defaults._data[0] + 1)

    response = api.get_employee_by_id(employee_id)

    db.delete_employees_by_company_id(company_id)
    db.delete_company_by_id(company_id)

    assert response.status_code == 200
    assert response.text == ""



#------------------------------------------------------------------------------------------------------------------------------------
# [patch]/employee/{id}

@pytest.mark.l9
@pytest.mark.parametrize("emp_data, data_to_change", [(emp_data_for_api, emp_data_to_change)])
def test_change_employee_data(emp_data: dict, data_to_change: dict, f_test_auth):

    company_id = db.create_company(company_name)
    emp_data["companyId"] = company_id
    employee_id = db.create_employee(company_id, emp_data).returned_defaults._data[0]

    response = api.change_employee_data(employee_id, data_to_change, f_test_auth)
    response_body = response.json()
        
    db.delete_employees_by_company_id(company_id)
    db.delete_company_by_id(company_id)

    assert response.status_code == 200, "Статус код должен быть 201"
    count = 0
    for x in data_to_change.keys():   
        try:
            assert data_to_change[x] == response_body[x], "В теле ответа не найдено обязательное поле"
        except KeyError as e:
            print(e, end=" ")
            print(": поле с данным ключом не найдено")      
            count = count + 1

    assert count == 0, "В теле ответа не найдено " + str(count) + " поля"


@pytest.mark.l9
@pytest.mark.parametrize("emp_data, data_to_change", [(emp_data_for_api, emp_data_bad_email)])
def test_change_employee_data_bad_email(emp_data, data_to_change, f_test_auth):

    company_id = db.create_company(company_name)
    emp_data["companyId"] = company_id
    employee_id = db.create_employee(company_id, emp_data).returned_defaults._data[0]

    response = api.change_employee_data(employee_id, data_to_change, f_test_auth)
        
    db.delete_employees_by_company_id(company_id)
    db.delete_company_by_id(company_id)

    assert response.status_code == 400, "Статус код должен быть 400"
    assert response.json()["message"] == ["email must be an email"]

@pytest.mark.l9
@pytest.mark.parametrize("value_to_change", list_data_to_change)
def test_change_employee_data_fields_separatly(value_to_change, f_test_auth):

    company_id = db.create_company(company_name)
    global emp_data_for_api
    emp_data_for_api["companyId"] = company_id
    employee_id = db.create_employee(company_id, emp_data_for_api).returned_defaults._data[0]
        
    response = api.change_employee_data(employee_id, value_to_change, f_test_auth)
    emp_data = db.get_employee_by_id(employee_id).mappings().all()
    value_to_change = support.change_api_data_to_db_view(value_to_change)

    assert response.status_code == 200

    assert value_to_change.items() <= emp_data[0].items(), "Значения из тела запроса и из БД не совпали: " + str(value_to_change.items())
    print(1)





