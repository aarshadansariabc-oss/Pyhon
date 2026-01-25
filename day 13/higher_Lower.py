import random
from Game_data import data

def AccountData(account):
    Account_Name = account['name']
    Account_Description = account['description']
    Account_country = account['country']
    return f"{Account_Name}, {Account_Description}, {Account_country}"


def moreFollowers(account_a, account_b):
    if account_a['follower_count'] > account_b['follower_count']:
        return 'a'
    else:
        return 'b'

random_a = random.choice(data)
random_b = random.choice(data)

if random_a == random_b:
    random_b = random.choice(data)


print(f"Compare A : {AccountData(random_a)}.")
print(f"Account  B : {AccountData(random_b)}. ")

#Ask User that who has more followers
userChoice = input("Who has More followers : 'A' or 'B' : ").lower()

#check user is correct of not :
points = 0

print(f"{moreFollowers(random_a, random_b)}")
# print(f"{moreFollowers(random_a,random_b,userChoice)}")
if userChoice == moreFollowers(random_a, random_b):
    points += 1
    print(f"Corret {points}")
else:
    points -= 1
    print(f"Wrong {points}")

