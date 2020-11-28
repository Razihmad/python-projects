import random
from random import choice

def dicenumber():
    print(random.randint(1,6))

game = True

print("Want To Play Ludo y or n: ")
choice = input("")
if choice == 'y':
    while game:
        # dicenumber()
        roll_dice = input("want to roll dice y or n: ")
        if roll_dice =='y':
            dicenumber()
        else:
            game = False
