print("Welcome to Tip Calculator!")

total_bill = float(input('What wa the total bill?  $'))
tip_percentege = int(input("How much tip would you like to give? 10, 15, or 20? "))
people = int(input("How many people are splitting this bill?"))

bill_with_tip = tip_percentege / 100 * total_bill + total_bill
bill_per_person = bill_with_tip / people
final_bill = round(bill_per_person, 2)

print(f"Each person has to pay: {final_bill} $")



