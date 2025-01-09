"""this program allows user to input temperature in celsius and displays the corresponding temperature in fahrenheit as a result"""

temperature= float(input("Enter a temperature in Celsius: "))
fahrenheit= float((temperature*9/5)+32)  #temperature conversion from Celsius to Fahrenheit
print(f"{temperature}C is equivalent to {fahrenheit}F.")