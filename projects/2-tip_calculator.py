print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill ? $"))
tip_percent = int(input("How much % of tip would you like to give ? 5,7,9 : "))
no_of_people = int(input("How many people to split the bill ?"))
total_bill = bill*(tip_percent/100) + bill
bill_per_person = round(total_bill/no_of_people,2)
print(f"Each person should pay: ${bill_per_person}")