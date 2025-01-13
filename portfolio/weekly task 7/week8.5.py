'''implementation of unix spell command'''

import sys
import string

VALID_WORDS = set([
      "orange","apple", "grape", "banana","papaya", "watermelon", "avocado", "mango", "blueberry", "strawberry", "peach", "pineapple"
])

def clean_word(word): #removes punctuation and deals with case sensitivity.
    return word.strip(string.punctuation).lower()

def spell_check(file6):
    try:
        with open(file6, 'r') as file:  #opens file in reading mode
            for line in file:  # Loop through each line in the file
                words = line.split()  # Split the line into words and clean them
                for word in words:
                    clean = clean_word(word)
                    if clean and clean not in VALID_WORDS:
                        print(f"Misspelled word: {word}")
    
    except FileNotFoundError:
        print(f"Error: The file {file6} was not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:  # check if the correct number of arguments are provided
        print("Usage: python week8.5.py")
    else:
        spell_check(sys.argv[1])
