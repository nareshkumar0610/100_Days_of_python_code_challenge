'''Q: Write a code for spliting bills calculator'''

### Write your code below ###

#Step_1: Ask user to input their total bill amount
bill = float(input("Enter your total bill: $"))
percentage = int(input("How many percentage tip do you want to provide: %"))
people_count = int(input("Enter the total number of people to split the bill: "))

#Step_2: formula for spliting the bill
#percentage of tip amount from the bill
tip_amount = round((bill * (percentage / 100)), 2)

# Total bill after tip percentage
total_bill = bill + tip_amount

#Total amount split after adding tip amount
Total_split_amount = round((total_bill / people_count), 2)

print(f"Your bill amount: ${bill}")
print(f"Tips amount you decided: {percentage}%")
print(f"Your total bill: ${total_bill}")
print(f"Total split amount for {people_count} people is ${Total_split_amount}.")

'''---------------------------------- END ----------------------------------'''