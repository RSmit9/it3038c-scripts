import datetime
now = datetime.datetime.now()

print ("Monthly budget creator", now.month,'/',now.year)
print ("please input data when prompted")
AverageMonthlyIncome = int(3000)




SpendingAccount= int(input("Current Spending Account Balance: "))
SavingAccount= int(input("Current Saving Account Balance: "))

Rent= int(input("Rent($ Amount): "))
PowerGas= int(input("Power/Gas($ Amount): "))
Water= int(input("water($ Amount): "))
Wifi = int(input(" wifi: "))
Groceries= int(input("groceries ($ Amount): "))
CC= int(input("Credit Card($ Amount): "))
MiscExpenses= int(input("Other expenses this month($ Amount): "))

Bills = Rent + PowerGas + Water + Wifi + Groceries + CC
TotalMonthlyCost= MiscExpenses + Bills

if AverageMonthlyIncome <= TotalMonthlyCost:
        print ("You spent more than your earned this month and chipped into your savings")


SpendingAccount = AverageMonthlyIncome * .2 + SpendingAccount
AverageMonthlyIncome = AverageMonthlyIncome * .8
SavingAccount = SavingAccount + AverageMonthlyIncome
SavingAccount = SavingAccount - TotalMonthlyCost



print("Your spending account total is", SpendingAccount)
print ("Your Savings account total is", SavingAccount)


filename = f"Month Budget_{now.month}_{now.year}.txt"
with open(filename, "w") as file:
        file.write(f"total costs of month: {TotalMonthlyCost}\n")
        file.write(f"Spending account total: {SpendingAccount}\n" )
        file.write(f"Savings account total: {SavingAccount}\n" )
print("The budget information has been exported to a txt document on your desktop")

