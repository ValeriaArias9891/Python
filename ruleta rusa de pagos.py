names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random
lenght=len(names)
selector = random.randint(0,lenght-1)
print(f"{names[selector]} is going to buy the meal today!")
