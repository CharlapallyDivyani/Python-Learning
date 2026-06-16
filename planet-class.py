class Planet:
    def __init__(self, name, planet_type, star):
        # Validate that all arguments are strings
        if not all(isinstance(arg, str) for arg in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        
        # Validate that all arguments are non-empty strings
        if not all([name, planet_type, star]):
            raise ValueError("name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

# Creating instances of the Planet class
planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Kepler-186f", "Super Earth", "Kepler-186")
planet_3 = Planet("Jupiter", "Gas Giant", "Sun")

# Printing each planet object (which invokes the __str__ method)
print(planet_1)
print(planet_2)
print(planet_3)

# Calling the orbit method on each planet and printing the result
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
