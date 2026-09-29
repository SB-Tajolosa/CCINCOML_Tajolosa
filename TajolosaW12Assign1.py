
patients = {
    "ana" : [80, 50, 150, 90, 140, 200, 100],
    "ben" : [130, 140, 135, 90, 140, 180, 70],
    "carlo" : [90, 100, 95, 90, 140, 97, 80]
}


for name, reading in patients.items():
    count = 0
    average = 0
    print("\nPatient: ", name)
    print("Blood Sugar Summary:")
    for r in reading:
        average = sum(reading) / len(reading)
        if r > 120:
            print(r, "- High")
            count = count + 1
        else:
            print(r, "- Normal")
    print("\nNumber of High Readings: ", count)
    print("Lowest Reading: ", min(reading), " - ", name)
    print("Highest Reading: ", max(reading), " - ", name)
    print("Difference: ", max(reading) - min(reading))
    print(f"Average: {average:.2f}", "\n----------")



