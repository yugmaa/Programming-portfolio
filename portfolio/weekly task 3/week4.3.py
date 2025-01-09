"""this program asks user to input their name and displays the first letter in uppercase and rest in lowercase."""

def corrected_name(name):
    final_name=name.capitalize() #built in function that converts first letter into uppercase and rest into lowercase.
    return final_name

name= str(input("enter your name: ")) #user input
output= corrected_name(name)
print(f"Your name after formatting is {output}.")

