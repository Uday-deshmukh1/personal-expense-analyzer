from expense import Expense
from data_manager import save_expense, get_next_id
from validation import get_validated_expense_input


def add_expense():
    print("\n--- Add New Expense ---")
    date, category, description, amount, payment_method = get_validated_expense_input()
    expense_id = get_next_id()

    new_expense = Expense(expense_id, date, category, description, amount, payment_method)
    save_expense(new_expense.to_dict())
    print(f"\nExpense #{expense_id} added successfully.")
