import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("1. Rock\n2. Paper\n3. Scissors")
user_choice = int(input("Enter your choice 1/2/3: "))
computer_choice = random.randint(1, 3)

if user_choice == 1:
    print(f"You choose '{rock}'")
    if computer_choice == 2:
        print(f"Computer choose '{paper}'")
        print("Computer Win")
    elif computer_choice == 3:
        print(f"Computer choose '{scissors}'")
        print("You Win")
    elif computer_choice == 1:
        print(f"Computer Choose '{rock}'")
        print("It's a draw")
    else:
        print("Enter a valid choice")


if user_choice == 2:
    print(f"You Choose '{paper}'")
    if computer_choice == 1:
        print(f"Computer choose '{rock}'")
        print("You Win")
    elif computer_choice == 3:
        print(f"Computer choose '{scissors}'")
        print("Computer Win")
    elif computer_choice == 2:
        print(f"Computer Choose '{paper}'")
        print("It's a draw")
    else:
        print("Enter a valid choice")


if user_choice == 3:
    print(f"You Choose '{scissors}'")
    if computer_choice == 1:
        print(f"Computer choose '{rock}'")
        print("Computer Win")
    elif computer_choice == 2:
        print(f"Computer choose '{paper}'")
        print("You Win")
    elif computer_choice == 3:
        print(f"Computer Choose '{scissors}'")
        print("It's a draw")
    else:
        print("Enter a valid choice")