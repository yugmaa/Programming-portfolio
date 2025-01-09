"""program that reads temperature from the user and displays the maximum, minimum, and mean of the values.The input
terminates when the user just pressed "Enter" at the prompt rather than entering a value."""

import statistics

def temperature_input():
    temperature=[]
    while True:
        user_input = input(f"Enter temperature in celsius (example: 20C): ")
        if user_input=="":
            break
        temperature.append(celsius_to_fahrenhiet(user_input))
    return temperature

def celsius_to_fahrenhiet(temp):
    celsius=float(temp[:-1]) #ommits the last character from the string temp and converts the data type into float
    fahrenhiet=(celsius*9/5)+32 #converts censius to fahrenhiet
    return fahrenhiet

def maximum(read_temperature): #function to detect maximum temperature
    maximum_temperature= max(read_temperature)
    return maximum_temperature

def minimum(read_temperature): #function to detetct minimum temperature
    minimum_temperature= min(read_temperature)
    return minimum_temperature

def mean(read_temperature): #function to calculate mean
    mean_value= statistics.mean(read_temperature)
    return mean_value

read_temperature=temperature_input()
maximum_value= maximum(read_temperature)
minimum_value= minimum(read_temperature)
mean_output= mean(read_temperature)
print(f"the maximum temperature is {maximum_value}F.")
print(f"the minimum temperature is {minimum_value}F.")
print(f"the mean value is {mean_output}.")

