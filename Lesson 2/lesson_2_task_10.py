def how_much_money(money, years):
    for x in range(1, years):
        money = money + money/10
    return int(money)


print(how_much_money(1500, 7))