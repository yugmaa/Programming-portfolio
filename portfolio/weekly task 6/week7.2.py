'''this program tests three functions that each take two words as parameters and returns sorted lists'''

def unique_sorted_letters(input_string):  # Extract unique letters and sort them
    return sorted(set(input_string))

def letters_either_word(word1, word2):  ## Letters that appear in at least one of the two words (Union)
    return sorted(set(word1) | set(word2))

def letters_both_words(word1, word2):  # Letters that appear in both words (Intersection)
    return sorted(set(word1) & set(word2))

def letters_either_but_not_both(word1, word2):  ## Letters that appear in either word but not both (Symmetric Difference)
    return sorted(set(word1) ^ set(word2))

first_word = input("enter first word")  #user input
second_word= input("enter second word")
print("Letters in at least one of the words:", letters_either_word(first_word, second_word))
print("Letters in both words:", letters_both_words(first_word, second_word))
print("Letters in either word but not both:", letters_either_but_not_both(first_word, second_word))