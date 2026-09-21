import pandas as pd
from data_manager import CSV_FILE, ensure_csv_file


def load_dataframe():
    ensure_csv_file()
    df = pd.read_csv(CSV_FILE)
    df = df[df["expense_id"] != ""]
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    return df


def get_total_expense():
    df = load_dataframe()
    if df.empty:
        return 0
    return df["amount"].sum()


def display_total_expense():
    print("\n--- Total Expense ---")
    total = get_total_expense()
    if total == 0:
        print("No expenses recorded yet.")
    else:
        print(f"Total Expense: {total:.2f}")


def display_average_expense():
    print("\n--- Average Expense ---")
    df = load_dataframe()
    if df.empty:
        print("No expenses recorded yet.")
        return
    average = df["amount"].mean()
    print(f"Number of expenses: {len(df)}")
    print(f"Average expense: {average:.2f}")
