def Temp_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, Temp_celsius(x));



teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team);


greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index])
    index += 1;




string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”;

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop");

# For this example, the while loop will count down by threes starting
# from 18 and ending at 0.
starting_number = 18

# The while loop will continue to loop until it reaches 0.
while starting_number >= 0:

    # To make the sequence of numbers easier to read, include a space
    # between each number in the sequence. You can override the default
    # behavior of the print() function by using the "end=" parameter with
    # the print() function. The syntax for adding a space is: end=" "
    print(starting_number, end=" ")

    # Decrement the "starting_number" variable by -3.
    starting_number -= 3;

def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # numbers up to and including the "maximum" value.
    for maximum in range(minimum, maximum+1 ):

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(maximum) + " "

        # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0
