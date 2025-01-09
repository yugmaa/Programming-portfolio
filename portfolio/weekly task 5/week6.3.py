'''this program tests a function that determines if a given integer is a prime number.'''

def prime_number(num): #function to test if the number is prime
    factors= [i for i in range(1,num+1) if num%i==0]
    if factors== [1,num]:
        return True
    else:
        return False
    
number= int(input("enter a positive integer:"))
if number>0:  #checks for valid input
    result= prime_number(number)
    print(f"the number is a prime number: {result}") 
else:
    print("enter a valid input")