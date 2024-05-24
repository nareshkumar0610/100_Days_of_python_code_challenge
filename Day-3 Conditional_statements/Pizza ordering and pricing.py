'''Q: Write a code for "PIZZA ORDERING" and "PRICING"?'''

### Write your code below ###


# Step_1: Ask user to enter the input
print("Type of Pizza:\n1. Margherita\n2. Veggie\n3. Cheese Burst\n4. Double Cheese Margherita\n")
pizza = int(input("Enter the pizza you want 1/2/3/4: "))

Margherita = 100
Veggie = 150
Cheese_Burst = 200
Double_Cheese_Burst = 150

print("Size of pizza:\n1. Small\n2. Medium\n3. Large\n4. Extra Large")
size = int(input("What size would you prefer 1/2/3/4/: "))

Small = 50
Medium = 100
Large = 150
Extra_Large = 200

print("Toppings may cost extra charge")
toppings = input("Do you want toppings in your pizza Y/N? ").lower()

topps = 15

#Pizza Type

if pizza == 1:
    pizza_cost = Margherita
elif pizza == 2:
    pizza_cost = Veggie
elif pizza == 3:
    pizza_cost = Cheese_Burst
elif pizza == 4:
    pizza_cost = Double_Cheese_Burst
else:
    print("kindly enter a valid choice")
    pizza_cost = 0

#Pizza Size
if size == 1:
    size_cost = Small
elif size == 2:
    size_cost = Medium
elif size == 3:
    size_cost = Large
elif size == 4:
    size_cost = Extra_Large
else:
    print("kindly enter a valid choice")
    size_cost = 0

#Toppings
if toppings == "Y" or toppings == "y":
    topps_cost = topps
else:
    print("kindly enter a valid choice")
    topps_cost = 0

print("Your final bill is: ", pizza_cost + size_cost + topps_cost)
