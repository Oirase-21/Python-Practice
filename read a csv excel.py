import csv

# replace 'customers.csv' with your filename or path to file (i.e. /Desktop/folder/file.csv)


with open(r"C:\Users\brown\ Documents\ accounting for bonus.xlsx', newline='") as csvfile:

    cust_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in cust_reader:

        print(', '.join(row))