def month_to_season (month_number):
    if(month_number > 0 and month_number < 4): 
        print("Зима")
    elif(3 < month_number < 7): 
        print("Весна")
    elif(month_number > 6 and month_number < 10): 
        print("Лето")
    elif(month_number > 9 and month_number < 13): 
        print("Осень")
    elif(month_number < 1  or month_number > 12):
        print("Число за рамками нумерации месяцев") 


for x in range (14):
    month_to_season(x)



        
