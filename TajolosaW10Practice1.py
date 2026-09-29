# THIS IS "SET A" OF THE PRACTICES

while True:
    print("------HALF-MONTH PAYROLL SYSTEM------")
    Tajolosa_Name = input("Enter the Employee's Name: ").title()
    Tajolosa_Job = input("Enter Job Position (Janitor | Clerk | Cashier | Manager): ").title()
    Tajolosa_HoursWorked = int(input("Enter Hours Worked: "))
    Tajolosa_OT = 0
    Tajolosa_MS = 0

    match (Tajolosa_Job):
        case "Janitor":
            Tajolosa_MS = 18000
        case "Clerk":
            Tajolosa_MS = 22000
        case "Cashier":
            Tajolosa_MS = 24000
        case "Manager":
            Tajolosa_MS = 40000
        case _:
            print("This position is invalid.")
    Tajolosa_BasicHM = Tajolosa_MS / 2
    Tajolosa_HourlyRate = Tajolosa_BasicHM / 88

    if Tajolosa_HoursWorked < 88:
        Tajolosa_AbsentHours = 88 - Tajolosa_HoursWorked
        Tajolosa_AbsentDeduc = Tajolosa_AbsentHours * Tajolosa_HourlyRate
        Tajolosa_OT = 0
    else:
        Tajolosa_OT = Tajolosa_HoursWorked - 88
        Tajolosa_AbsentDeduc = 0
        Tajolosa_AbsentHours = 0

    Tajolosa_OTRate = Tajolosa_HourlyRate * 1.25
    Tajolosa_OTPay = Tajolosa_OT * Tajolosa_OTRate
    Tajolosa_NetSalary = Tajolosa_BasicHM - Tajolosa_AbsentDeduc + Tajolosa_OTPay
    if Tajolosa_MS != 0 and Tajolosa_HoursWorked != 0:
        print("\n------EMPLOYEE PROFILE------\nEmployee's Name: ", Tajolosa_Name)
        print("Job Position: ", Tajolosa_Job, "\nActual Hours Worked: ", Tajolosa_HoursWorked)
        print("Monthly Salary: ", Tajolosa_MS, "\nBasic Half Month Salary: ", Tajolosa_BasicHM)
        print(f"Hourly Rate: {Tajolosa_HourlyRate:.2f}")
        print("Absent hours: ", Tajolosa_AbsentHours, f"\nAbsent Deduction: {Tajolosa_AbsentDeduc:,.2f}", )
        print("Overtime Hours: ", Tajolosa_OT, f"\nOvertime Pay: {Tajolosa_OTPay:,.2f}")
        print(f"Net Salary: {Tajolosa_NetSalary:,.2f}")
    else:
        print("---CANNOT PROCESS---")
        break

    again = input("\nWould you like to process again? (Y | N): ").upper()
    if again != "Y":
        print("--------\nThank you for using the System!")
        break