while True:
    Tajolosa_word = input("Enter a Word: ").lower()
    Tajolosa_letter = input("Enter a letter to search: ").lower()
    found = False

    for Tajolosa_character in Tajolosa_word:
        if Tajolosa_character == Tajolosa_letter:
            found = True
            break

    if found:
        print("The Character is found!: ", Tajolosa_letter)
        break
    else:
        print("Not found.")

    Tajolosa_again = input("Would you like to try again? (y | n): ").lower()

    if Tajolosa_again != "y":
        print("ended")
        break