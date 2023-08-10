# Creating a Class

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
        pass

    def cry(self):
        pass

    def sleep(self):
        pass


little_boy = Baby("supelman", "male", 2)
little_girl = Baby("diana", "female", 1)

print(little_boy.name)
print(little_girl.name)

print(little_boy.gender)
print(little_girl.play())

