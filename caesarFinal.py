import replit
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

choises= "yes"

def caesar (text, shift, direction):
  dencoded=""
  for position in text: 
    if direction=="encode":
      if position in alphabet:  
        dencoded+= alphabet[(alphabet.index(position)+shift)%26]
      else:
        dencoded+=position
    elif direction=="decode":
      if position in alphabet: 
        dencoded+= alphabet[(alphabet.index(position)-shift)%26]
      else:
       dencoded+=position  
  print(f"your word is: {dencoded}")

while choises=="yes":
  print(f"{art.logo}\n")
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  choises=input("Do you want to continue yes/no\n").lower()
  replit.clear()
print("Thanks for Using Caesar Today")