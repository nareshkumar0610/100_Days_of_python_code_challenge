'''Q: Write a code for Password Generator Project'''

### Write you code below ###

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Step_1: Ask user for inputs
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Method
password = ""

for i in range(0, nr_letters):
    password += random.choice(letters)


for i in range(0, nr_symbols):
    password += random.choice(symbols)


for i in range(0, nr_numbers):
    password += random.choice(numbers)

print(f"Easy method\n{password}")

#Hard Method
password1 = []
for i in range(0, nr_letters):
    random_letter1 = random.randint(0, len(letters)-1)
    randl1 = letters[random_letter1]
    password1 += randl1


for i in range(0, nr_symbols):
    random_sym1 = random.randint(0, len(symbols)-1)
    rands1 = symbols[random_sym1]
    password1 += rands1


for i in range(0, nr_numbers):
    random_num1 = random.randint(0, len(numbers)-1)
    randn1 = numbers[random_num1]
    password1 += randn1

random_password = password1
print(random_password)
random.shuffle(random_password)
print(random_password)

Shuffled_password = ""
for char in random_password:
    Shuffled_password += char

print(Shuffled_password)
