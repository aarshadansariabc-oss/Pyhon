import random
def check(user_guess, Answer):
    if user_guess > Answer:
        print("Too High")
        return False
    elif user_guess < Answer:
        print("Too Low")
        return False
    else:
        print("You Win, Your Guess is Correct!")
        return True

def set_dificulty():
    level = input("Choose a deifficulty. Type 'easy' or 'hard' : ").lower()
    if level == 'easy':
        return 10
    else:
        return 5
def game():
    Answer = random.randint(1,100)
    print(f"Answer is : {Answer}")
    print("Welcome to The Guessing Number Game!")
    print("I'm thinking a Number between 1 to 100.")

    Total_Lives = set_dificulty()



    print(f"You Have {Total_Lives} attempts to guess the number.")
    guess = 0
    while guess != Total_Lives:
        guess = int(input('Make a Guess : '))
        check(guess, Answer)
        Total_Lives -= 1
        print(f"You Have {Total_Lives} attempts to guess the number.")
        if Total_Lives == 0:
            print("You Lose, You Lost All Your Lives")
            break

game()
playAgain = input("Dou You Want to play again? Type 'y' or 'n' L ").lower()

if playAgain == 'y':
    game()
else:
    print("Thanks for Playing our Game!")

