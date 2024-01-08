from replit import clear
from art import logo
print(logo)

no_more_bidders = False
auction = {}

def find_highest_bidder(auction):
  highest_bid = 0
  winner = ""
  for bidder in auction:
    bid_amount = auction[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not no_more_bidders:
  name = input("What is your name? ")
  bid_price = int(input("What much you would like to bid? $"))
  auction[name] = bid_price
  question = input("Are there any other bidders? Yes or No? ")
  if question == "Yes":
    clear()
  else:
    no_more_bidders = True
    find_highest_bidder(auction)
