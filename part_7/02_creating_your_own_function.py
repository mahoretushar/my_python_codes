def hello_world(name, age):
    """Greet a user and repeat their age"""
    print(f"Hello {name}!")
    print(f"You are {age} years old.")


hello_world("Ben", 44)

stu_name = "Bats"
stu_age = 55

hello_world(stu_name, stu_age)


def goodbye_world(name="nobody", day="today"):
    """Say goodbye to a person and wish them a good day"""
    print(f"Goodbye {name.title()}....")
    print(f"May you have a good {day.title()}.")


goodbye_world()
goodbye_world("Bats")
goodbye_world("Bats", "Saturday")
goodbye_world("Saturday")
goodbye_world(day="Saturday")
