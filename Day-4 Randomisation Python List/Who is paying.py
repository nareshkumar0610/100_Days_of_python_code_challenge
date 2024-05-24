'''Q: Write a code using random generator for who is going to pay the bill?'''

###Write your code below ###

#Step_1: Ask input from user
Enter_names = input("GIve me the name with comma separated values? ")

names = Enter_names.split(", ")

#Step_2:import radom module
import random

len_list = len(names)

random_names = random.randint(0, len_list)

payer_name = names[random_names]

print(f"{payer_name} is going to pay today!")
