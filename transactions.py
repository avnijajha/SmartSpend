"""
Module 1: Transaction Management
This module contains the following functions:
1. Adding transactions
2. Editing transactions
3. Deleting transactions
4. Viewing transactions
5. Searching transactions
6. Filtering transactions
7. Sorting transactions
Binary file will be added in a later module to work as a database to store transactions.
"""
def add_transaction(transactions, date, description, amount, transaction_type, category="Others"):
    """
    Adds a new transaction to the transaction list.
    """
    transaction ={"id": len(transactions) + 1,"date": date,"description": description,"amount": float(amount),"type": transaction_type,"category": category}
    transactions.append(transaction)
    return transaction

def view_transaction(transactions):
     """
     displays all transactions
     """
     if len(transactions) == 0:
        print("\nNo transactions found.")
        return
     print("\n" + "-" * 90)
     print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Description':<25}"
        f"{'Amount':<12}"
        f"{'Type':<12}"
        f"{'Category':<15}"
        )
     print("-" * 90)
     for transaction in transactions:
         print(
            f"{transaction['id']:<5}"
            f"{transaction['date']:<15}"
            f"{transaction['description']:<25}"
            f"₹{transaction['amount']:<11.2f}"
            f"{transaction['type']:<12}"
            f"{transaction['category']:<15}"
              )
         print("-" * 90)

def find_transaction(transactions, transaction_id):
    """
    Returns:
    dict: Transaction if found
    None: If transaction does not exist
    """
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction
    return None

def edit_transaction(transactions, transaction_id, date=None, description=None, amount=None, transaction_type=None, category=None):
    """
    Edits an existing transaction
    Only the values provided by the user will be changed.
    Returns:
     True if transaction was successfully edited.
     False if transaction was not found.
    """
    transaction = find_transaction(transactions, transaction_id)
    if transaction is None:
        return False
    if date is not None:
        transaction["date"] = date
    if description is not None:
        transaction["description"] = description
    if amount is not None:
        transaction["amount"] = float(amount)
    if transaction_type is not None:
        transaction["type"] = transaction_type
    if category is not None:
        transaction["category"] = category
    return True

def delete_transaction(transactions, transaction_id):
    """
    uses transaction ID to delete a transaction
    Returns:
    True if deleted.
    False if transaction was not found.
    """
    transaction = find_transaction(transactions, transaction_id)
    if transaction is None:
        return False
    transactions.remove(transaction)
    return True

def search_transactions(transactions, keyword):
    """
    Searches transactions using the description or category.
    Returns:
    list: Matching transactions
    """
    keyword = keyword.lower()
    results = []
    for transaction in transactions:
        description = transaction["description"].lower()
        category = transaction["category"].lower()
        if keyword in description or keyword in category:
            results.append(transaction)
    return results

def type_filter(transactions, transaction_type):
    """
    filters transaction by its type
    """
    results = []
    for transaction in transactions:
        if transaction["type"] == transaction_type:
            results.append(transaction)
    return results

def filter_category(transactions, category):
    """
    filters transactions by the category it is put in
    """
    results = []
    for transaction in transactions:
        if transaction["category"] == category:
            results.append(transaction)
    return results




    