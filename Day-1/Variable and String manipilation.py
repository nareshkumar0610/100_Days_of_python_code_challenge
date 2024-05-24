'''Q: Ask user to update their name and print 
'how many characters are there in the name'?'''

### Write a Code below ###

# #Step_1: Ask user to enter their name
# name = input('Enter your name: ')

# #Step_2: print the output
# print(len(name))


'''Q: Write a program that switches the values 
stored in the variables a and b.'''

### Write a Code below ###

#Step_1: create 2 variables for the user input
# num_1 = int(input("Enter the first number: \n"))
# num_2 = int(input("Enter the second number: \n"))
# print(f"Original_numbers: {num_1}, {num_2}")

# #Step_2/Method_1: swap variables without using 
# #new variable
# num_1 = num_1 + num_2
# num_2 = num_1 - num_2
# num_1 = num_1 - num_2
# print(f"Method_1 - Swapped_numbers: {num_1}, {num_2}")

# #Step_3/Method_2: swap variables using new 
# #variable
# num_3 = num_1
# num_2 = num_3
# num_1 = num_2
# print(f"Method_2 - Swapped_numbers: {num_1}, {num_2}")


'''Q: Indexing and slicing / String Methods'''

### Write a Code below ###

paragraph = '''Chapter 6 in Automate the Boring Stuff covers strings. 
I honestly found this chapter quite fascinating. Thereis so much that
can be done with strings simply by adding a method. They are also 
inherently set up as a list (each character has its own index) which
makes slicing and dicing easy-peasy.'''

#lets convert everyting into upper case:
print(paragraph.upper())

#lets check what is the 50th character in the paragraph
# print(paragraph[39:53])

#lets convert everyting into lower case:
# print(paragraph.lower())





