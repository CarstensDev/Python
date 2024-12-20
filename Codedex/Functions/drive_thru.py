
food = ["Cheeseburger (1)", "Fries (2)", "Soda (3)", "Ice Cream (4)", "Cookie (5)"]

print("Hey :D welcome to this McDonald\'s, what can i get you?")
print(food)
answer = input()


def get_item():
    if answer == "q":
        quit()
    elif answer == "1":
        print("You want a cheesburger?")

    elif answer == "2":
        print("You want fries?")
        
    elif answer == "3":
        print("You want soda?")
        
    elif answer == "4":
        print("You want ice cream?")
        
    elif answer == "5":
        print("You want a cookie?")
        
    else:
        print("Wrong input... please choose a number")


get_item()



