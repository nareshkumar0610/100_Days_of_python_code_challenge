'''Q: Write a code for Hangman Game Project'''

### Write you code below ###

#Step_1: import module files
from ascii_art import stages, logo
from list_of_words import animals

# Begining of the game code
print(logo)
print("Welcome to the Hangman Game.")
print("1. Start\n2. Game instructions\n3. Quit")


user_choice1 = "n"

while user_choice1 == "n":
    user_choice = input("\nEnter the choice 1/2/3: ")
    if user_choice == "1":
        print("\nFind the animal name\n")
        #Step_2: Generate random word
        import random

        guess_word = random.choice(animals)
        # print(guess_word)


        #Step_3: show the guess word count as "_"
        guess_count = []

        for letters in guess_word:
            guess_count += "_"

        print(guess_count)

        #Step_4: Ask user to enter the guess letter
        end_of_game = False
        lives = 6
        while end_of_game == False:
            guess = input("Guess a Letter: ").lower()

        #Step_5: Replace the "_" with guess word
            for position in range(len(guess_word)):
                if guess_count[position] == guess:
                    print(f"The letter '{guess}' is already entered")
                elif guess == guess_word[position]:
                    guess_count[position] = guess
                
            if guess not in guess_word:
                print(f"letter '{guess}' not in the word.\nYou lost a life.")
                lives -= 1
                
            print(stages[lives])
            print(guess_count)

            if lives == 0:
                end_of_game = True
                print(f"\nThe correct word is {guess_word}")
                print("You Lost the game\nStart te new game")
            elif "_" not in guess_count:
                end_of_game = True
                print(f"\nYou found the word '{guess_word}'.\nYou won the game.\n\nStart te new game and find the new word")
    elif user_choice == "2":
        print('''The object of hangman is to guess the secret word before the stick figure is hung. Player have 6 lives, each incorrect letter player will lose 1 life. Gameplay continues until the players guess the word or they run out of guesses and the stick figure is hung.''')
    
    else:
        user_choice == "3"
        user_choice1 = input("Are you sure to quit (Y/N): ").lower()
        if user_choice1 == "y":
            quit()
        else:
            user_choice1 == "n"




