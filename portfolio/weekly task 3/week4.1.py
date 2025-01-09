"""program returns true if the user input falls within the range 0-100."""

def test(number):  #function to test if the number falls within the range
    if number in range(0,101):
        return True
    else:
        return False

number= int(input("enter a number:")) #user input
output= test(number)
if output==True:
    print("true")
else:
    print("false")