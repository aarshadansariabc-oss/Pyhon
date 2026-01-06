import random
from Game_data import data

random_a = random.choice(data)
random_b = random.choice(data)

if random_a == random_b:
    random_b = random.choice(data)

account_name = random_a['name']
print(account_name)
