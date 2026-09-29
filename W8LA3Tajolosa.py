tajolosa_Name = input("Enter your name: ")
tajolosa_Month= int(input("Enter month number: "))
tajolosa_NameUp = tajolosa_Name.title()
print(f"\nName: {tajolosa_NameUp}")
if tajolosa_Month>=1 and tajolosa_Month<=3:
    print("Travel Season:\nRainy = Not a good month to travel due to flooding in many areas. This weather is not recommended.")
elif tajolosa_Month>=4 and tajolosa_Month<=5:
    print("Travel Season:\nSummer = A good time to travel. You can enjoy the warm weather while visiting sights.")
elif tajolosa_Month>=6 and tajolosa_Month<= 8:
    print("Travel Season:\nMixed Weather Condition = Typhoon may come and the country may experience typhoon or good weather.")
elif tajolosa_Month>=9 and tajolosa_Month<= 12:
    print("Travel Season:\nChristmas Vibe = Still a mixed weather but mostly sunny and cold breeze. Stores and tourist destinations offer a lot of discounts.")
else:
    print("Invalid. Please input a number from 1 to 12 only.")

