from smartphone import Smartpone

phone_1 = Smartpone("Samsung", "Galaxy S 21 FE", "89282623429")
phone_2 = Smartpone("IPhone", "11", "89282623428")
phone_3 = Smartpone("Huawei", "14", "89282623427")
phone_4 = Smartpone("Xiaomi", "999", "89282623426")
phone_5 = Smartpone("Keneksi", "Crystal", "89282623425")

catalog = [phone_1, phone_2, phone_3, phone_4, phone_5]

for x in range (len(catalog)):
    catalog[x].getInfo()