import random
from Game_data import data

point = 0
def more_followers(user, accounta, accountb):
    if accounta['follower_count'] > accountb['follower_count']:
        return user == 'a'
    else:
        return user == 'b'
    
def instInfo(account):
    return f"{account['name']}, {account["description"]}"

while True:
    a = random.choice(data)
    b = random.choice(data)


    while a == b:
        b = random.choice(data)

    print(f"Choice a : {instInfo(a)} ")
    print(f"Choice b : {instInfo(b)} ")

    userChoice = input("Enter your choice A and B : ")

    is_correct = more_followers(userChoice, a, b)

    if is_correct:
        point += 1
        print(f"Correct choice : {point}")
    else:
        print(f"Wrong choice! your total points is  {point}")
        break
