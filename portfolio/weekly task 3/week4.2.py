"""this program counts the number of uppercase and lowercase letters in a single string."""

def letter_count(string_input):
    uppercase=0
    lowercase=0
    for char in string_input: #iterates through each character to test either uppercase or lowercase
        if char.isupper(): #built-in function to detect uppercase letters
            uppercase= uppercase+1
        else:
            if char.islower():  #built-in function to detect lowercase letters
                lowercase=lowercase+1
    return uppercase,lowercase

string_input=str(input("enter a string:")) #user input
uppercase_count,lowercase_count= letter_count(string_input)
print(f"the number of uppercase letters are {uppercase_count}")
print(f"the number of lowercase letters are {lowercase_count}")
