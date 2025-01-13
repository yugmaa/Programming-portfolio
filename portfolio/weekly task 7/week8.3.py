'''implementation of unix grep command'''

import sys

def grep(pattern, file4):
    try:
        with open(file4, 'r') as file:  # open the file in reading mode
            for line in file:  # check if the pattern is in the line
                if pattern in line:
                    print(line, end='')  # print the line that contains the pattern
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:  # check if the correct number of arguments are provided
        print("Usage: python week8.3.py")
    else:
        grep(sys.argv[1], sys.argv[2]) # run the grep function with the given pattern and filename