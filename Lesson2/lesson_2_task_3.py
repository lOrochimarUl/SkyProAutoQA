def calculating_are_of_square (square_side):
    if(square_side % 1 != 0):
        square_side = int(square_side) + 1
    else:
        square_side = int(square_side)
    square_area = square_side*square_side    
    return square_area

print(calculating_are_of_square(5))
print(calculating_are_of_square(6.1))
print(calculating_are_of_square(7.8))


        
