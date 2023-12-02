from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

dict_bid = {}
other_players = "yes"

while other_players == "yes":
  name = input("What is your name?")
  bid_price = int(input("What is your bid price? $"))
  
  dict_bid[name] = bid_price
  
  other_players = input("Are there other players who want to bid? (Yes or No) ").lower()
  
  if other_players == "yes":
    clear()
  else:
    highest_bidder = ""
    highest_bid = 0
    for key in dict_bid:
      if dict_bid[key] > highest_bid:
        highest_bidder = key
        highest_bid = dict_bid[key]

print(f"Highest bidder is {highest_bidder} with a bid of ${highest_bid}.")
