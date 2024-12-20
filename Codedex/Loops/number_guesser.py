guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input("guess the number: "))
    tries += 1
    
print("you got it")