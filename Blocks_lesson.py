## this lesson is on blocks
for i in range (1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3))
    print("*" * 80)

### if statement lesson

name = input("please enter name here: ")
age = int(input("please enter age here:  ".format(name)))
print(age)

if age >= 17:
    print("You old enough to ride this ride ")
    print("Please put an x in the box")
else:
    print("Sorry you are not old enough to ride come back in {0} years".format((17-age)))

## ELIF lesson
name1 = input("please enter name here: ")
age1 = int(input("please enter age here:  ".format(name1)))

if age1 >= 17:
    print("You old enough to ride this ride ")
elif age1 >= 140:
    print("Listen you know you are not really that old try again")
else:
    print("Sorry you are not old enough to ride come back in {0} years".format((17-age1)))

