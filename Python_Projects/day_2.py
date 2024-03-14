# Tip Calculator
def tip_calculator(total_bill,tip_percentage,split):
    res = (total_bill / split) * (tip_percentage / 100)
    return res
print("Welcome to the Tip Calculator !!")
total_bill = float(input("What was the total bill ?"))
tip_percentage = int(input("What percentage tip would you like to give ? 10,12 or 15 ?"))
split = int(input("How many people to split the bill?"))

print(f"Each Person Should Pay : Rs:{tip_calculator(total_bill,tip_percentage,split):.2f}")
