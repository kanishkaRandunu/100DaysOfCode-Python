from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print('\nWelcome to the Secret Auction')

bids = {}

def finding_winner(bidding_dict):
  max_val = 0
  winner  = ""
  
  for bidder in bidding_dict:
    if bidding_dict[bidder] >= max_val:
      max_val = bidding_dict[bidder] 
      winner  = bidder
  print(f"The winner is {winner} and his bid value is {max_val} ")

auction_close = False

while not auction_close:
  name = input("Enter your name: ")
  bid_val = int(input("Enter your bid: "))
  bids[name] = bid_val

  cont_bid = input("Are the any other users? (yes/ no) ")
  if cont_bid == "no":
    auction_close = True
    finding_winner(bids)
  elif cont_bid == "yes":
    clear()







  
  


