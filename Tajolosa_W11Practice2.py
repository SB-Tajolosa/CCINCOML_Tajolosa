
# TUPLE Practice
#Tuple uses parentheses

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

for x in months:
    print(x)

print("\n")
for i in days:
    print(i)

print("")

#HYBRID OF TUPLE AND LIST
MachineLearning = [('Supervised', 'Decision Tree'), ('Supervised', 'Random Forest'), ('Unsupervised', 'K-Means'), ('Unsupervised', 'Gaussian Mixture Mode')]
#4 tuples , 8 list items
#print("Learning Type:" , MachineLearning[3][1])
# MachineLearning[tuple][which element in the list]

for i in MachineLearning:
    if i[0]=="Supervised":
        print(i[1])
    elif i[0] == "Unsupervised":
        print(i[1])
    else:
        print("Not in the list")



