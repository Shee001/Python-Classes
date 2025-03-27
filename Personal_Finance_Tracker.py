# Title: Personal Finance Tracker
# Description: A simple program to track personal finance transactions.

import csv
from datetime import datetime

# Initialize data structure
finance_data = {
    "income": [],
    "expenses": []
}

# Function to add income
def add_income():
    try:
        amount = float(input("Enter income amount: "))
        category = input("Enter income category (e.g. Salary, Gift): ")
        description = input("Enter description: ")
        date = datetime.now().strftime("%Y-%m-%d")
        finance_data["income"].append((amount, category, description, date))
        print("Income added successfully.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

# Function to add expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category (e.g. Food, Transport): ")
        description = input("Enter description: ")
        date = datetime.now().strftime("%Y-%m-%d")
        finance_data["expenses"].append((amount, category, description, date))
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

# Function to view financial summary
def view_summary():
    total_income = sum(entry[0] for entry in finance_data["income"])
    total_expenses = sum(entry[0] for entry in finance_data["expenses"])
    balance = total_income - total_expenses

    print("\n--- Financial Summary ---")
    print(f"Total Income   : ${total_income:.2f}")
    print(f"Total Expenses : ${total_expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")

# Function to save data to CSV
def save_to_csv():
    with open("transactions.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Category", "Description", "Date"])

        for entry in finance_data["income"]:
            writer.writerow(["Income", *entry])
        for entry in finance_data["expenses"]:
            writer.writerow(["Expense", *entry])
    
    print("Transactions saved to transactions.csv\n")

# Main menu
def menu():
    while True:
        print("----- Personal Finance Tracker -----")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            print("Thank you for using the finance tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
