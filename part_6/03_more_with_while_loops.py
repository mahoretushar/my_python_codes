# names = []
# print(names)
# print(bool(names))
#
# # while names:
# #     print("This is a list")
#
# names.append("Batman")
# print(names)
# print(bool(names))
#
# print(0)
# print(bool(0))
# print(1)
# print(bool(1))
# print(2)
# print(bool(2))
#
# numbers = list(range(1, 11))
# print(numbers)
#
# while numbers:
#     numbers.pop()
#     print(numbers)
#
# print("All elements are Removed......")


# Q --> Find multiplication table of numbers from 1 to 10
# Q --> Find multiplication table of numbers starting from 1 until user enters exit

flag1 = True
flag2 = True

while flag1:
    print("While loop #1 is running....")
    while flag2:
        choice = input("Continue running while loop #2 (y/n): ")
        if choice.lower() == 'n':
            flag2 = False
            print("Ending while loop #2....")
    choice = input("Continue running while loop #1 (y/n): ")
    flag2 = True
    if choice.lower() == 'n':
        flag1 = False
        print("Ending while loop #1....")
