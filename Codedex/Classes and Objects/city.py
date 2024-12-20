class City:

    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

NY = City("New York", "USA", 8.4, ["Statue of Liberty", "Central Park", "Empire State Building"])
Köln = City("Köln", "Germany", 1.1, ["Köln Cathedral", "Old Town Hall", "Romanesque Cathedral"])

print(vars(NY))
print(vars(Köln))
