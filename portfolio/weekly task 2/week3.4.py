"""this program prompts user to enter a password of length 8-12 characters long.
the password has to be re entered and if matches the criteria and the previous input the password is set otherwise an error message is displayed.
the entered password should not match with the given list as well"""

password=input("enter a password. note the password must be 8-12 characters long:")
if len(password)>=8 and len(password)<=12:  #checks if the password is 8-12 characters long
    recheck=input("enter your password again: ")
    if password==recheck:  #password verification
        BAD_PASSWORDS= ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
        if recheck in BAD_PASSWORDS: #if the entered password matches with one of the password on the list
                print("this password cannot be set. try entering a new one.")
        else:
                print("Password Set")  #if the password entered is unique and not a common one
    else:
        print("Error! try again.")  #if verification fails
else:
    print("enter a valid password following the given criteria.") #if the passwork is not 8-12 characters long.

    