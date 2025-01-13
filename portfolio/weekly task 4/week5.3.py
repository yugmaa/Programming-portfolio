'''this a program that takes a bunch of command-line arguments, and then prints out the shortest.'''

import sys

def shortest_argument():
    args = sys.argv[1:]  # get the command-line arguments excluding the script name
    if not args:  # check if there are any arguments provided
        print("No arguments provided.")
        return 
    sorted_args = sorted(args, key=len)  # Sort the arguments by their length
    print(f"The shortest argument is: {sorted_args[0]}")  # the first one in the sorted list will be the shortest argument

if __name__ == "__main__":
    shortest_argument()