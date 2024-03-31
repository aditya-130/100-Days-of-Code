import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_of_letters= int(input("How many letters would you like in your password?\n")) 
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))
pw_characters = []
for i in range (0,number_of_letters):
    pw_characters.append(random.choice(letters))
for i in range (0,number_of_symbols):
    pw_characters.append(random.choice(symbols))
for i in range (0,number_of_numbers):
    pw_characters.append(random.choice(numbers))
random.shuffle(pw_characters)
password = ''.join(pw_characters)
print(f"your password is {password}")