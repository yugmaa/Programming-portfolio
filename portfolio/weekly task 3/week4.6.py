"""conversion of temperature in celsius into fahrenheit"""

def fahrenheit_conversion():
    temperature= input("enter the temperature in celsius, example- 48C:")
    celsius= float(temperature[:-1]) #strips the last character i.e. C 
    fahrenheit= (celsius*9/5)+32 #conversion from celsius to fahrenheit
    return fahrenheit

fahrenheit_temperature= fahrenheit_conversion()
print(f"the temperature entered in celsius is equal to {fahrenheit_temperature}F.")