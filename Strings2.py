#
#         01234567890123
Parrot = "Royal Purple"
print(Parrot)
print(Parrot[3])

#Mini Challenege print out plural with each character on a separate line using indexing
print(Parrot[6])
print(Parrot[4])
print(Parrot[7])
print(Parrot[0])
print(Parrot[3])
print(Parrot[10])


#when doing negative indexing you start from the opposite end of the string and count.





#  Slicing tutorial
#slicing starts at index beginning number and ends at but does not include ending number

#       01234567890123
LION = "Royal Purple"

print(LION[0:6])   #Royal
print(LION[0:3])    #Roy
print(LION[6:10])   #Purp
print(LION[:6])

print(LION[6:12])
print(LION[6:])
print(LION[:6] + LION[6:])


print(LION[:])
#new lesson after here
#
#
print(LION[-4:-2])
print(LION[-4:12])
print(LION[-14:-8])


####### lesson on using a step in a slice.

print(LION[0:4:3])


# #numbers seperators
# number = "49,859,997,836,222"/
# print(number[2::5])
# seperators = number[1::6]
# print(seperators)
#
# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])



number2 = input("please enter a number with as many seperators as u like:  ")
separators2 = ""

for char in number2:
    if not char.isnumeric():
        separators2 = separators2 + char

print(separators2)

values2 = "".join(char if char not in separators2 else " " for char in number2).split()
print([int(val) for val in values2])