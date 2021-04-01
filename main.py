#main code

import random

def guess(x):
    random_num = random.randint(1,x)

    guess = 0

    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess > random_num:
            print("Sorry your guess is too high. Try again\n")
        elif guess < random_num:
            print("Sorry your guess is too low. Try again\n")
    
    print(f"Yay! {random_num} is the number that I was thinking!\n")

guess(100)

