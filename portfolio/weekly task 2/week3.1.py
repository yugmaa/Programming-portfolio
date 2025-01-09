"""this program prompts user to input their name. if name prints greeting message with user input else prints hello stranger"""

name= input("enter your name: ")
if name== "":  #if the user does not enter data 
    print("Hello,Stranger!")
else: #if the user gives an input 
    print(f"Hello, {name}. Good to meet you!")