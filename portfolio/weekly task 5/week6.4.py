'''this program includes a function that takes a string containing a message and encrypts it'''
def final_message(text):
    no_space= text.replace(" ","")  #replaces space with no character
    reverse_message= no_space[::-1]  #reverses the string with no space character
    return reverse_message

message= input("enter you message here. ")
result= final_message(message)
print(f"your text with no space and in reversed order is {result}") #encrypted message