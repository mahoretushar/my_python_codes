# Adding elements to lists

colors = ["red", "green", "blue"]
print(colors)
print(colors[2])
print(colors[-1])

colors[2] = "yellow"
print(colors)

# colors[3] = "black"
colors.append("black")
print(colors)

new_colors = []
new_colors.append("red")
new_colors.append("white")
new_colors.append("green")
print(new_colors)


print(new_colors[1])
new_colors.insert(1, "orange")
print(new_colors)
