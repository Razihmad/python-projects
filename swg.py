# snake water gun game

import random
def minechoice():
    return random.choice(seq=['snake','water','gun'])

player_score = 0
mine_score = 0
for i in range(10):
    mine = minechoice()
    player_choice = input("what do you want => snake, water,or gun  : ")

    if player_choice=='snake' and mine== 'water':
        print("You Win")
        print(mine)
        player_score +=10
    elif player_choice == 'snake' and mine == 'gun':
        print("You Loose")
        print(mine)
        mine_score +=10
    elif player_choice =='water' and mine == 'snake':
        print("You Loose")
        print(mine)
        mine_score +=10
    elif player_choice == 'water' and mine == 'gun':
        print("You Win")
        print(mine)
        player_score +=10

    elif player_choice == 'gun' and mine == 'snake':
        print("You Win")
        print(mine)
        player_score +=10


    elif player_choice == 'gun' and mine == 'water':
        print("You Loose")
        print(mine)
        mine_score +=10

    else:
        print("match draw")

if mine_score>player_score:
    print("You Lost the game Your core =",player_score)
else:
    print("you won the game Your score = ",player_score)


