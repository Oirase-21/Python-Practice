shopping_list = ["Eggs", "Milk", "Bread", "pasta", "Juice", "Cake"]

# for items in shopping_list:
#     if items != "Juice":
#         print("Buy " + items)


for items in shopping_list:
    if items == "Juice":
        continue  #makes the code skip juice

    print("Buy " + items)


for items in shopping_list:
    if items == "Juice":
        break #makes the code terminate at juice

    print("Buy " + items)