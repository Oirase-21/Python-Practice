available_exits = ["north", "south",  "east", "west"]

choose_exits = ""
while choose_exits not in available_exits:
    choose_exits = input("please choose a direction: ")

    if choose_exits not in available_exits:
        print("A direction bruv")

    if choose_exits.casefold() == ["quit", "stop"]:
        print("game over sorry you didn't make it out")
        break

    if choose_exits in available_exits:
        print(" arent you glad you got out of there")