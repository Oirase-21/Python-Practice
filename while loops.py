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

# Should print 18 15 12 9 6 3 0


def X_figure(salary):

    # Initializes the counter as an integer.
    tally = 0

    # The if-statement checks if the variable "salary"
    # is equal to 0.
    if salary == 0:
        # If true, then it increments the counter to
        # show there is 1 digit in 0.
        tally += 1

    # The while loop starts to run while the "salary"
    # is greater than or equal to 1 (the loop will
    # not run if the "salary" is 0).
    while salary >= 1:

        # The body of the while loop counts the digits
        # in "salary" by counting the number of times
        # "salary" can be divided by 10 until "salary"
        # is no longer >= 1.
        salary = salary/10

        # Add 1 to the counter to tally the number of
        # times the loop runs.
        tally += 1

    # Return the results of the "tally" of the number
    # of digits in "salary".
    return tally

# Call the X_figure function with 1 parameter, converted to a string,
# inside a print function with additional strings.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.");

# Should print"The CEO has a 7-figure salary."



def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0: # Complete the while loop
            return_string += str(x) # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1 # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
print(countdown(0)); # Should be "Cannot count down to 0";


