'''this program tests a function that takes an integer as its parameter and returns the
factors of that integer.'''

def factor(num):  #function to determine the factors
    factors= [i for i in range(1,num+1) if num%i==0]
    return factors
    
number= int(input("enter a number:"))
factors_num= factor(number)
print(f"the factors of the number are {factors_num}")  #displays the factors