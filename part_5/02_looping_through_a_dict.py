# Looping through dictionary

menu = {
    "tea": 50,
    "coffee": 100,
    "black_coffee": 150
}
fav_colors = {
    'batman': "black",
    'superman': "blue",
    'flash': "red",
    'wonder_woman': "red",
    'green_lantern': "green",
    'aquaman': "orange"
}


# print(fav_colors)

fav_colors_list = fav_colors.items()
print(fav_colors_list)

for key, value in fav_colors_list:
    print(f"{key.title()}'s favourite color is {value.title()}")

fav_colors_keys = fav_colors.keys()
fav_colors_values = fav_colors.values()

for key in fav_colors_keys:
    print(f"{key.title()}")

# set()
for color in set(fav_colors_values):
    print(f"{color}")

















