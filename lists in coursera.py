x = ["Now", "we", "are", "cooking!"]
##this is a list

x = ["Now", "we", "are", "cooking!"]
type(x)
## this tells the type of string

x = ["Now", "we", "are", "cooking!"]
len(x)
## this is the length of the list

x = ["Now", "we", "are", "cooking!"]
"are" in x
##this is cheking if what you put in the list is there.

x = ["Now", "we", "are", "cooking!"]
print(x[0])
print(x[3])
##this prints the words that are specifically in the list.

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
print(fruits)
##modifies list

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
##appends the list

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits);



def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(result)
type(result);

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
## counts the amount of characters and gets the average length


winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
##i dont know yet but enumerate means to keep track of the numbers
