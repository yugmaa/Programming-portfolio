'''this program includes the implementation of Unix nl command'''

import sys

def nl_command(file1):  # prints the line numbers for the contents of the file
    try:
        with open(file1, 'r') as file:  #open the file in read mode ('r')
            for line_number, line in enumerate(file, start=1):  #iterates over the lines in the file
                print(f"{line_number}\t{line}", end='')
    except FileNotFoundError:
        print(f"Error: The file {file1} was not found.")  #if the file is not found, display an error message

if __name__ == "__main__":
    if len(sys.argv) < 2:  #check if the user has provided a filename as a command-line argument
        print("Usage: python week8.1.py") #if no filename is provided (print usage information)
    else:
        nl_command(sys.argv[1]) #function call 