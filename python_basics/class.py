class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def get_profile(self) -> str:
        profile = (f"A dog belongs to the {self.species} specie. "
                   f"My dog's name is {self.name} and is {self.age} years old.")
        return profile


# Creating an object from the Dog class
# Also called an instance of the class
my_dog = Dog("Kat", 2)

# Creating another object from the Dog class
my_dog2 = Dog("Luna", 0)

print(my_dog.species)
print(my_dog2.species)

print(my_dog.name)
print(my_dog2.name)

print(my_dog2.get_profile())
