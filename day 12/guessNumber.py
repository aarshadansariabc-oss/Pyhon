import random

#set Game Dificulty
def Set_Dificulty():
    level = input("Choose a deifficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        return 10
    if level == "hard":
        return 5
    
#Check answer 
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
    
#Game Logic

def game():
    Answer = random.randint(1,100)
    print("Welcome to the Guessing Number :")
    print("You Have to guess number between (1 to 100)")

    Total_lives = Set_Dificulty()
    print(f"You have Total {Total_lives} to guess the Number")

    while Total_lives > 0:
        user_guess = int(input("Guess a Number : "))
        is_correct = check(user_guess,Answer)

        if is_correct:
            return
        
        Total_lives -=1
        print(f"You have {Total_lives} Chances ")
        
        if Total_lives == 0:
            print(f"You have lost all your lives\nThe Answer is {Answer}")

#Ask user to play the game agin           
while True:
    game()
    play_again = input("Do You want to play again. 'y' or 'n' : ").lower()
    if play_again != 'y':
        print("Thanks for Playing our game")
        break