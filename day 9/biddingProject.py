import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("................Welcome to the bidding projects..............")

bids = {}
bidding_finished = False
winner = ""

def find_highest_bidder(bidding_record):
    maxBid = 0
    for bidder in bidding_record:
        bid_amound= bidding_record[bidder] 
        if bid_amound > maxBid:
            maxBid = bid_amound
            winner = bidder
    print(f"The winner is {winner} with a bid of {maxBid}")

while not bidding_finished:
    name = input("Enter your Name : ")
    price = int(input("What is your bid ? $"))
    bids[name]=price
    should_continue = input("Are ther any other bidderrs? Type 'yes or no '.").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    else:
        clear()


