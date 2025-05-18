bill=int(input("Enter the bill amount: "))
number_of_people=int(input("Enter the number of people: "))
tip=int(input("Enter the tip percentage: "))
total_bill=bill+(bill*tip/100)
total=total_bill/number_of_people
print(f"total bill is {total_bill} and each person has to pay {total}")