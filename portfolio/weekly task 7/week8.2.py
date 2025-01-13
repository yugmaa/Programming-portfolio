'''implementation of Unix diff command'''

import sys

def compare_files(file2, file3):
    try:
        with open(file2, 'r') as f1, open(file3, 'r') as f2:  # Open both files in reading mode
            if f1.read() == f2.read():
                print("The files are the same.")
            else:
                print("The files are different.")
    except FileNotFoundError:
        print("One or both of the files were not found.")

if __name__ == "__main__":
    if len(sys.argv) < 3:  # check if the correct number of arguments are provided
        print("Usage: python week8.2.py")
    else:
        compare_files(sys.argv[1], sys.argv[2])  # Compare the two files passed as arguments