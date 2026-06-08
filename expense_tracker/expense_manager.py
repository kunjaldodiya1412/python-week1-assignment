from datetime import datetime
from models import Expense


class ExpenseManager:
    def __init__(self, expenses):
        self.expenses = expenses

    def add_expense(self):
        """Collect expense details from user and add to list."""
        print("\n--- Add New Expense ---")

        # Date input
        date_input = input("Enter date (DD-MM-YYYY) or press Enter for today: ").strip()
        if not date_input:
            date_input = datetime.today().strftime("%d-%m-%Y")
        else:
            try:
                datetime.strptime(date_input, "%d-%m-%Y")
            except ValueError:
                print("❌ Invalid date format. Use DD-MM-YYYY.")
                return None

        # Category input
        print("Common categories: Food, Travel, Shopping, Medical, Entertainment, Other")
        category = input("Enter category: ").strip()
        if not category:
            print("❌ Category cannot be empty.")
            return None

        # Description input
        description = input("Enter description: ").strip()
        if not description:
            print("❌ Description cannot be empty.")
            return None

        # Amount input with validation
        try:
            amount = float(input("Enter amount (₹): ").strip())
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                return None
        except ValueError:
            print("❌ Invalid amount. Please enter a numeric value.")
            return None

        expense = Expense(date_input, category.capitalize(), description, amount)
        self.expenses.append(expense)
        print(f"\n✅ Expense added successfully!")
        return expense

    def view_all_expenses(self):
        """Display all expenses in a formatted table."""
        if not self.expenses:
            print("\n⚠️  No expenses recorded yet.")
            return

        print("\n" + "=" * 75)
        print(f"{'DATE':<13} {'CATEGORY':<15} {'DESCRIPTION':<25} {'AMOUNT':>10}")
        print("=" * 75)

        for exp in self.expenses:
            print(f"{exp.date:<13} {exp.category:<15} {exp.description:<25} ₹{exp.amount:>9.2f}")

        print("=" * 75)
        print(f"{'Total Entries:':<40} {len(self.expenses)}")
        print(f"{'Total Amount:':<40} ₹{sum(e.amount for e in self.expenses):.2f}")
        print("=" * 75)

    def filter_by_category(self):
        """Filter and display expenses by category."""
        if not self.expenses:
            print("\n⚠️  No expenses recorded yet.")
            return

        # Show available categories
        categories = list(set(e.category for e in self.expenses))
        print("\nAvailable categories:")
        for i, cat in enumerate(categories, 1):
            print(f"  {i}. {cat}")

        search = input("\nEnter category name to filter: ").strip().capitalize()
        filtered = [e for e in self.expenses if e.category == search]

        if not filtered:
            print(f"❌ No expenses found under category: {search}")
            return

        print(f"\n--- Expenses for '{search}' ---")
        print("=" * 75)
        print(f"{'DATE':<13} {'DESCRIPTION':<30} {'AMOUNT':>10}")
        print("=" * 75)

        for exp in filtered:
            print(f"{exp.date:<13} {exp.description:<30} ₹{exp.amount:>9.2f}")

        print("=" * 75)
        total = sum(e.amount for e in filtered)
        print(f"Total spent on {search}: ₹{total:.2f}")

    def show_summary_report(self):
        """Generate and display a summary report of all expenses."""
        if not self.expenses:
            print("\n⚠️  No expenses to generate report.")
            return

        total_entries = len(self.expenses)
        total_spent = sum(e.amount for e in self.expenses)
        highest = max(self.expenses, key=lambda e: e.amount)

        # Category-wise totals
        category_totals = {}
        for exp in self.expenses:
            category_totals[exp.category] = category_totals.get(exp.category, 0) + exp.amount

        print("\n" + "=" * 45)
        print("         📊 EXPENSE SUMMARY REPORT")
        print("=" * 45)
        print(f"  Total Entries      : {total_entries}")
        print(f"  Total Spent        : ₹{total_spent:.2f}")
        print(f"  Highest Expense    : {highest.category} - ₹{highest.amount:.2f}")
        print(f"                       ({highest.description} on {highest.date})")
        print("\n  Category-wise Breakdown:")
        print("  " + "-" * 35)
        for cat, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat:<20} : ₹{total:.2f}")
        print("=" * 45)