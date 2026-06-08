import csv
import os

FILE_NAME = "expenses.CSV"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


initialize_file()


def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")
    description = input("Enter Description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n------ Expense Records ------")
            for row in reader:
                print("\t".join(row))

    except FileNotFoundError:
        print("No records found.")


def search_expense():
    category = input("Enter category to search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 1 and row[1].lower() == category.lower():
                print(row)
                found = True

    if not found:
        print("No matching expense found.")


def delete_expense():
    date = input("Enter date of expense to delete: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 0 and row[0] != date:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Expense deleted successfully (if found).")