'''this program that manages a list of countries and their capital cities.'''

def country_capitals():  # Dictionary to store countries and their capital cities
    countries_and_capitals = {
        "Nepal": "Kathmandu",
        "India": "New Delhi",
        "South Korea": "Seoul",
        "USA": "Washington DC",
        "Japan": "Tokyo",
    }

    while True:
        country = input("Enter the name of a country (or type 'quit' to exit): ").strip()  # Prompt the user for the country name
        if country.lower() == 'quit':
            print("you will not exit the system.")
            break
        if country in countries_and_capitals:  # If the country is in the dictionary, show the capital
            print(f"The capital city of {country} is {countries_and_capitals[country]}.")
        else:
            capital = input(f"I don't know the capital city of {country}. Please enter it: ").strip()  # If the country is not in the dictionary, ask for the capital
            countries_and_capitals[country] = capital
            print(f"Thank you! {capital} has been added as the capital of {country}.")

country_capitals()