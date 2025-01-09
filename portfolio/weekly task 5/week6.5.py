'''In this program, random interval between 2 and 20 is chosen. The message is then encrypted by inserting random letters from the alphabet (a to z).
As the output of the program the encrypted message is returned, along with the interval used.'''

import random
import string

def final_encryption(message):  # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    encrypted_message = []   #empty string
    count = 0 # Count how many characters we have inserted so far
    for char in message:
        if count == interval: # Insert random characters until we reach the interval
            encrypted_message.append(char)
            count = 0
        else:
            encrypted_message.append(random.choice(string.ascii_lowercase))
            count += 1
    return ''.join(encrypted_message), interval

message = input("enter your message here: ")
final_encrypted_message, intervals = final_encryption(message)
print("Original message:", message)
print("Encrypted message:", final_encrypted_message)
print("Interval used:", intervals)