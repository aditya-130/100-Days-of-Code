import os
clear = lambda: os.system('cls')

def calculate_auction_winner(bidders):
    # winner = max(bidders, key = bidders.get) // Alternate way
    # winning_bid = bidders[winner]
    winner = ""
    winning_bid = 0
    for bidder in bidders:
        if bidders[bidder] > winning_bid:
            winner = bidder
            winning_bid = bidders[bidder]
    print(f"The winner is {winner} with a bid of ${winning_bid}")
clear()
print("Welcome to the silent auction program.\n")
bidders = {}
auction_in_progress = True
while(auction_in_progress):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    more_bidders = input("\nAre there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "yes":
        clear()
    else:
        auction_in_progress = False
calculate_auction_winner(bidders)

