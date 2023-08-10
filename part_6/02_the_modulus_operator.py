# current_num = 1
# while current_num <= 10:
#     if current_num % 2 == 0:
#         print(f"{current_num} is even!")
#     else:
#         print(f"{current_num} is odd!")
#     current_num += 1


current_num = 1
playing = True
while playing:
    if current_num % 3 == 0:
        print(f"{current_num} is divisible by 3!")
    else:
        print(f"{current_num} is not divisible by 3!")

    choice = input("Enter 'n' to stop or press enter to continue.")
    if choice.lower() == 'n':
        playing = False

    current_num += 1
