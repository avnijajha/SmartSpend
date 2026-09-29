SmartSpend – Project Statement

1. Problem Statement
Managing personal income and expenses manually can make it difficult for users to understand their spending habits and control their budgets.
People may record expenses in notebooks, spreadsheets, or different applications, making it difficult to maintain transaction records and analyze their spending patterns.
There is a need for a simple system that allows users to record income and expenses, categorize transactions, set budgets, and obtain useful financial summaries.
SmartSpend is developed to address this problem by providing a Python-based expense tracking and budget management system. The application allows users to manage their transactions, categorize expenses, monitor category-wise budgets, and analyze their financial activities.
The project focuses on providing these features without using an SQL database.

2. Scope of the Project
The scope of SmartSpend includes the development of a personal finance management application with the following capabilities:
-Recording income and expense transactions.
-Editing and deleting transaction records.
-Searching, filtering, and sorting transactions.
-Importing transactions from bank statement CSV files.
-Categorizing expenses using keyword-based rules.
-Setting category-wise spending budgets.
-Monitoring spending against assigned budgets.
-Generating warnings when spending approaches or exceeds a budget.
-Calculating total income and total expenses.
-Calculating savings and average expenses.
-Generating category-wise expense summaries.
-Generating monthly financial summaries.
-Storing data locally using files instead of an SQL database.
The project is intended for personal expense management and does not aim to provide banking, investment, payment processing, or direct financial transaction services.

3. Target Users
SmartSpend is primarily intended for individuals who want to keep track of their personal finances.
-Students
Students can use SmartSpend to:
Record daily expenses.
Track spending on food, transport, education, entertainment, and shopping.
Set limits for different categories.
Understand their monthly spending.
-Working Professionals
Working professionals can use the application to:
Track income and expenses.
Monitor monthly spending.
Set category-wise budgets.
Analyze savings and spending patterns.
Individuals Managing Personal Finances
Anyone who wants a simple method of recording and analyzing personal expenses can use SmartSpend.
The application is designed particularly for users who prefer a simple local desktop application rather than a complex financial management platform.

4. High-Level Features
4.1 Transaction Management
Users can add, view, edit, delete, search, filter, and sort income and expense transactions.
4.2 Bank Statement Import
Users can import transaction records from a CSV-formatted bank statement instead of entering every transaction manually.
4.3 Automatic Expense Categorization
The application categorizes expenses based on keywords found in transaction descriptions.
Example:
Swiggy → Food
Uber → Transport
Amazon → Shopping
Netflix → Entertainment
Electricity Bill → Bills
4.4 Budget Management
Users can set spending limits for different categories and monitor their spending against those limits.
4.5 Budget Warnings
The system provides warnings when spending reaches a significant portion of the budget or exceeds the assigned budget.
4.6 Financial Analysis
The application provides information such as:
Total income
Total expenses
Savings
Average expense
Largest expense
Category-wise expenses
Monthly income and expenses
4.7 Local File Storage
The project stores data locally using file handling techniques such as CSV and binary files instead of using an SQL database.

5. Project Goal
The main goal of SmartSpend is to develop a simple, modular, and user-friendly personal expense management system using Python.
The project also demonstrates the practical application of programming and problem-solving concepts such as functions, lists, dictionaries, loops, conditional statements, searching, sorting, file handling, and basic algorithms.