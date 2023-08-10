# Looping through lists of elements

# teams = ["India", "Aus", "Pak"]
# print(teams)

# print(teams[0].title())
# print(teams[1].title())
# print(teams[2].title())

# for each_team in teams:
#     print(each_team)
#     print("You are going to win!")
#
# print("Go Cricket!")

# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total_sum = 0
#
# for each_value in values:
#     total_sum += each_value
#
# print(total_sum)

triples = [["a", "b", "c"], ["1", "2", "3"], ["do", "re", "mi"], [10, 20, 30, 40, 50, 60, 00000]]
print(triples)


for list_value in triples:
    for element in list_value:
        print(element, end=" ")
    print("I just finished one of the inner loops.")

print("Now I'm out of all the loops.")
