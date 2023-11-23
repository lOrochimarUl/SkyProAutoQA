import datetime

class Support:
        
    def clear_id(id: str):
        f = filter(str.isdecimal, id)
        s1 = "".join(f)
        return s1
                
    def parse_date_from_api_body(self, date):
        return datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))

    def change_api_data_to_db_view(self, data_to_change: dict):
       
        result_data = {
            "id": 0,
            "first_name": "fname",
            "last_name": "lanme",
            "middle_name": "mname",
            "company_id": 0,
            "email": "1@d.com",
            "avatar_url": "sallam",
            "phone": "8800",
            "birthdate": datetime.date(2000, 1, 1),
            "is_active": True
        }
        result_data["id"] = data_to_change["id"]
        result_data["first_name"] = data_to_change["firstName"]
        result_data["last_name"] = data_to_change["lastName"]
        result_data["middle_name"] = data_to_change["middleName"]
        result_data["company_id"] = data_to_change["companyId"]
        result_data["email"] = data_to_change["email"]
        result_data["avatar_url"] = data_to_change["url"]
        result_data["phone"] = data_to_change["phone"]
        result_data["birthdate"] = data_to_change["birthdate"]
        result_data["is_active"] = data_to_change["isActive"]

        return result_data

#support = Support

#s1 = [1,2,3]
#s2 = [1,2,3]

#result = set(s1).difference(set(s2))
#print(result)