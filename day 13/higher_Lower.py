import random
from Game_data import data

def AccountData(account):
    Account_Name = account['name']
    Account_Description = account['description']
    Account_country = account['country']
    return f"{Account_Name}, {Account_Description}, {Account_country}"


def moreFollowers(guess, account_a, account_b):
    if account_a['follower_count'] > account_b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


points = 0


while True:
    random_a = random.choice(data)
    random_b = random.choice(data)
    

    if random_a == random_b:
        random_b = random.choice(data)

    print(f"Compare A : {AccountData(random_a)}.")
    print(f"Account  B : {AccountData(random_b)}. ")

    userChoice = input("Who has More followers : 'A' or 'B' : ").lower()

    is_correct = moreFollowers(userChoice, random_a, random_b)


    if is_correct:
        points += 1
        print(f"You'r right your score is {points}")

    else:
        print(f"Sorry you loose Your Total point is {points}")
        break
