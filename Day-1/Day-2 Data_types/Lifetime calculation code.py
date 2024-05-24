'''Q: Write a code to find the remaining life time in days, 
months, years form the user age'''

### Write your code below ###

# Step_1: Ask input from the user regarding their age
age = int(input("Enter your age in years: "))

# Step_2: Calculate their age in days months and years
days = 365 * (90 - age)
months = 12 * (90 - age)
years = 1 * (90 - age)
hours = (24 * 365) *(90 - age)
minutes = (hours * 60) * (90 - age)

print(f'''You've {days} days, {months} months, {years} years, {hours} hours and {minutes} minutes remaining in your lifetime''')

print("-------------------------- End --------------------------")
#-------------------------- Code Ends here --------------------------