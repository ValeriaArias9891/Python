alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar (text, shift, direction):
  dencoded=""
  for position in text: 
    if direction=="encode":
      dencoded+= alphabet[(alphabet.index(position)+shift)%26]
    elif direction=="decode":
      dencoded+= alphabet[(alphabet.index(position)-shift)%26]
  print(dencoded)

caesar(text, shift, direction)