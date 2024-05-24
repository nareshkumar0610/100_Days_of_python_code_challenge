'''Q: Create a BMI Calculator and ask user to enter the
height and weight value?'''

### Write your code below ###

# Step_1: ASk input from the User
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in Kgs: "))

print(f"Your height is {height}m")
print(f"Your wiight is {weight}kg")

# Step_2: Calculate BMI form the user input
#Formula for BMI
# BMI = weight(kg) / height(m**2)

BMI = round(weight / (height * height),2)
print(f"Your BMI is {BMI}")

print("-------------------------- End --------------------------")
#-------------------------- Code Ends here --------------------------