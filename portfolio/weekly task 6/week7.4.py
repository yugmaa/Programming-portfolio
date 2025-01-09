'''this program processes a string representing a message and reports the six most common letters, along with the number of times they appear.'''

from collections import Counter

def frequency(message):  # Converts the message to lowercase to ignore case sentivity
    message = message.lower()
    message_filtered = [char for char in message if char.isalpha()]  # Filter out non-alphabetic characters
    letter_counts = Counter(message_filtered)  # Counts the frequency of each letter
    common_ones= letter_counts.most_common(6)  # Get the six most common letters and their counts
    print("The six most common letters and their frequencies are:")
    for letter, count in common_ones:
        print(f"{letter}: {count}")

message = input("enter your message: ")  #user input
frequency(message)