from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.




def add_bidders():
  bidders= {}
  verification="yes"
  print(art.logo)
  while verification== "yes":
    name= input("Please let us know the bidder name\n")
    bidder_price= int(input(f"Please let us know how much {name} wants to bid\n$"))
    bidders[name]=bidder_price
    verification=input("Do you have more bidders to check-in?\n")
  print(bidders)
  highest_bid=0
  for i in bidders:
    if highest_bid < bidders[i]:
      highest_bid=bidders[i]
      highest_bidder=i
  print(f"El que ofrecio más es {highest_bidder} con: ${highest_bid}")
  
add_bidders()
