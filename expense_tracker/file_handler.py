import csv
import os
from models import Expense

FILE_PATH = "expenses.csv"
HEADERS = ["date", "category", "description", "amount"]


def load_expenses():
    """Load all expenses from CSV file. Returns list of Expense objects."""
    expenses = []

    if not os.path.exists(FILE_PATH):
        return expenses

    try:
        with open(FILE_PATH, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = Expense(
                    date=row["date"],
                    category=row["category"],
                    description=row["description"],
                    amount=row["amount"]
                )
                expenses.append(expense)
    except FileNotFoundError:
        print("No existing expense file found. Starting fresh.")
    except Exception as e:
        print(f"Error loading expenses: {e}")

    return expenses


def save_expense(expense):
    """Append a single expense to the CSV file."""
    file_exists = os.path.exists(FILE_PATH)

    try:
        with open(FILE_PATH, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)

            # Write header only if file is new
            if not file_exists:
                writer.writeheader()

            writer.writerow(expense.to_dict())
    except Exception as e:
        print(f"Error saving expense: {e}")