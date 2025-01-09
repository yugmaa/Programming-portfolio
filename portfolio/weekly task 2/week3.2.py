"""this program prompts user to input a new password and re enter the password again for verification.
displays password set if both the input matches otherwise displays an error message."""

password= input("enter a password: ")
recheck= input("enter your password again: ")
if password==recheck:  #password verification
    print("Password Set")
else:
    print("Error! try again") #if verification fails