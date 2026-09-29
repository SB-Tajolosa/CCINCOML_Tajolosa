print("----------CLASS RECORD SUMMARY PROGRAM----------")
#This is where I establish the classrecord Dictionary
Tajolosa_classrecord = {
    "Liza" : {
        "StudID" : "5001",
        "Grade" : [90, 85, 86, 82, 83, 90, 92]
    },
    "Jeremy" : {
        "StudID" : "5002",
        "Grade" : [72, 75, 69, 80, 84, 75, 85]
    },
    "Bini" : {
        "StudID" : "5003",
        "Grade" : [72, 59, 69, 80, 51, 65, 100]
    },
    "Adrian" : {
        "StudID" : "5004",
        "Grade" : [70, 75, 89, 82, 90, 97, 50]
    }
}
#This line of code below asks the user for input to search for a certain student
Tajolosa_search = input("Enter Student Name to Search: ").title()

#This is where we can access the keys and values inside of the dictionary.
for Tajolosa_student, Tajolosa_details in Tajolosa_classrecord.items():
    if Tajolosa_student == Tajolosa_search:
        print("Student Found!")
        print("\n----Grades SUMMARY----")

        #I made a variable to hold the values inside of the 'Grade' key
        Tajolosa_grades = Tajolosa_details["Grade"]
        print("Grades: ", *Tajolosa_grades)
        Tajolosa_average = sum(Tajolosa_grades) / len(Tajolosa_grades)

        #Most computations are here, finding the average, highest, lowest, and if there are any grades below 60- for students for intervention
        print(f"Average: {Tajolosa_average:.2f}")
        print("Highest Grade: ", max(Tajolosa_grades))
        print("Lowest Grade: ", min(Tajolosa_grades))
        if min(Tajolosa_grades) < 60:
            print("This Student is Candidate for Intervention.")
        break
else:
    print("Student Not found!")