"""conversion of temperature in celcius into fahrenheit and vice versa."""

def celsius_conversion(): 
    temperature= float(input("enter the temperature in fahrenheit:"))
    celsius= 5/9 * (temperature-32) #conversion from fahrenheit to celsius
    return celsius 

def fahrenheit_conversion():
    temperature= float(input("enter the temperature in celsius:"))
    fahrenheit= (temperature*9/5)+32 #conversion from celsius to fahrenheit
    return fahrenheit

celsius_temperature= celsius_conversion()
fahrenheit_temperature= fahrenheit_conversion()
print(f"the temperature entered in celsius is equal to {fahrenheit_temperature} fahrenheit")
print(f"the temperature entered in fahrenheight is equal to {celsius_temperature} celsius.")