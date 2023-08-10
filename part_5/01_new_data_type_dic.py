# Dictionaries

# list() --> []
# tuple() --> ()

batman_info = {
    'first_name': "Bruce",
    'last_name': "Wayne",
    'age': 32,
    'weight': 80.5,
    'villains_defeated': ["Joker", "Bane", "Riddler"],
    'nickname': "The Dark Knight"
}

print(batman_info)
print(type(batman_info))

print(batman_info['first_name'])
print(batman_info['villains_defeated'][0])

batman_info['age'] = 35
batman_info['weight'] = 81.5

print(batman_info)

batman_info['weight'] -= 1
print(f"Wow, Batman lost weight! He now weighs {batman_info['weight']} kg.")

del batman_info['nickname']
print(batman_info)

batman_info['villains_defeated'].append("Penguin")
print(f"Batman has defeated {batman_info['villains_defeated']}.")

super_hero_info = {}

super_hero_info['first_name'] = input("Enter first name of your superhero: ").title()
super_hero_info['last_name'] = input("Enter last name of your superhero: ").title()
super_hero_info['age'] = int(input("Enter age of your superhero: "))
super_hero_info['villains_defeated'] = list(input("Enter villains defeated by your superhero (separated by comma): ").title().split(","))

print(super_hero_info)























