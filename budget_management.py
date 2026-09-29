"""
Module 4- Budget management
allows users to set a budget for any category and track their spendings.
"""
def set_budget(budgets, category, amount):
    if amount < 0:
        print("Budget cannot be negative.")
        return
    budgets[category] = amount
    print("Budget set successfully.")


def display_budgets(budgets):
    if len(budgets) == 0:
        print("No budgets have been set.")
        return
    print("\n----- Category Budgets -----")
    for category in budgets:
        print(category, ":", budgets[category])

def calculate_category_expense(transactions, category):
    total = 0
    for transaction in transactions:
        if (transaction["type"] == "Expense" and transaction["category"] == category):
            total = total + transaction["amount"]
            return total


def check_budget(transactions, budgets, category):
    if category not in budgets:
        print("No budget has been set for", category)
        return
    budget = budgets[category]
    spent = calculate_category_expense(transactions,category)
    safe_budget = budget if budget is not None else 0.0
    safe_spent = spent if spent is not None else 0.0
    remaining = safe_budget - safe_spent
    print("\nCategory:", category)
    print("Budget:", budget)
    print("Spent:", spent)
    print("Remaining:", remaining)
    if spent > budget:
        print("WARNING: EXCEEDED BUDGET!")
    elif spent == budget:
        print("WARNING: You have reached your budget limit.")
    else:
        print("You are within your budget.")


def check_all_budgets(transactions, budgets):
    for category in budgets:
        check_budget(transactions,budgets,category)
