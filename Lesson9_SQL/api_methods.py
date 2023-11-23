import pytest
import requests


base_url = "https://x-clients-be.onrender.com"
employee_url = "/employee"
employee_id = "74"
non_existinct_employee_id = "999"

class APIMethods:

    #------------------------------------------------------------------------------------------------------------------------------------
    # [get]/employee

    def get_employees_by_company_id(self, company_id):
        return requests.get(
            base_url + employee_url,
            "company=" + str(company_id)
        )



    #------------------------------------------------------------------------------------------------------------------------------------
    # [post]/employee

    def create_employee(self, employee_data: dict, f_test_auth):
        header = {"x-client-token" : f_test_auth}
        response = requests.post(
            base_url + employee_url,
            headers=header,
            json = employee_data
        )
        return response



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





