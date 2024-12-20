
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


print("Question 1: Do you like Dawn or Dusk?")
q1 = input()

if q1 == "Dawn":
    Gryffindor =+ 1
    Ravenclaw =+ 1
elif q1 == "Dusk":
    Ravenclaw =+ 1
    Slytherin =+ 1
else:
    print("Wrong input")


print("Question 2: When I'm dead, I want people to remember me as: (please only write the number e.g. '1')")
print("\n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold")
q2 = int(input())

if q2 == 1:
    Hufflepuff =+ 2
elif q2 == 2:
    Slytherin =+ 2
elif q2 == 3:
    Ravenclaw =+ 2
elif q2 == 4:
    Gryffindor =+ 2
else:
    print("Wrong input")


print("Question 3: Which kind of instrument most pleases your ear? (please only write the number e.g. '1')")
print("\n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum")
q3 = int(input())

if q3 == 1:
    Slytherin =+ 4
elif q3 == 2:
    Hufflepuff =+ 4
elif q3 == 3:
    Ravenclaw =+ 4
elif q3 == 4:
    Gryffindor =+ 4
else:
    print("Wrong input")


houses = {"Gryffindor": Gryffindor, "Ravenclaw": Ravenclaw, "Hufflepuff": Hufflepuff, "Slytherin": Slytherin}
chosen_house = max(houses, key=houses.get)

print(f"You belong in house {chosen_house}")


