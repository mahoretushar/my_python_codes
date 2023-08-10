# Nested if Statements

our_list = [1, 2, 3]
our_string = "Bats"

if our_list:
    print("Our list is not empty!")

if our_string:
    print("Our string is not empty.")


teams = ["Isa", "India", "Aus", "Pak", "SA"]
for team in teams:
    if team.startswith('I'):
        print(f"This team {team} could win the World Cup.")
        if team == "India":
            print("India will win.")
        else:
            print(f"The team {team} will not win the World Cup.")
    elif team.startswith('A'):
        print(f"The team {team} will probably make it to the semi-finals.")
        if team == "Aus":
            print(f"They need Brett Lee Back")
    else:
        print(f"The team {team} will not win the world cup.")





