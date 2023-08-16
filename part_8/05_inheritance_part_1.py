# Inheritance

# Parent class ---> Child class

# Parent Class
class Dog:
    """A class to represent a general dog"""

    def __init__(self, name, gender, age, loud):
        """Initialize attributes"""
        self.name = name.title()
        self.gender = gender
        self.age = age
        self.is_loud = loud  # Loud is Bool

    def call_dog(self):
        """Call the dog"""
        if self.gender == 'male':
            print(f"Here {self.name}! Good Boy!")
        else:
            print(f"Here {self.name}! Good Girl!")

    def dog_years(self):
        """Compute age in dog years"""
        dog_years = self.age * 7
        print(f"{self.name} is {dog_years} years old in dog years.")

    def bark(self):
        """Get the dog to speak"""
        if self.is_loud:
            print("Woof Woof Woof Woof")
        else:
            print("wof")


class Husky(Dog):
    """A class to represent a specific dog type"""

    def __init__(self, name, gender, age, loud, gunshy):
        """Initialization attributes of parent class"""
        super().__init__(name, gender, age, loud)
        self.gunshy = gunshy  # bool

    def bark(self):
        """Get the dog to speak"""
        if self.is_loud:
            print("HOOOOOOWWWWWWLLLLLLLLLLLLLL")
        else:
            print("howl")

    def go_hunt(self):
        """If the dog is not gunshy, take them hunting"""
        if not self.gunshy:
            self.bark()
            print(f"{self.name} just brought back a duck.")
        else:
            print(f"{self.name} is not a good hunting dog.")


class Chihuahua(Dog):
    """Represents a specific dog"""

    def __init__(self, name, gender, age, loud):
        """Initialization attributes of parent class"""
        super().__init__(name, gender, age, loud)

    def bark(self):
        """Get the dog to speak"""
        if self.is_loud:
            print("YIP YIP YIP YIP YIP")
        else:
            print("yip")


my_dog = Dog('spot', 'male', 3, True)
print(my_dog.name)
print(my_dog.age)

my_dog.call_dog()
my_dog.dog_years()
my_dog.bark()

your_dog = Husky('tess', 'female', 8, True, False)

print(type(my_dog))
print(type(your_dog))

your_dog.call_dog()
your_dog.dog_years()
your_dog.bark()

your_dog.go_hunt()


tiny_dog = Chihuahua('tiny', 'male', 2, True)
tiny_dog.bark()
