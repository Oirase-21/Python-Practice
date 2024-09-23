numbers = [1, 25, 16, 48, 80]

for number in numbers: # checks all the numbers in the brackets before giving answer
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break

else:
    print("these numbers are fine")