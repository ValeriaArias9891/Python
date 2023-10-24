import art
import random
import game_data
# Welcome the user to the game
def welcome():
  print(art.logo)
  print("Please choose who has more followers A. or B.")
# Return the contestant
def return_contest():
  number_of_contendents=len(game_data.data)
  chosen_one= random.randint(1,number_of_contendents)
  return(game_data.data[chosen_one-1])


game_datas=[]
cont=0
verifier=True

welcome()
game_datas.append(return_contest())

while verifier:
  game_datas.append(return_contest())
  # print(game_datas)
  print(f"{game_datas[cont]['follower_count']}  {game_datas[cont+1]['follower_count']} ")
  print(f"A. The first one is {game_datas[cont]['name']}  they´re a {game_datas[cont]['description']} from {game_datas[cont]['country']}")
  a=int(game_datas[cont]['follower_count'])
  print(art.vs)
  print(f"B. The second one is {game_datas[cont+1]['name']} they´re a {game_datas[cont+1]['description']} from {game_datas[cont+1]['country']}")
  b=int(game_datas[cont+1]['follower_count'])
  
  choice=input("Please tell me your choice\n").lower()
  
  if a>b:
    if choice == 'a':
      print(f"that's right {game_datas[cont]['name']} has more followers")
      cont+=1
    else:
      print(f"Sorry {game_datas[cont]['name']} has more followers")
      verifier=False
  elif a<b:
    if choice=='b':
      print(f"that's right {game_datas[cont+1]['name']} has more followers")
      cont+=1
    else:
      print(f"Sorry {game_datas[cont+1]['name']} has more followers")
      verifier=False
  elif a==b:
    print("It's a tie")
    cont+=1
print("Thanks for playing")