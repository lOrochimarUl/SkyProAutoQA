import allure
import datetime

list_db_api_keys = [
        ["first_name","firstName"],
        ["last_name", "lastName"],
        ["middle_name", "middleName"],
        ["company_id", "companyId"],
        ["avatar_url", "url"],
        ["is_active", "isActive"]
    ]


class Support:
    """Класс со вспомогательными функциями"""
   
    @allure.step("Распарсить дату рождения")
    def parse_date_from_api_body(self, date: str) -> datetime:
        """
        Парсит дату из тела ответа
        
        :param date: дата рождения из тела ответа api-запроса
        """

        return datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))

    @allure.step("Конвертирвать тело ответа api-запроса для сравнения с данными из БД")
    def change_api_data_to_db_view(self, data_to_change: dict) -> dict:
        """
        Конвертирует тело ответа api-запроса в БД-шный вид
        
        :param data_to_change: данные тела ответа api-запроса
        """

        for x in list_db_api_keys:
            try:
                data_to_change[x[0]] = data_to_change[x[1]]
                del data_to_change[x[1]]
            except KeyError:
                continue 

        return data_to_change
