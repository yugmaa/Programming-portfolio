'''this program includes a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary'''

def binary(num):  #function to convert the number into binary
    result=bin(num)
    return result

number= int(input("enter a positive number:"))
if number>0:   #to ensure the entry of a positive integer
    binary_num=binary(number)
    print(f"the number in binary is {binary_num}")
else:
    print("enter a valid number")