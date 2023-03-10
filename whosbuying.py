names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

random = random.randint(0, len(names)-1)
payer = names[random]
print(f"{payer} is going to buy the meal today!")