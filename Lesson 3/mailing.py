from address import Address

class Mailing:


    cost = 0
    track = "unknown"

    def __init__(self, to_address, from_address, cost, track) -> None:
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
        
    def getInfo(self):
        print("Отправление", self.track, "из", self.from_address.index,",", self.from_address.city, ",", self.from_address.street, ",", self.from_address.house, " - ",
               self.from_address.apartment,"в", self.to_address.index,",", self.to_address.city, ",", self.to_address.street, ",", self.to_address.house, " - ",
               self.to_address.apartment, ". Стоимость", self.cost, "рублей")

