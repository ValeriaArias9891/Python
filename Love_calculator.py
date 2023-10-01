print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name_joined = name1+name2
name_joined2= name_joined.lower()

# we check for true 
t= name_joined2.count('t')
r= name_joined2.count('r')
u= name_joined2.count('u')
e= name_joined2.count('e')

total1= t+r+u+e

#we check for looove 

l= name_joined2.count('l')
o= name_joined2.count('o')
v= name_joined2.count('v')
e= name_joined2.count('e')

total2=l+o+v+e
total_string= str(total1)+str(total2)
total_inte= int(total_string)

if total_inte<10 or total_inte>90:
  print(f"Your score is {total_inte}, you go together like coke and mentos.")
elif total_inte>=40 and total_inte<=50:
  print(f"Your score is {total_inte}, you are alright together.")
else:
  print(f"Your score is {total_inte}.")