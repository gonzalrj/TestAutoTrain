class Animal:
    def speak(self):
        return "Some generic animal sound"


class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # <-- Method overriding
        return "Woof!"


class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):  # <-- Method overriding
        return "Meow!"


class Duck:
    # Duck does NOT inherit from Animal, but it still has speak()
    def speak(self):
        return "Quack!"


def make_it_speak(animal):
    # Duck typing: we don’t care if it’s Animal, Dog, Cat, or Duck
    print(animal.speak())


# -------------------
# Method overriding demo
generic = Animal()
dog = Dog()
cat = Cat()

print(generic.speak())  # Some generic animal sound
print(dog.speak())  # Woof!  (overrides Animal.speak)
print(cat.speak())  # Meow!  (overrides Animal.speak)

# -------------------
# Duck typing demo
duck = Duck()
make_it_speak(dog)  # Woof!
make_it_speak(cat)  # Meow!
make_it_speak(duck)  # Quack! (works even without inheritance!)
