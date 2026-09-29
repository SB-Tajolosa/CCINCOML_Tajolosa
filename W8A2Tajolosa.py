"""This program is a GROCERY CHECK OUT SYSTEM. It lets the user input five products and their prices.
 Next, it calculates the cost of the items and gives the total. Then the user is allowed to input the amount of cash they will pay.
 It will subtract the cash with the cost and prints the grocery receipt and change."""

print()
print("----GROCERY CHECK OUT----")
print("Welcome! Input your grocery items...")
tajolosa_Prod1 = input("Enter first product: ")
tajolosa_Price1 = float(input("Enter the price of the first product: ₱"))

tajolosa_Prod2 = input("Enter second product: ")
tajolosa_Price2 = float(input("Enter the price of the second product: ₱"))

tajolosa_Prod3 = input("Enter third product: ")
tajolosa_Price3 = float(input("Enter the price of the third product: ₱"))

tajolosa_Prod4 = input("Enter fourth product: ")
tajolosa_Price4 = float(input("Enter the price of the fourth product: ₱"))

tajolosa_Prod5 = input("Enter fifth product: ")
tajolosa_Price5 = float(input("Enter the price of the fifth product: ₱"))

tajolosa_Cost = tajolosa_Price1 + tajolosa_Price2 + tajolosa_Price3 + tajolosa_Price4 + tajolosa_Price5

print()
print("TOTAL---")
print("Your total is: ₱",tajolosa_Cost)
tajolosa_Cash = float(input("Enter the amount of Money you will pay: "))
tajolosa_Change = tajolosa_Cash - tajolosa_Cost

print()
print("---------GROCERY RECEIPT---------")
print("Store #123")
print("Philippines, Davao City")
print("---")
print(tajolosa_Prod1, "        ", tajolosa_Price1)
print(tajolosa_Prod2, "        ", tajolosa_Price2)
print(tajolosa_Prod3, "        ", tajolosa_Price3)
print(tajolosa_Prod4, "        ", tajolosa_Price4)
print(tajolosa_Prod5, "        ", tajolosa_Price5)
print()
print("TOTAL: ", tajolosa_Cost)
print("AMOUNT PAID: ", tajolosa_Cash)
print("CHANGE: ", tajolosa_Change)
print("---")

print()
print("   Thank you for Shopping!   ")