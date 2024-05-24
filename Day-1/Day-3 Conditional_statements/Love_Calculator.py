'''Q: Wite a code to calculate the Love meter between two people'''

### Write your code below ###

# Step_1: Ask user for input
name_1 = input("Enter your name: ").lower()
name_2 = input("Enter your crush name: ").lower()

combined_names = name_1 + name_2
lower = combined_names.lower()

t = lower.count("t")
print(f"T occurs {t} times")
r = lower.count("r")
print(f"R occurs {r} times")
u = lower.count("u")
print(f"U occurs {u} times")
e = lower.count("e")
print(f"E occurs {e} times")

True_count = str(t+r+u+e)
print(True_count)

l = lower.count("l")
print(f"L occurs {l} times")
o = lower.count("o")
print(f"O occurs {o} times")
v = lower.count("v")
print(f"V occurs {v} times")
e = lower.count("e")
print(f"E occurs {e} times")

Love_count = str(l+o+v+e)
print(Love_count)

Love_score = (True_count + Love_count)
print(Love_score)

if Love_score < "10" and Love_score > "90":
    print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif Love_score > "40" and Love_score < "50":
    print(f"Your score is {Love_score}, you are alright together.")
else:
    print(f"Your score is {Love_score}")