from transactions import (add_transaction,view_transaction,find_transaction,edit_transaction,delete_transaction,search_transactions,type_filter,filter_category)
import bank_statement
import expense_categorization
import budget_management
import financial_analysis

transactions=[]
budgets={}

def add_new_transaction():
    print("\n----- Add Transaction -----")
    date = input("Enter date (DD-MM-YYYY): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    transaction_type = input("Enter type (Income/Expense): ")
    category = input("Enter category: ")
    add_transaction(transactions,date,description,amount,transaction_type,category)

def import_bank_statement():
    print("\n----- Import Bank Statement -----")
    file_path = input("Enter the CSV file path: ")
    bank_statement.import_statement(transactions, file_path)

def manage_budgets():
    while True:
        print("\n----- Budget Management -----")
        print("1. Set or update a budget")
        print("2. Display all budgets")
        print("3. Check one category's budget")
        print("4. Check all budgets")
        print("5. Return to main menu")
        choice = int(input("Enter choice: "))
        if choice == 1:
            category = input("Enter category: ")
            amount = float(input("Enter budget amount: "))
            budget_management.set_budget(budgets, category, amount)
        elif choice == 2:
            budget_management.display_budgets(budgets)
        elif choice == 3:
            category = input("Enter category to check: ")
            budget_management.check_budget(transactions, budgets, category)
        elif choice == 4:
            budget_management.check_all_budgets(transactions, budgets)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Try again.")

def finance_analysis():
    while True:
        print("\nFinancial Analysis")
        print("1. Overall financial summary")
        print("2. Category-wise expenses")
        print("3. Monthly summary")
        print("4. Return to main menu")
        choice =int(input("Enter your choice: "))
        if choice == 1:
            financial_analysis.display_financial_summary(transactions)
        elif choice == 2:
            financial_analysis.calculate_category_expenses(transactions)
        elif choice == 3:
            financial_analysis.calculate_monthly_summary(transactions)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def search_and_filter_transactions():
    while True:
        print("\n----- Search, Filter and Sort -----")
        print("1. Search by keyword")
        print("2. Filter by type")
        print("3. Filter by category")
        print("4. Return to main menu")
        choice =int(input("Enter your choice: "))
        if choice == 1:
            keyword = input("Enter keyword: ")
            results = search_transactions(transactions, keyword)
            view_transaction(results)
        elif choice == 2:
            transaction_type = input("Enter type (Income/Expense): ")
            results =type_filter(transactions, transaction_type)
            view_transaction(results)
        elif choice == 3:
            category = input("Enter category: ")
            results =filter_category(transactions, category)
            view_transaction(results)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nSMARTSPEND")
        print("1. Add transaction")
        print("2. Import bank statement")
        print("3. Display transactions")
        print("4. Categorize transactions")
        print("5. Budget management")
        print("6. Financial analysis")
        print("7. Search, filter and sort")
        print("8. Find transaction by ID")
        print("9. Delete transaction")
        print("10. Edit transaction")
        print("11. Exit")
        choice =int(input("Enter your choice: "))
        if choice == 1:
            add_new_transaction()
        elif choice == 2:
            import_bank_statement()
        elif choice == 3:
            view_transaction(transactions)
        elif choice == 4:
            expense_categorization.categorize_all_transactions(transactions)
            expense_categorization.display_categories(transactions)
        elif choice == 5:
            manage_budgets()
        elif choice == 6:
            finance_analysis()
        elif choice == 7:
            search_and_filter_transactions()
        elif choice == 8:
            transaction_id = int(input("Enter transaction ID: "))
            result =find_transaction(transactions, transaction_id)
            if result is None:
                print("Transaction not found.")
            else:
                print(result)
        elif choice == 9:
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_transaction(transactions, transaction_id)
        elif choice == 10:
            transaction_id = int(input("Enter transaction ID to edit: "))
            print("Leave blank if you do not want to change it.")
            date = input("Enter new date (DD-MM-YYYY): ")
            description = input("Enter new description: ")
            amount = input("Enter new amount: ")
            transaction_type = input("Enter new type (Income/Expense): ")
            category = input("Enter new category: ")
            if date == "":
                date = None
            if description == "":
                description = None
            if amount == "":
                amount = None
            else:
                amount = float(amount)
            if transaction_type == "":
                transaction_type = None
            else:
                transaction_type = transaction_type.capitalize()
            if category == "":
                 category = None
            edit_transaction(transactions,transaction_id,date,description,amount,transaction_type,category)
        elif choice == 11:
            print("Thank you for using SmartSpend!")
            break
        else:
            print("Invalid choice. Please try again.")
main()