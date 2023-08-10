# 1. Letter Counter App

print("Welcome to the Letter Counter App")

# Get User Input
name = input("\nWhat is your name: ").title().strip()
print(f"Hello, {name}!")

print("I will count the number of times that a specific letter occurs in a message.")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurrence of: ")

# Convert to lower case
message = message.lower()
letter = letter.lower()

# Get the count and display
letter_count = message.count(letter)
print(f"\n{name}, your message has {letter_count} {letter}'s in it.")
