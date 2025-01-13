'''this is a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address.'''

import sys
import requests

def website_verify(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:  #checks if the website is working i.e. if the status code is 200
            print("Website is working!")
        else:
            print(f"Website returned status code: {response.status_code}")  #working functional website
    except requests.exceptions.RequestException:
        print("Error: Could not reach the website.")  #error message

if __name__ == "__main__":
    if len(sys.argv) != 2:  #checks if only one argument is passed
        print("Usage: python website_verify.py")
    else:
        website_verify(sys.argv[1])  # Pass the URL from the command-line argument to the website_verify function