import random

highest = 15
answer = random.randint(1, highest)

print("please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("you got it the first time")
else:
    while guess != answer:
        print("please try again")

        if guess < answer:
            print("please guess higher")
            guess = int(input())

        if guess > answer:
            print("Please guess lower")
            guess = int(input())

        if guess == answer:
            print("great guess you got it")

