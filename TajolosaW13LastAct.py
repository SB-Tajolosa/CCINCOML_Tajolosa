Tajolosa_Employee = {
    "E100" : {"Name" : "Llane Uy","Rank" : "JO S","DutyHours" : (42, 43, 40,30),"Basicpay" : 29000,"RequiredHrs" : 160},
    "E105" : {"Name" : "Robert Santos","Rank" : "Manager 1","DutyHours" : (30, 35, 31, 30),"Basicpay" : 60000,"RequiredHrs" : 120},
    "E110" : {"Name" : "Bryan","Rank" : "Manager 2","DutyHours" : (20, 30, 31, 30),"Basicpay" : 60000,"RequiredHrs" : 120}
}

Tajolosa_Search = input("Search for employee with employeeID: ").title()

for Tajolosa_ID, Tajolosa_Details in Tajolosa_Employee.items():
    if Tajolosa_ID == Tajolosa_Search:
        print("Employee Found!")
        Tajolosa_Exceeding = 0
        Tajolosa_Basicpay = Tajolosa_Details["Basicpay"]
        Tajolosa_RequiredHrs = Tajolosa_Details["RequiredHrs"]
        Tajolosa_DH = Tajolosa_Details["DutyHours"]
        Tajolosa_CombDH = sum(Tajolosa_DH)
        print("\nEmployees ID: ", Tajolosa_ID)
        print("Employees Name: ", Tajolosa_Details["Name"], "\nEmployees Job Rank: ", Tajolosa_Details["Rank"], "\nEmployees Duty Hours: ", *Tajolosa_DH)
        print("Employees Basic Pay: ", Tajolosa_Details["Basicpay"], "\nEmployees Required Hours: ", Tajolosa_Details["RequiredHrs"], "\nEmployees Total Duty Hours: ", Tajolosa_CombDH)
        Tajolosa_Rate = Tajolosa_Basicpay / Tajolosa_RequiredHrs

        if Tajolosa_CombDH > Tajolosa_RequiredHrs:
            Tajolosa_Exceeding = Tajolosa_CombDH - Tajolosa_RequiredHrs
            print("Employees Excess Hours: ", Tajolosa_Exceeding)
        else:
            print("Employees Excess Hours: ", Tajolosa_Exceeding)
        print("Rate Per Hour: ", Tajolosa_Rate)

        Tajolosa_Overtime = Tajolosa_Rate * 1.5 * Tajolosa_Exceeding
        Tajolosa_Gross = Tajolosa_Basicpay + Tajolosa_Overtime
        print("Overtime: ", Tajolosa_Overtime)
        print("Gross Pay: ", Tajolosa_Gross)
        break
else:
    print("Employee Not Found")