"""this program allows the user to enter a number and generate its times table as an output.
if the input number is negative the table is printed backwards"""

number= int(input("enter a number"))
if number>0:
    for i in range(0,13): #for positive number
        product= number*i
        print(f"{number} * {i} = {product}") #times multiplication of the given number
        i=i+1
else:
    for i in range (-12,1): #for negative number
        product= number*i
        print(f"{number} * {i} = {product}") #times multiplication of the given number
        i=i+1
