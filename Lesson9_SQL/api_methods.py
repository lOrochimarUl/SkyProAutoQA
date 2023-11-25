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

    def get_employee_by_id(self, id):
        return requests.get(base_url + employee_url + "/" + str(id))
         


    #------------------------------------------------------------------------------------------------------------------------------------
    # [patch]/employee/{id}

    def change_employee_data(self, id, data_to_change: dict, f_test_auth):
        return requests.patch(base_url + employee_url + "/" + str(id), headers = {"x-client-token" : f_test_auth}, json = data_to_change)
