import random
from Game_data import data

def AccountData(account):
    Account_Name = account['name']
    Account_Description = account['description']
    Account_country = account['country']
    return f"{Account_Name}, {Account_Description}, {Account_country}"

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

random_a['follower_count'] > random_b['follower_count']
random_a['follower_count'] < random_b['follower_count']
