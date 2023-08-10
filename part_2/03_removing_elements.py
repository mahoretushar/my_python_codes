# Removing elements from lists

colors = ["red", "blue", "green", "blue"]
print(colors)

# colors.remove("green")
# print(colors)

# colors.remove("blue")
# print(colors)
#
# new_colors = ["red", "green", "blue", "black", "white", "yellow"]
# removed_element = new_colors.pop()
# print(f"Removing {removed_element} form {new_colors}")
#
# bad_color = new_colors.pop(1)
# print(f"A bad color is {bad_color} form {new_colors}")

print(colors)
del colors[0]
print(colors)

fruits = []
fruits.append(input("Enter a fruit: "))
fruits.append(input("Enter a fruit: "))
fruits.append(input("Enter a fruit: "))
print(fruits)
