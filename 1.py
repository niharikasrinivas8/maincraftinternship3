import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"


# Create file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount"])


# Add expense
def add_expense():
    description = input("Enter description: ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])

    print("Expense added successfully!\n")


# View all expenses
def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# Search by category
def search_category():
    search = input("Enter category to search: ").lower()

    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if row["Category"].lower() == search:
                print(row)
                found = True

        if not found:
            print("No expenses found in this category.")


# Total spent per category
def total_per_category():
    totals = {}

    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    print("\nTotal Spending Per Category:")
    for cat, total in totals.items():
        print(cat, ":", total)


# Monthly spending
def monthly_spending():
    month = input("Enter month (YYYY-MM): ")

    total = 0

    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])

    print("Total spending for", month, "=", total)


# Menu
def menu():
    initialize_file()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total per Category")
        print("5. Monthly Spending")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_category()
        elif choice == "4":
            total_per_category()
        elif choice == "5":
            monthly_spending()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


menu()