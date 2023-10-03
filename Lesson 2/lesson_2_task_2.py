def is_year_leap (year):
    if(year % 4 == 0):
        return True
    else:
       return False
    
year = 2020
year_leap = is_year_leap(year)   
print("Year ", year, ": ", year_leap)
