"""
module 5- Financial analysis
this module tells us-
1. Total income.
2. Total expenses.
3. Savings (income minus expenses).
4. Average expense.
5. Spending totals for each category.
6. A monthly income and expense summary.
"""
def calculate_total_income(transactions):
    total = 0
    for transaction in transactions:
        if transaction["type"] == "Income":
            total = total + transaction["amount"]
    return total

def calculate_total_expenses(transactions):
    total = 0
    for transaction in transactions:
        if transaction["type"] == "Expense":
            total = total + transaction["amount"]
    return total


def calculate_savings(transactions):
    income = calculate_total_income(transactions)
    expenses = calculate_total_expenses(transactions)
    return income - expenses

def calculate_average_expense(transactions):
    total = 0
    count = 0
    for transaction in transactions:
        if transaction["type"] == "Expense":
            total = total + transaction["amount"]
            count = count + 1
    if count == 0:
        return 0
    return total / count

def calculate_category_expenses(transactions):
    category_totals = {}
    for transaction in transactions:
        if transaction["type"] == "Expense":
            category = transaction["category"]
            amount = transaction["amount"]
            if category in category_totals:
                category_totals[category] = (category_totals[category] + amount)
            else:
                category_totals[category] = amount
    return category_totals


def calculate_monthly_summary(transactions):

    monthly_data = {}
    for transaction in transactions:
        month = transaction["date"][:7]
        if month not in monthly_data:
            monthly_data[month] = {"Income": 0,"Expense": 0}
        transaction_type = transaction["type"]
        if transaction_type == "Income":
            monthly_data[month]["Income"] += transaction["amount"]
        elif transaction_type == "Expense":
            monthly_data[month]["Expense"] += transaction["amount"]
    return monthly_data

def display_financial_summary(transactions):
    income = calculate_total_income(transactions)
    expenses = calculate_total_expenses(transactions)
    savings = calculate_savings(transactions)
    average = calculate_average_expense(transactions)
    print("\n===== Financial Summary =====")
    print("Total Income: ₹", income)
    print("Total Expenses: ₹", expenses)
    print("Savings: ₹", savings)
