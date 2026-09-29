while True:
    print("\n---GRADE SHEET SEARCHER---\nInstructions: input the student's final letter grades, check if there is a failed grade.\nexample: Student's grade: AABBFC")
    Tajolosa_grade = input("\nEnter the student's Grade: ").upper()
    Tajolosa_search = input("Enter the grade category you want to search: ").upper()
    Tajolosa_found = False

    for Tajolosa_char in Tajolosa_grade:
        if Tajolosa_char == Tajolosa_search:
            Tajolosa_found = True
            break

    if Tajolosa_found:
        print("Grade Category found!: ", Tajolosa_char)
    else:
        print("No particular grade seen in this Batch.")

    Tajolosa_again = input("\nWould you like to try again? (Y | N): ").upper()
    if Tajolosa_again != "Y":
        print("Process ended")
        break