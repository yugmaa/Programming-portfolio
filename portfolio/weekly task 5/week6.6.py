'''this program decodes an encrypted message'''

def decryption(encrypted_message, interval_present):
    decrypted_message = [] #empty string 
    for i in range(interval_present - 1, len(encrypted_message), interval_present): # loop through the encrypted message, picking every `interval`-th character
        decrypted_message.append(encrypted_message[i])
    return ''.join(decrypted_message)# Join the list into a string and return the decrypted message

encrypted_message = input("enter your encryoted message here: ")   #user input
interval_present = int(input("Enter the interval used for encryption (between 2 and 20): "))
decrypted_message = decryption(encrypted_message, interval_present)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)  #message after decrytion displayed