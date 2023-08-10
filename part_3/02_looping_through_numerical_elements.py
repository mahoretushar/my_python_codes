# Looping through numerical elements

# values = range(1, 11)   # iter
# print(values)
# print(type(values))

# range(5) --> 0, 1, 2, 3, 4
# range(1, 6) --> 1, 2, 3, 4, 5
# range(2, 11, 2) --> 2, 4, 6, 8, 10

# for i in range(1, 11):
#     print(i)
#
# for num in range(5):
#     print(num)

# range(start, stop, step)
# for i in range(0, 101, 5):
#     print(i, end=" ")
#
# print()
#
# word = "Hello World!"
# list_word = list(word)
# print(list_word)
#
# # list_word[5] = "New"
# # print(list_word)
#
# new_word = "".join(list_word)
# print(new_word)

numbers = list(range(10, 101, 10))
# print(numbers)
#
# for num in numbers:
#     print(num)
#
# squares = []
# for num in numbers:
#     sq = num ** 2
#     squares.append(sq)
#
# print("Populating squares list Complete!")
# for square in squares:
#     print(square)
#


cubes = [num**3 for num in numbers]
for cube in cubes:
    print(cube)

print()

print(min(cubes))
print(max(cubes))
print(sum(cubes))

list1 = ["a", "b", "c"]
print(min(list1))

