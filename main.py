# 100 Days of Code
# Silent Auction

from replit import clear
from art import logo

print(logo)

# Auction start. Will continue to loop and get info from User
# until no more bids are left
print("\nWelcome to the Silent Auction\n")
auction_going = True
bidders = {} # empty dictionary to store bids
while auction_going:

  name = input("What is your name?: ")
  amount = int(input("What is your bid?: $"))

  bidders[name] = amount

  cont = input("Are there any other bidders? Type 'yes or 'no'.\n")

  if cont == 'yes':
    clear()
  elif cont == 'no':
    auction_going = False


highest_bid = 0
highest_bidder = ""
# loop through dictionary to find highest bid, and print the winner
for bidder in bidders:
  if bidders[bidder] > highest_bid:
    highest_bid = bidders[bidder]
    highest_bidder = bidder
  
print(f"The winner {highest_bidder} with an amount of ${highest_bid}!")