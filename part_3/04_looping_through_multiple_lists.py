# Looping through multiple lists

names = ["Batman", "Superman", "Flash", "Wonder Woman"]
ages = [45, 100, 23, 300]

# for name in names:
#     print(name)
#
# for age in ages:
#     print(age)

# for i in range(len(names)):
#     print(f"{names[i]} is {ages[i]} years old.")

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# tu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# a, b, *c = tu
#
# print(f"{a} {b} {c}")
