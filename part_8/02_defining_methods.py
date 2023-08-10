# Creating a Class
import random


# Class         ---> Blueprint to build something
# Object        ---> What you build
# Instance      ---> What you work with once it is built
# Attributes    ---> Information used to distinguish one instance from another in a class
# Method        ---> Behavior common to all instances of a class (functions)

class Baby:
    """A simple class to simulate a baby"""

    def __init__(self, name, gender, age):
        """Initialization attributes"""
        self.name = name
        self.gender = gender
        self.age = age

        self.tired = True

    def play(self):
        """Simulate playing based on gender"""
        if self.gender == "male":
            print(f"{self.name} is playing with cars.")
        else:
            print(f"{self.name} is playing with puzzles.")

    def cry(self):
        """Simulate crying"""
        print("Waaahhhhhhhhhh......")
        print(f"Even {self.age} year old cry.")

    def sleep(self):
        """Simulating Sleep"""
        if self.tired:
            print(f"{self.name} is sleeping finally.")
            self.tired = False
        else:
            print(f"Sorry {self.name} isn't tired.")


little_boy = Baby("supelman", "male", 2)
little_girl = Baby("diana", "female", 1)

print(f"{little_boy.name} is a {little_boy.age} year old {little_boy.gender}.")
print(f"{little_girl.name} is a {little_girl.age} year old {little_girl.gender}.")

little_boy.play()
little_girl.play()

little_boy.cry()
little_girl.cry()

little_boy.sleep()
little_girl.sleep()
little_girl.sleep()
little_girl.tired = True
little_girl.sleep()

babies = []
for i in range(25):

    num = random.randint(0, 1)
    if num == 0:
        gender = 'male'
    else:
        gender = 'female'

    age = random.randint(0, 5)

    baby = Baby("flash", gender, age)
    babies.append(baby)

for baby in babies:
    print(f"{baby.name} is a {baby.age} year old {baby.gender}.")







