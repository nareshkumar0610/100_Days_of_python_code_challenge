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

#Step_3: providing conditions for the BMI
if BMI < 18.5:
    print(f"Your BMI is {BMI} and you're under 'Underweight Category'.")

elif BMI > 18.5 and BMI < 24.9:
    print(f"Your BMI is {BMI} and you're under 'Normal Category'.")

elif BMI > 25 and BMI < 29.9:
    print(f"Your BMI is {BMI} and you're under 'Overweight Category'.")

elif BMI > 30 and BMI < 34.9:
    print(f"Your BMI is {BMI} and you're under 'Obese Category'.")

else:
    print(f"Your BMI is {BMI} and you're under 'Extremely Obese Category'.")

print("-------------------------- End --------------------------")
#-------------------------- Code Ends here --------------------------