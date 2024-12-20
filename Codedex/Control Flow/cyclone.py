

print("How tall are you in m?")
height = float(input())

print("How many credits do you have?")
credits = int(input())

if height >= 1.37 and credits >= 10:
    print("You can enter")
elif height < 1.37 and credits >= 10:
    print("You are not tall enough!")
elif height >=1.37 and credits < 10:
    print("You dont have enough credits")
else:
    print("You can't enter")