def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4);

# This function will accept an integer variable "end" and count by 10
# from 0 to the "end" value.
def count_by_10(end):
    # Initializeq the "count" variable as a string.
    count = ""

    # The range function parameters instruct Python to start the count
    # at 0 and stop at the variable given as the upper end of the range.
    # Since the value of the high end of a range is excluded by default,
    # you can make Python include the "end" value by adding +1 to it.
    # The third parameter tells Python to increment the count by 10.
    for number in range(0,end+1,10):

        # Although the variable "count" will hold a count of integers,
        # this example will be converted to a string using "str(number)"
        # in order to display the incremental count from 0 to the "end"
        # value on the same line with a space " " separating each
        # number.
        count += str(number) + " "

    # The .strip() method will trim the final space " " from the end of
    # the string "count"
    return count.strip()


# Call the function with 1 integer parameter.
print(count_by_10(100))
# Should print 0 10 20 30 40 50 60 70 80 90 100;

# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):


    # It is an optional code style to assign the long variable names in the
    # function parameters to shorter variable names.
    n1 = initial_number
    n2 = end_of_first_row+1  # include the upper range value with +1

    # The first for loop will create the columns.
    for column in range(n1, n2):

        # The nested for loop will create the rows.
        for row in range(n1, n2):

            # To make the matrix of numbers easier to read, include a space
            # between each number in the rows until the loop reaches the
            # end of the row. You can override the default behavior of the
            # print() function (which inserts a new line character after
            # the print command runs) by using the "end=" "" parameter
            # inside the print() function.
            print(column*row, end=" ")

        # The row ends when the upper range value is encountered within the
        # nested for loop. The outer (column) for loop should insert a new line
        # to create the next row. Use the print() function new line default
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters.
matrix(1, 4);

# For this example, the outer for loop uses an end of range index of
# 10. The value of index 10 will be 10-1, or 9.
for outer_loop in range(10):

    # Using the "outer_loop" variable as the end of range for the
    # inner loop, means the end of range index will be 9. The value
    # of index 9 will be 9-1, or 8.
    for inner_loop in range(outer_loop):

        # The printed result is the value of "inner_loop". Since
        # there aren’t any calculations in this loop, there is a
        # simple shortcut for solving what the final value printed
        # by the "inner_loop" will be. The solution is to simply use
        # the value of the "inner_loop" index, which is 8.
        print(inner_loop);

def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop+1):
        # Complete the inner loop range
        for y in range(start, stop+1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3);
# Should print the multiplication table shown above
