age = int(input('How old are you'))

if age >= 21 and age <= 65:
    print('Have a great day at work')
elif 12 <= age <= 19:
    print('have a great day at school')
else:
    print('enjoy your free time')

print('-'*80)

age2 = int(input('how old is he'))

if age2 >= 21 and age2 <= 65:
    print('Have a great day at work')
elif 12 <= age2 <= 19:
    if age2 == 16 or age2 == 17:
        print('go get your liscense')
    else:
        print('have a great day at school')

else:
    print('enjoy your free time')