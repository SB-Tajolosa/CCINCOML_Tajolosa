tajolosa_name = input("Enter student's Name: ")
tajolosa_grade = int(input("Enter the grade: "))

print("------\nStudent's Name: ", tajolosa_name)
match tajolosa_grade:
    case n if 90 <= n <= 100:
        print("Excellent!")
    case n if 80 <= n <= 89:
        print("Very Good!")
    case n if 75 <= n <= 79:
        print("Passed!")
    case n if 0 <= n <= 74:
        print("Failed!")
    case _:
        print("Invalid grade.")