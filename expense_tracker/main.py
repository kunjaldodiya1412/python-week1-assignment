from file_handler import load_expenses, save_expense
from expense_manager import ExpenseManager


def show_menu():
    print("\n" + "=" * 40)
    print("       💰 EXPENSE TRACKER 💰")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. Expense Summary Report")
    print("5. Exit")
    print("=" * 40)


def main():
    expenses = load_expenses()
    manager = ExpenseManager(expenses)

    print("\nWelcome to Expense Tracker!")
    print("Previous records loaded successfully." if expenses else "No previous records found. Starting fresh.")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            expense = manager.add_expense()
            if expense:
                save_expense(expense)

        elif choice == "2":
            manager.view_all_expenses()

        elif choice == "3":
            manager.filter_by_category()

        elif choice == "4":
            manager.show_summary_report()

        elif choice == "5":
            print("\nThank you for using Expense Tracker. Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()