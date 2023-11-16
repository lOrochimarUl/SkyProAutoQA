def fizz_buzz (number):
    if(number % 3 == 0 and number % 5 == 0): 
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")  
    else:
        print(number)

for x in range (20):
    fizz_buzz(x)



        
