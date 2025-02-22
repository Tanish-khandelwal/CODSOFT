#====PASSWORD GENERATOR====#

import random
import string

print("=== Password Generator ===")
length = int(input("Please enter the length of the password : "))

print("\nChoose The Password Difficulty  ")
print("1. Only letters")
print("2. Letters + numbers")
print("3. Letters + numbers + symbols")
choice = input("Choose from 1, 2, or 3 : ")

chars = string.ascii_letters 
if choice == '2':
    chars += string.digits   
elif choice == '3':
    chars += string.digits + string.punctuation 

password = ''.join(random.choice(chars) for _ in range(length))
print("\nYour new password:", password)