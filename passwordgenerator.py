import random
import secrets

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosenLetters = random.sample(letters, nr_letters)
chosenSymbols = random.sample(symbols, nr_symbols)
chosenNumbers = random.sample(numbers, nr_numbers)

password = ""

for letters in chosenLetters:
    randomletter = secrets.choice(letters)
    password += randomletter
for symbols in chosenSymbols:
    randomsymbol = secrets.choice(symbols)
    password += randomsymbol
for numbers in chosenNumbers:
    randomnumber = secrets.choice(numbers)
    password += randomnumber

mixpassword = list(password)
random.shuffle(mixpassword)
password = "".join(mixpassword)

print(f"your strong password is: {password}")
