"""this program takes a string parameter and returns it with the last character removed."""

def character_removal(string_input):
    result= string_input[:-1] #removing the last character
    return result

string_input= str(input("enter a string:"))
output= character_removal(string_input)
if len(string_input)<=1: #string with 1 or less character remains unchanged
    print(f"your result is {string_input}")
else:
    print(f"your result is {output}") #result after the removal