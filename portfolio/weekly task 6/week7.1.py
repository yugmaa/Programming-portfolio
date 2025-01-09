'''this program tests a function that takes a string as a parameter and returns a sorted list of all the unique letters used in the string.'''

def user_list_sorted(string): #extracts uniques lettes and sorts the list
    extraction= sorted(set(string))
    return extraction 

string= input("enter string: ") #user input
result= user_list_sorted(string)
print(f"the sorted list of all uniques character is {result}") #displays sorted list