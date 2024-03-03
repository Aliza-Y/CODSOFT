import random
import string

length = int(input("Enter the desired length for your password: "))

characters = string.ascii_letters
characters += string.digits
characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters) 

print("Here's the password we generated for you: " + password)    
