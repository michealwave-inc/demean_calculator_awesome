import math
print("Welcome to the demean calculator. This has only 10 lines of code")
while True:
    demean_number = float(input("enter a number, 15 is the gold standard and is also the highest you can put in: "))

    print("Your rounded value (since plane crazy only supports down to thousandths) is", round(demean_number * math.pi, 3), "and your non rounded value is", (demean_number * math.pi))

    again = input("Would you like to try another number? (n for no, enter for yes): ")
    if again == "n":
        break