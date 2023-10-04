def how_much_money(money, years):
    for x in range(1, years):
        money = money + money/10
    return int(money)


cost = int(input("Пожалуйста, введите сумму, которую хотите внести во вклад:"))
years = int(input("Пожалуйста, введите количество лет, на которые хотите положить деньги:"))

print(how_much_money(cost, years))