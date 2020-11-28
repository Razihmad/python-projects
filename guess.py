import random

n = random.randint(1,100)
guessed_number = int(input("Guess the number between 1,100 : "))
attempt = 0
while True:
    if guessed_number>n:
        print("You Guess Higher Number : ")
        guessed_number = int(input("Guess The Number Again : "))
        attempt +=1

    elif guessed_number<n:
        print("You Guess Lower Number")
        guessed_number = int(input("Guess The number Again : "))
        attempt +=1

    elif n == guessed_number:
        attempt +=1
        print("Hurray !You Guess The Correct Number ,you try number of times  = ",attempt)
        break




