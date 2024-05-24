'''Q: Write a code to find the user input is either "odd" or "even"?'''

### Write your code below ###

#Step_1: Ask input from the user as integer
num = int(input("Enter number to find odd or even: "))

#Step_2: add formula to find odd or even using conditional statement
if num % 2 == 0:
    print(f"You enter a number {num} and it is 'EVEN NUMBER'.")
else:
    print(f"You enter a number {num} and it is 'ODD NUMBER'.")

