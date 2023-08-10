# Basic Data Types Challenge 5: Multiplication/Exponent Table Program

print("Welcome to the Multiplication/Exponent Table Program")

# Gather user input
name = input("\nHello, what is your name: ").title().strip()
num = float(input("What number would you like to work with: "))
message = f"{name}, Math is cool!"

# Multiplication table
print("\nMultiplication Table For " + str(num))
print(f"\t 1.0 * {num} = {round(1 * num, 4)}")
print(f"\t 2.0 * {num} = {round(2 * num, 4)}")
print(f"\t 3.0 * {num} = {round(3 * num, 4)}")
print(f"\t 4.0 * {num} = {round(4 * num, 4)}")
print(f"\t 5.0 * {num} = {round(5 * num, 4)}")
print(f"\t 6.0 * {num} = {round(6 * num, 4)}")
print(f"\t 7.0 * {num} = {round(7 * num, 4)}")
print(f"\t 8.0 * {num} = {round(8 * num, 4)}")
print(f"\t 9.0 * {num} = {round(9 * num, 4)}")

print(f"\n\t 1.0 * {num} = {round(1 * num, 4)}")
print(f"\t 2.0 * {num} = {round(2 * num, 4)}")
print(f"\t 3.0 * {num} = {round(3 * num, 4)}")
print(f"\t 4.0 * {num} = {round(4 * num, 4)}")
print(f"\t 5.0 * {num} = {round(5 * num, 4)}")
print(f"\t 6.0 * {num} = {round(6 * num, 4)}")
print(f"\t 7.0 * {num} = {round(7 * num, 4)}")
print(f"\t 8.0 * {num} = {round(8 * num, 4)}")
print(f"\t 9.0 * {num} = {round(9 * num, 4)}")

# Exponent table
print("\nExponent Table For " + str(num))
print(f"\t{num} ** 1 = {round(num ** 1, 4)}")
print(f"\t{num} ** 2 = {round(num ** 2, 4)}")
print(f"\t{num} ** 3 = {round(num ** 3, 4)}")
print(f"\t{num} ** 4 = {round(num ** 4, 4)}")
print(f"\t{num} ** 5 = {round(num ** 5, 4)}")
print(f"\t{num} ** 6 = {round(num ** 6, 4)}")
print(f"\t{num} ** 7 = {round(num ** 7, 4)}")
print(f"\t{num} ** 8 = {round(num ** 8, 4)}")
print(f"\t{num} ** 9 = {round(num ** 9, 4)}")


# Math is cool!
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())
