#inputs
Basic_salary = 1500
Comm_rate = 0.02
Number_of_laptops = int()
Bonus_rate = 200
commission = float()
Price_of_laptop = float(input("Price of the laptop/s: "))
#processes
while Price_of_laptop <= 500.00:
    print("Laptop price too low!")
    Price_of_laptop = float(input("Price of the laptop/s: "))
else:
    Number_of_laptops = int(input("Number of laptops were sold: "))
    commission = Comm_rate * Number_of_laptops * Price_of_laptop
bonus = Bonus_rate * Number_of_laptops
Gross_salary = Basic_salary + bonus + commission
#output
print("Bonus: R", bonus)
print("Commission: R", commission)
print("Gross salary: R", Gross_salary)


