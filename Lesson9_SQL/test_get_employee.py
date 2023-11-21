import pytest
import requests


#def test_get_employees_by_id():
    
    # 1) создать компанию через бд

    # 2) бахнуть в компанию работников

    # 3) считать по БД работников компании

    # 4) считать по api работников компании

    # 5) удалить компанию

























base_url = "https://x-clients-be.onrender.com"
employee_url = "/employee"
employee_id = "74"
non_existinct_employee_id = "999"


#------------------------------------------------------------------------------------------------------------------------------------
# [post]/auth/login
@pytest.fixture()
def f_test_auth():

    credentials = {
        "username": "bloom",
        "password": "fire-fairy"
        }
    
    response = requests.post(base_url + "/auth/login", json=credentials)
    assert response.status_code == 201
    print("Токен получен: " + response.json()["userToken"])

#------------------------------------------------------------------------------------------------------------------------------------
# [get]/employee

@pytest.mark.l8
def test_company_without_employees():
    assert requests.get(base_url + employee_url, "company=95").text == '[]'

@pytest.mark.l8
def test_get_employee():
    response = requests.get(base_url + employee_url, "company=98")
    print(response.text)
    assert response.status_code == 200

@pytest.mark.l8
def test_get_employee_without_company_id():
    assert requests.get(base_url + employee_url).status_code == 500
 
@pytest.mark.l8
def test_get_employee_from_non_existent_company():
    assert requests.get(base_url + employee_url, "0").status_code == 500


#------------------------------------------------------------------------------------------------------------------------------------
# [post]/employee

valid_employee_data = {
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

@pytest.mark.l8
@pytest.mark.parametrize("employee_data", [valid_employee_data])
def test_create_employee(employee_data: dict, f_test_auth):
    assert requests.post(base_url + employee_url, headers = {"x-client-token" : f_test_auth}, json = employee_data).status_code == 201

@pytest.mark.l8
def test_create_employee_without_body(f_test_auth):
        
    employee_data = {}
    
    response = requests.post(base_url + employee_url, headers = {"x-client-token" : f_test_auth}, json = employee_data)
    print(response.text)
    assert response.status_code == 500

@pytest.mark.l8                                                                   #---------------------------------------------------------
@pytest.mark.parametrize("employee_data", employee_data_without_required_fields)  # Т.к. в Свагере информации нет предположим, что все поля 
def test_unfilling_required_employee_fields(employee_data, f_test_auth):          # обязательны и отсутсвие хотя бы одного вызовет 500ку
    response = requests.post(base_url + employee_url, headers = {"x-client-token" : f_test_auth}, json = employee_data)
    assert response.status_code == 500


#------------------------------------------------------------------------------------------------------------------------------------
# [get]/employee/{id}

@pytest.mark.l8
@pytest.mark.parametrize("id", [non_existinct_employee_id])
def test_get_non_existinct_employee_by_id(id):
    response = requests.get(base_url + employee_url + "/" + str(id))
    assert response.status_code == 200
    assert response.text == ""

@pytest.mark.l8
@pytest.mark.parametrize("id", [employee_id])
def test_get_employee_by_id(id):
    response = requests.get(base_url + employee_url + "/" + str(id))
    print(response.text)
    assert response.status_code == 200
    assert response.text != ""

@pytest.mark.l8
def test_get_employee_without_specifying_id():
    assert requests.get(base_url + employee_url + "/").status_code == 500


#------------------------------------------------------------------------------------------------------------------------------------
# [patch]/employee/{id}

id_to_change_data = employee_id
valid_employee_data_to_change  = {
        "lastName": "new last name",
        "email": "new@email.com",
        "url": "new url",
        "phone": "new phone",
        "isActive": False
}
employee_data_to_change_bad_email = {
        "lastName": "new last name",
        "email": "new email",
        "url": "new url",
        "phone": "new phone",
        "isActive": False
}
employee_data_to_change_separatly = [
    (id_to_change_data, "lastName", "new_l_name"),
    (id_to_change_data, "email", "new@email.com"),
    (id_to_change_data, "url", "new url"),
    (id_to_change_data, "phone", "8800553536"),
    (id_to_change_data, "isActive", False)]

@pytest.mark.l8
@pytest.mark.parametrize("id, data_to_change", [(employee_id, valid_employee_data_to_change)])
def test_change_employee_data(id: int, data_to_change: dict, f_test_auth):
  
    response = requests.patch(base_url + employee_url + "/" + str(id), headers = {"x-client-token" : f_test_auth}, json = data_to_change)
    
    assert response.status_code == 201
    assert response.json()["lastName"] == data_to_change["lastName"]
    assert response.json()["email"] ==  data_to_change["email"]
    assert response.json()["url"] == data_to_change["url"]
    assert response.json()["phone"] == data_to_change["phone"]
    assert response.json()["isActive"] == data_to_change["IsActive"]

@pytest.mark.l8
@pytest.mark.parametrize("id, data_to_change", [(employee_id, employee_data_to_change_bad_email)])
def test_change_employee_data_with_bad_email(id: int, data_to_change: dict, f_test_auth):

    response = requests.patch(base_url + employee_url + "/" + str(id), headers = {"x-client-token" : f_test_auth}, json = data_to_change)

    print(response.text)
    
    assert response.status_code == 400
    assert response.json()["message"] == ["email must be an email"]

@pytest.mark.l8
@pytest.mark.parametrize("id, data_to_change", [(non_existinct_employee_id, valid_employee_data_to_change)])
def test_change_non_existinct_employee_data(id: int, data_to_change: dict, f_test_auth):

    response = requests.patch(
        base_url + employee_url + "/" + str(id), headers = {"x-client-token" : f_test_auth}, json = data_to_change
    ).status_code

    assert response == 404

@pytest.mark.l8
@pytest.mark.parametrize("id, key, value", employee_data_to_change_separatly)
def test_change_employee_data_fields_separatly(id: int, key: str, value, f_test_auth):

    request_body = {
        key : value
    }
    response =  requests.patch(
        base_url + employee_url + "/" + str(id), headers = {"x-client-token" : f_test_auth}, json = request_body
    )
    assert response.status_code == 200
    assert str(response.json()[key]) == str(value)





