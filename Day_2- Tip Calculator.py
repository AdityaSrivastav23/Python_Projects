# Hotel Tip Calculator


print("Welcome TO The Tip Calculator")
bill = float(input("What is The Normal Bill?\n ₹"))
tip = int(input("What % tip would you like to give? 10,12 or 15?\n"))
people = int(input("How Many people to split the bill?\n"))
Total_bill = (bill+(0.12*bill))
Grand_total =(Total_bill/people)
bill_perhead=round(Grand_total,2)

print(f"Your Total Bill is\n₹{Total_bill}\nYour Grand Total Per Head is\n₹{bill_perhead}")
