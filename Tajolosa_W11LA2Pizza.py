# UNFINISHED!!!

print("--------PIZZA ORDERING SYSTEM-------")
Tajolosa_Pizza = [('Margherita', 'small', 300), ('Margherita', 'medium', 500), ('Margherita', 'large', 900),
                  ('Veggie', 'small', 360), ('Veggie', 'medium', 540), ('Veggie', 'large', 800)]

tajolosa_customer = input("Enter Customer Name: ").title()
print("\nWelcome!", tajolosa_customer)

tajolosa_flavor = input("Enter the pizza flavor (Veggie/Margherita): ").title()
for flavor in ['Margherita', 'Veggie']:
    for order in Tajolosa_Pizza:
        if flavor == tajolosa_flavor:
            print(flavor)

Tajolosa_flavor = ('Veggie', 'Margherita')
