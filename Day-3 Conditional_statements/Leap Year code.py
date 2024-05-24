'''Q: Write a code to find a user input is whether a "Leap Year" or not?'''

### Write your code below ###

#Step_1: Ask input from the user
year = int(input("Enter the year you want to check in the format yyyy: "))

#Step_2 / Method_1: Write a conditional statement to check the "Leap year"
if year % 4 == 0 and year % 100 != 0:
    print(f"Year {year} is a 'Leap Year'")
elif year % 400 == 0:
    print(print(f"Year {year} is a 'Leap Year'"))
else:
    print(print(f"Year {year} is a 'Not a Leap Year'"))

#Step_3 / ethod_2: Write a conditional statement to check the "Leap year"
if (year %4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(print(f"Year {year} is a 'Leap Year'"))
else:
    print(print(f"Year {year} is a 'Not a Leap Year'"))