#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
randomized_list=[letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

accumulator1= ""
accumulator2= ""
accumulator3=""
accumulator_total=""
for letter in range(0,nr_letters):
  randomize_1= random.randint(0,len(letters)-1)  
  accumulator1= accumulator1 + letters[randomize_1]
  #Also can be done as password+= random.choice(letters)
  #it picks a random from the list 
  
for number in range(0,nr_numbers):
  randomize_2= random.randint(0,len(numbers)-1)
  accumulator2= accumulator2 + numbers[randomize_2]
  
for symbol in range(0,nr_symbols):
  randomize_3= random.randint(0,len(symbols)-1)
  accumulator3= accumulator3+symbols[randomize_3]
accumulator_total=accumulator1+accumulator2+accumulator3
print(accumulator_total)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
accumulator_total2= ''.join(random.sample(accumulator_total,len(accumulator_total)))
print(accumulator_total2)
#You can also use the shuffle() and a for to joint them in random 