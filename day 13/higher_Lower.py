import random
from Game_data import data


def account_data(account):
    """This function is used for to get details about user data"""
    return f"{account['name']}, {account['description']}, {account['country']}"


def more_followers(guess, a, b):
    if a['follower_count'] > b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


points = 0

while True:
    a = random.choice(data)
    b = random.choice(data)

    while a == b:
        b = random.choice(data)

    print(f"Compare A: {account_data(a)}")
    print(f"Compare B: {account_data(b)}")

    guess = input("Who has more followers? A or B: ").lower()

    if guess not in ['a', 'b']:
        print("Invalid input!")
        continue

    if more_followers(guess, a, b):
        points += 1
        print(f"Correct! Your score is {points}")
    else:
        print(f"Wrong! Final score: {points}")
        break
