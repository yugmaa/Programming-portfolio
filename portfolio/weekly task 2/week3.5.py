"""this program prompts user to enter a password of length 8-12 characters long.
the password has to be re entered and if matches the criteria and the previous input the password is set otherwise an error message is displayed.
the password should also not match with any element in the given list. if the entered password fails to match any criteria the user is directed to the start again."""

def first_entry(): #password entry from the user
    password=input("enter a password. note the password must be 8-12 characters long:")
    return password

def character_check(password):   #checks if the password is within the given character range
    if len(password)>=8 and len(password)<=12:
        recheck= input("enter your password again:")
        if recheck==password: #password verification
            return recheck
        else:
            print("password mismatched. enter a new one.")
            return None
    else:
        return None

def list_check(recheck):  
    BAD_PASSWORDS= ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    if recheck in BAD_PASSWORDS: #checks if the entered password matches with one of the password on the list
        print("this password cannot be set. try entering a new one.") 
        return None
    else:
        print("Password Set")  #after all the criteria are satisfied the password is set
        return recheck

while True:
    password= first_entry()
    recheck= character_check(password)
    if recheck==None: #if criteria is not fulfilled the program starts again from the entry
        continue
    output= list_check(recheck) 
    if output is None: #if criteria is not fulfilled the program starts again from the entry
        continue
    if output is not None: #if all the criteria is fulfilled now the while loop terminates and the password is set.
        break





    
    



