#HYBRID OF TUPLE AND LIST
MachineLearning = [('Supervised', 'Decision Tree'), ('Supervised', 'Random Forest'), ('Unsupervised', 'K-Means'), ('Unsupervised', 'Gaussian Mixture Mode')]

for LT in ['Supervised', 'Unsupervised']:
    print("\nLearning Type: ", LT)

    for i in MachineLearning:
        if i[0]==LT:
            print(i[1])

