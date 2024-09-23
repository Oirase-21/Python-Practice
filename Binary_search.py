low = 1
high = 100

print("please guess a number between {} and {}".format(low, high))
input("press enter to start")

guesses = 1

while True:
    print("\t guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input(" my guess is {}. Should i guess higher or lower?"
                     "\nEnter h or l, or c if my guess was correct"   #get this by reformatting code
                     .format(guess)).casefold()
    if high_low == "h":

        # guess higher new low is the guess  plus 1
        low = guess + 1
    elif high_low == "l":
        # guess lower new high is the guess minus 1
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break

    else:
        print("please enter h,l,or c")

    #guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))

