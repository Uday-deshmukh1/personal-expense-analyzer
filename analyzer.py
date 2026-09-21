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


def display_category_analysis():
    print("\n--- Category Wise Analysis ---")
    df = load_dataframe()
    if df.empty:
        print("No expenses recorded yet.")
        return
    category_total = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    print(f"{'Category':<15} {'Amount':<10}")
    print("-" * 25)
    for category, amount in category_total.items():
        print(f"{category:<15} {amount:<10.2f}")
    print("-" * 25)
    print(f"{'Total':<15} {category_total.sum():<10.2f}")


def display_payment_analysis():
    print("\n--- Payment Method Analysis ---")
    df = load_dataframe()
    if df.empty:
        print("No expenses recorded yet.")
        return
    payment_total = df.groupby("payment_method")["amount"].sum().sort_values(ascending=False)
    print(f"{'Payment Method':<15} {'Amount':<10}")
    print("-" * 25)
    for method, amount in payment_total.items():
        print(f"{method:<15} {amount:<10.2f}")
    print("-" * 25)
    print(f"{'Total':<15} {payment_total.sum():<10.2f}")


def display_highest_expense():
    print("\n--- Highest Expense ---")
    df = load_dataframe()
    if df.empty:
        print("No expenses recorded yet.")
        return
    highest = df.loc[df["amount"].idxmax()]
    print(f"ID:          {highest['expense_id']}")
    print(f"Date:        {highest['date']}")
    print(f"Category:    {highest['category']}")
    print(f"Description: {highest['description']}")
    print(f"Amount:      {highest['amount']:.2f}")
    print(f"Payment:     {highest['payment_method']}")
