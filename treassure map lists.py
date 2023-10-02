line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇

position1=position[0].lower()
position2=int(position[1])

abc=["a","b","c"]
position1_1=abc.index(position1)

map[position2-1][position1_1]= "X"
print(f"{line1}\n{line2}\n{line3}")