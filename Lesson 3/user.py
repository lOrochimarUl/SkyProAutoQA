class User:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def getFirstName(self):
        print("The first name is:", self.first_name)
        return 1
    
    def getLastName(self):
        print("The last name is:", self.last_name)
    
    def getFullName(self):
        print("The full name is:", self.first_name, self.last_name)