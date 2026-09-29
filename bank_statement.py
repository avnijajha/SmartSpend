import csv
import os
"""
module 2- Bank statement import
allows users to import transactions from a bank statement in CSV file format and add them to the existing transaction list.
"""
def import_statement(transactions, file_path):
    if not os.path.exists(file_path):
        print("Error: Bank statement file not found.")
        return 0
    next_id = 1
    for transaction in transactions:
        if transaction["id"] >= next_id:
            next_id = transaction["id"] + 1
    imported_count = 0
    try:
        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            required_columns = ["Date", "Description", "Amount", "Type"]
            if reader.fieldnames is None:
                print("Error: File is empty.")
                return 0
            for column in required_columns:
                if column not in reader.fieldnames:
                    print("Error: Missing required column:", column)
                    return 0
            for row in reader:
                try:
                    date = row["Date"].strip()
                    description = row["Description"].strip()
                    amount = float(row["Amount"])
                    transaction_type = row["Type"].strip().capitalize()
                    if date == "" or description == "":
                        print("Skipped a row because its date or description is missing.")
                        continue
                    if amount <= 0:
                        print("Skipped a row because its amount is not positive.")
                        continue
                    if transaction_type not in ["Income", "Expense"]:
                        print("Skipped a row because its type is invalid.")
                        continue
                    transaction = {
                        "id": next_id,
                        "date": date,
                        "description": description,
                        "amount": amount,
                        "type": transaction_type,
                        "category": "Others"
                    }
                    transactions.append(transaction)
                    next_id += 1
                    imported_count += 1
                except (ValueError, KeyError):
                    print("Skipped a row because some data is invalid.")
    except OSError:
        print("Error: Unable to open or read the CSV file.")
        return 0
    print(imported_count, "transaction(s) imported successfully.")
    return imported_count