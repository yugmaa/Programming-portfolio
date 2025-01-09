"""this program allows the user to enter a number and generate its times table as an output."""

number= int(input("enter a number. note:the number should be between 0 and 12 inclusive.")) #user input
if number>=0 and number<=12:
    for i in range(0,13):
        product= number*i
        print(f"{number} * {i} = {product}") #times multiplication of the given number
        i=i+1
