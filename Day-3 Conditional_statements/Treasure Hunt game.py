'''Q: Write a code for Treasur hunt game'''

### Write your code here ###

Q1 = "Q1. You cut me on a table, but I'm never eaten"
print(Q1)
answer1 = input("Enter your Answer: ")
Ans1 = ("Deck of cards").lower()
if answer1 == Ans1:
    print("Great Start, keep moving")
    Q2 = "Q2. The building that has the most stories."
    print(Q2)
    answer2 = input("Enter your Answer: ")
    Ans2 = ("Library").lower()
    if answer2 == Ans2:
        print("Awesome, keep moving")
        Q3 = "Q3. I dry as I get wetter."
        print(Q3)
        answer3 = input("Enter your Answer: ")
        Ans3 = ("Towel").lower()
        if answer3 == Ans3:
            print("Hattrick, don't stop now. Continue to next one")
            Q4 = "Q4. I make bones hard and cookies soft. Babies love me."
            print(Q4)
            answer4 = input("Enter your Answer: ")
            Ans4 = ("Milk").lower()
            if answer4 == Ans4:
                print("Keep Moving, you're play like a pro")
                Q5 = "Q5. I have hands but cannot clap."
                print(Q5)
                answer5 = input("Enter your Answer: ")
                Ans5 = ("Clock").lower()
                if answer5 == Ans5:
                    print("Almost reached the destination, Don't stop now")
                    Q6 = "Q6. I go up and down, but I never move."
                    print(Q6)
                    answer6 = input("Enter your Answer: ")
                    Ans6 = ("Staircase").lower()
                    if answer6 == Ans6:
                        print("One more step to reach the treasue.")
                        Q7 = "Q7. I’m tall when I’m young and short when I’m old."
                        print(Q7)
                        answer7 = input("Enter your Answer: ")
                        Ans7 = ("Candles").lower()
                        if answer7 == Ans7:
                            print("You reached the treasure")
                        else:
                            print("Unfortunately its Game over for you, Don't worry start again")
                    else:
                        print("Unfortunately its Game over for you, Don't worry start again")
                else:
                    print("Unfortunately its Game over for you, Don't worry start again")
            else:
                print("Unfortunately its Game over for you, Don't worry start again")
        else:
            print("Unfortunately its Game over for you, Don't worry start again")
    else:
        print("Unfortunately its Game over for you, Don't worry start again")
else:
    print("Unfortunately its Game over for you, Don't worry start again")




