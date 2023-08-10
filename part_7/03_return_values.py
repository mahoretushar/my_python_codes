def calc_age(age=0, interval=0):
    """Calculate a persons age in interval years"""
    print(f"You are currently {age} years old.")
    age += interval
    return age


new_age = calc_age(10, 6)
print(new_age)
