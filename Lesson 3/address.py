class Address:

    index = "unknown"
    city = "unknown"
    street = "unknown"
    house = "unknown"
    apartment = "unknown"

    def __init__(self, index, city, street, house, apartment) -> None:
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
