from expense import Expense
from data_manager import save_expense, get_next_id, load_all_expenses, delete_expense_by_id
from validation import get_validated_expense_input


def add_expense():
    try:
        print("\n--- Add New Expense ---")
        date, category, description, amount, payment_method = get_validated_expense_input()
        expense_id = get_next_id()

        new_expense = Expense(expense_id, date, category, description, amount, payment_method)
        save_expense(new_expense.to_dict())
        print(f"\nExpense #{expense_id} added successfully.")
    except Exception as e:
        print(f"Error adding expense: {e}")


def view_expenses():
    try:
        print("\n--- All Expenses ---")
        expenses = load_all_expenses()
        if not expenses:
            print("No expenses recorded yet.")
            return

        print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Description':<20} {'Amount':<10} {'Payment':<12}")
        print("-" * 74)
        for exp in expenses:
            print(f"{exp['expense_id']:<5} {exp['date']:<12} {exp['category']:<15} "
                  f"{exp['description']:<20} {exp['amount']:<10.2f} {exp['payment_method']:<12}")
    except Exception as e:
        print(f"Error loading expenses: {e}")


def delete_expense():
    try:
        print("\n--- Delete Expense ---")
        expenses = load_all_expenses()
        if not expenses:
            print("No expenses to delete.")
            return

        view_expenses()
        expense_id = int(input("\nEnter expense ID to delete: "))

        if delete_expense_by_id(expense_id):
            print(f"Expense #{expense_id} deleted successfully.")
        else:
            print(f"Expense #{expense_id} not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")
    except Exception as e:
        print(f"Error deleting expense: {e}")
