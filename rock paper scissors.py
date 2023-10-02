rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇

hands=[rock,scissors, paper]

choice=int(input("Please select 0 for rock, 1 for scissors and 2 for paper\n"))
machine_choice= random.randint(0,2)
print(f"your choice{hands[choice]}\n Machine´s choice {hands[machine_choice]}")

if machine_choice==choice:
  print("is a tight")
elif choice==0 and machine_choice==1:
  print("you win")
elif choice==0 and machine_choice==2:
  print("You loose")
elif choice==1 and machine_choice==0:
  print("You loose")
elif choice==1 and machine_choice==2:
  print("You win")
elif choice==2 and machine_choice==0:
  print("You win")
else:
  print("You loose")