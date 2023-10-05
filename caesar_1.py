alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (text, shift):
  encoded=""
  for position in text: 
    encoded+= alphabet[(alphabet.index(position)+shift)%26]

  print(encoded)
#second part 

def decrypt (text, shift):
  decoded=""
  for position in text: 
    decoded+= alphabet[(alphabet.index(position)-shift)%26]

  print(decoded)

if direction=="encode":
  encrypt(text, shift)
elif direction=="decode":
  decrypt(text, shift)
else:
  print("Error")