import random


symbols = ["🍒", "🍇", "🍉", "7️⃣ "]

def play():
    result = random.choices(symbols, k=3)
    print(" | ".join(result))
    
    i = 1
    while result != ["7️⃣ ", "7️⃣ ", "7️⃣ "]:
        answer = input("Do you want to play again? (y/n)")
        if answer == "y":
            result = random.choices(symbols, k=3)
            print(" | ".join(result))
            i += 1
            print(i)
        elif answer == "n":
            print("Thanks for playing!")
            break # closes the loop
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    else:
        print("Jackpot!💰")
    


play()

