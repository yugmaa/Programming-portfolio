'''this is a program that, when run from the command line, reports how many arguments were provided.'''

import sys

def count_arguments():
    num_arguments = len(sys.argv) - 1  # the number of arguments excluding the script name
    print(f"Number of arguments provided: {num_arguments}")

if __name__ == "__main__":
    count_arguments()