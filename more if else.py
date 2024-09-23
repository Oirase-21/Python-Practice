#else if guessing game
answer = 10

print("Please guess a number between 1 and 20")
guess = int(input())

if guess < answer:
    print("please guess higher")
    guess = int(input())
    if guess == answer:
        print("great guess you got it")
    else:
        print("sorry that's not it")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("great guess you got it")
    else:
        print("sorry that's not it")
else:
    print("you got it the first time")
# if you want to comment multiple lines highlight and do ctrl /
