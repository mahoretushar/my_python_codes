# Sorting Lists

sports = ["basketball", "football", "tennis", "chess"]
print(sports)
print(sorted(sports))

grades = [50, 34, 55, 89, 45, 66]
print(grades)
print(sorted(grades))
print(sorted(grades, reverse=True))
print(grades)

grade_length = len(grades)
print(grade_length)
print(type(grade_length))

removed_grade = grades.pop()
print(f"Removing {removed_grade} from {grades}.")
print(len(grades))

print(sports)
sports.sort(reverse=True)
print(sports)

print(grades)
grades.reverse()
print(grades)
