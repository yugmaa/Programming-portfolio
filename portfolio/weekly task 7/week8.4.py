''' implementation unix wc command '''

import sys

def wc(file5):
    try:
        with open(file5, 'r') as file:  #open file in reading mode
            lines = 0
            characters = 0
            for line in file:  # loop through each line in the file
                lines += 1  # count the line
                characters += len(line)  # count the characters in the line
            print(f"Lines: {lines}")
            print(f"Characters: {characters}")

    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:  # check if the correct number of arguments are provided
        print("Usage: python week8.4.py")
    else:
        wc(sys.argv[1])