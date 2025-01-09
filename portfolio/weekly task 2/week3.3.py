"""this program prompts user to enter a password of length 8-12 characters long.
the password has to be re entered and if matches the criteria and the previous input the password is set otherwise an error message is displayed"""

password= input("enter a password. note the password must be 8-12 characters long: ")
if len(password)>=8 and len(password)<=12:  #checks if the password is 8-12 characters long
    recheck=input("enter your password again: ")
    if password==recheck:  #password verification
        print("Password Set")
    else:
        print("Error! try again.")  #if verification fails
else:
    print("enter a valid password following the given criteria.")  