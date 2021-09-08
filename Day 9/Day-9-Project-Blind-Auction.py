from replit import clear
import art
print(art.logo)
#HINT: You can call clear() to clear the output in the console.

# Test Run
# numbers = {
#   "First": 10,
#   "Second": 20
# }
# maximum = max(numbers)
# print(f"The Highest bid was {maximum}, their bid was {numbers[maximum]}")
cont = True #condition for while
auction = {} #establishing emoty dictionary

while cont == True:
  # taking input
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  # storing inouts in dictionary
  auction[name] = bid
  # storing maximum bid in variable max_bid
  max_bid = max(auction)
  y_or_no = input("Are there any other users who want to bid? Type 'yes' or 'no': ").lower()
  if y_or_no == "yes":
    clear()
  else:
    print(f"The highest bid was {max_bid} with a bid of ${auction[max_bid]}")
    cont = False

# Alternative to finding max bid
# def max_bid():
#   highest_bid = 0
#   for bidder in auction:
#     bid = auction[bidder]
#     if bid > highest_bid:
#       highest_bid = bid 
#     print(highest_bid)
