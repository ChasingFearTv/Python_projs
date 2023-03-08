
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1L = name1.lower()
name2L = name2.lower()

true_count = name1L.count('t') + name2L.count('t') + name1L.count('r') + name2L.count('r') + name1L.count('u') + name2L.count('u') + name1L.count('e') + name2L.count('e') 
love_count = name1L.count('l') + name2L.count('l') + name1L.count('o') + name2L.count('o') + name1L.count('v') + name2L.count('v') + name1L.count('e') + name2L.count('e')

loveadd = str(true_count) + str(love_count)

loveScore = int(loveadd)

if loveScore <= 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore < 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")