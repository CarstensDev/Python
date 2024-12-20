class Pokemon:

    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ', ' + self.name + '!')

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")

        if len(self.types) == 1:
            print(f"Types: {self.types[0]}")
        else:
            print(f"Types: {self.types[0]} and {self.types[1]}")

        print(f"Description: {self.description}")

        if self.is_caught:
            print("This Pokemon is caught")
        else:
            print("This Pokemon is not caught")

pikachu = Pokemon(25, "Pikachu", ["Electric"], "A yellow mouse Pokemon", True)
charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)

pikachu.speak()
charizard.speak()

