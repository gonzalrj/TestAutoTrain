# Single Inheritance
class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print(f"Labrador woofs")

    def display_new_name(self, new_name):
        print("Old Name:")
        super().display_name()  # Parent class is also called Super class
        print(f"New Name:\nDog's Name: {new_name}")


# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        txt = self.species
        print(f"{self.name}Guides the way!")


# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")


class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")


# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()
lab.display_new_name("Heads")

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()
