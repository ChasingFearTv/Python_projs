import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors? \n"
)
choice_num = int(choice)
user_choice = options[choice_num]
cpu_choice = random.choice(options)

if user_choice > cpu_choice:
    print(
        f"You chose:\n {user_choice}, and the computer chose:\n {cpu_choice}, \nyou win."
    )
if cpu_choice > user_choice:
    print(
        f"You chose:\n {user_choice}, and the computer chose:\n {cpu_choice}, \nyou lose."
    )
if cpu_choice == user_choice:
    print(
        f"You chose:\n {user_choice}, and the computer chose:\n {cpu_choice},\nits a draw."
    )
