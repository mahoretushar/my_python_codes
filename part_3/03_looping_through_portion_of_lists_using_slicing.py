# Looping through portion of lists using slicing

# indexing and slicing

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = list(range(1, 101))

numbers = list(range(1, 11))
# print(numbers)
# for num in numbers:
#     print(num)

# print("\nSlicing the first 5 numbers.")
# print(numbers[0:5])
# for num in numbers[0:5]:
#     print(num)
#
# print("\nSlicing the last 5 numbers.")
# print(numbers[5:])
# for num in numbers[5:]:
#     print(num)
#
# print("\nSlicing the middle 5 numbers.")
# print(numbers[3:8])
# for num in numbers[3:8]:
#     print(num)

# new_numbers = numbers
# print(new_numbers)
# print(numbers)
#
# new_numbers.pop()
# print(new_numbers)
# print(numbers)
#
# new_numbers = numbers[:]
# print(new_numbers)
# print(numbers)
#
# new_numbers.pop()
# print(new_numbers)
# print(numbers)

names = ["Batman", "Superman", "Flash", "Wonder Woman"]
new_names = names.copy()
print(names)
print(new_names)

new_names[0] = "Iron Man"
print(names)
print(new_names)




