try:
    bill = round(float(input("What was the total bill? $")))
    tip = round(float(input("What percentage tip would you like to give? ")))
    people = int(input("How many people to split the bill? "))
except ValueError:
    print("Please enter a number only")
else:
    tip_calc = round(bill*tip/100)
    total = bill+tip
    total_per_diner = (total/people)
    print(f"You'r Bill is {bill}$")
    print(f"With {tip}% tip.")
    print(f"That is {tip_calc}$ for tip")
    print(
        f"Split bettwen {people}. Divided among all the diners, each one will pay: {total_per_diner}$")
