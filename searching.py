shopping_list = ["Eggs", "Milk", "Bread", "pasta", "Juice", "Cake"]

item_to_find = "cereal"
found_a = None

#for index in range(amount of items that are in the shopping list)
# for index in range (len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_a = index
#         break

if item_to_find in shopping_list:  #same as commentted code above
    found_a =shopping_list.index(item_to_find)

if found_a is not None:
    print("item found at position {}".format(found_a))
else:
    print("{} not found".format(item_to_find))