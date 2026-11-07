print("Welcome to the tip calculator!")

bill_cost = float(input("Enter the total bill: ₹"))
tip_percent = int(input ("Enter the percentage of tip (10%, 12%, 15%): "))
people = int(input("Enter the number of people: "))

result = (bill_cost + (tip_percent/100)*(bill_cost))/people

print(f"Each person should pay ₹{round(result,2)}")