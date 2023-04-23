import datetime
import openpyxl

#Only allows you to enter a number to the prompts,
#will ask you to try again if you do not
#sets up the prompts to input data below
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")


def create_budget():
    #opening information
    now = datetime.datetime.now()
    print(f"Monthly budget creator {now.month}/{now.year}")
    print("Please input data when prompted")

    #Prompting for expenses this month
    average_monthly_income = get_integer_input("average monthly income: ")
    spending_account = get_integer_input("Current spending account balance: ")
    saving_account = get_integer_input("Current saving account balance: ")
    rent = get_integer_input("Rent ($ amount): ")
    power_gas = get_integer_input("Power/Gas ($ amount): ")
    water = get_integer_input("Water ($ amount): ")
    wifi = get_integer_input("Wifi ($ amount): ")
    groceries = get_integer_input("Groceries ($ amount): ")
    cc = get_integer_input("Credit card ($ amount): ")
    misc_expenses = get_integer_input("Other expenses this month ($ amount): ")

    #adds up all expenses
    bills = rent + power_gas + water + wifi + groceries + cc
    total_monthly_cost = misc_expenses + bills
    
    
    #to warn me if i spent too much money this month
    if average_monthly_income <= total_monthly_cost:
        print("You spent more than you earned this month and chipped into your savings")

    #calculate where my montlhly income will go and print the numbers
    spending_account += average_monthly_income * 0.2
    average_monthly_income *= 0.8
    saving_account += average_monthly_income
    saving_account -= total_monthly_cost
    print(f"Your spending account total is {spending_account}")
    print(f"Your savings account total is {saving_account}")
    
    # goes to existing excel file, File must be present on desktop for it to work
    wb = openpyxl.load_workbook("monthly budgets.xlsx")
    
    # adds a new page
    month_sheet_name = f"{now.strftime('%B %Y')}"
    month_sheet = wb.create_sheet(month_sheet_name)
    
    # inputs the information
    month_sheet["A1"] = "Total costs of month:"
    month_sheet["B1"] = total_monthly_cost
    month_sheet["A2"] = "Spending account total:"
    month_sheet["B2"] = spending_account
    month_sheet["A3"] = "Savings account total:"
    month_sheet["B3"] = saving_account
    
    # Save 
    wb.save("monthly budgets.xlsx")
    
    print("The budget information has been exported to the 'monthly budgets' Excel file.")


if __name__ == "__main__":
    create_budget()

#keeps window open until user hits enter
input("Press Enter to close out of window")
