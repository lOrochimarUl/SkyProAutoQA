import requests
import allure
from requests import Response

base_url = "https://x-clients-be.onrender.com"
employee_url = "/employee"

class APIMethods:

    #------------------------------------------------------------------------------------------------------------------------------------
    # [get]/employee

    @allure.step("Получить список сотрудников компании с id:{company_id}")
    def get_employees_by_company_id(self, company_id: int) -> Response:
        """
        Посылает GET запрос с адресом https://x-clients-be.onrender.com/employee
        
        :param company_id: id компании, сотрудников которой необходимо получить
        """

        return requests.get(
            base_url + employee_url,
            "company=" + str(company_id)
        )



    #------------------------------------------------------------------------------------------------------------------------------------
    # [post]/employee

    @allure.step("Создать пользователя с указанными данными")
    def create_employee(self, employee_data: dict, f_test_auth) -> Response:
        """
        Посылает POST запрос с адресом https://x-clients-be.onrender.com/employee
        
        :param employee_data: набор данных, для создания сотрудника
        """

        response = requests.post(
            base_url + employee_url,
            headers={"x-client-token" : f_test_auth},
            json=employee_data
        )
        return response



    #------------------------------------------------------------------------------------------------------------------------------------
    # [get]/employee/{id}

    @allure.step("Получить информацию о пользователе с id:{id}")
    def get_employee_by_id(self, id: int) -> Response:
        """
        Посылает GET запрос с адресом https://x-clients-be.onrender.com/employee/(id)
        
        :param id: id сотрудника
        """

        return requests.get(base_url + employee_url + "/" + str(id))
         


    #------------------------------------------------------------------------------------------------------------------------------------
    # [patch]/employee/{id}

    @allure.step("Обновить информацию о пользователе с id:{id}")
    def change_employee_data(self, id: int, data_to_change: dict, f_test_auth):
        """
        Посылает PATCH запрос с адресом https://x-clients-be.onrender.com/employee/(id)
        
        :param id: id сотрудника 

        :param data_to_change: набор данных для изменения данных сотрудника
        """

        return requests.patch(
            base_url + employee_url + "/" + str(id),
            headers = {"x-client-token" : f_test_auth},
            json = data_to_change
        )
