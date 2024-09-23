# for this code the output is a mutiplication table for 1-20
for i in range(1, 13):
    for j in range(1, 21):
        print("{0} times {1} is {2}".format(j, i, i*j))
    print("-"*10)


