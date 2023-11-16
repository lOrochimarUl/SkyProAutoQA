from address import Address
from mailing import Mailing



address_1 = Address(369961, "Olkhovatka", "Novatorov", "39","13")
address_2 = Address(123456, "Olkhovatka", "Centralnaya", "40","1")
mail = Mailing(address_1, address_2, 500, 88005553535)

mail.getInfo()
