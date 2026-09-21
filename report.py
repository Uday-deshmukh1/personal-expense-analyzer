import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from analyzer import load_dataframe

GRAPHS_DIR = "graphs"


def ensure_graphs_directory():
    if not os.path.exists(GRAPHS_DIR):
        os.makedirs(GRAPHS_DIR)


def generate_category_graph():
    df = load_dataframe()
    if df.empty:
        print("No expenses to graph.")
        return

    category_total = df.groupby("category")["amount"].sum().sort_values(ascending=True)

    plt.figure(figsize=(10, 6))
    category_total.plot(kind="barh", color="steelblue")
    plt.title("Expense by Category", fontsize=14)
    plt.xlabel("Amount")
    plt.ylabel("Category")
    plt.tight_layout()

    ensure_graphs_directory()
    filepath = os.path.join(GRAPHS_DIR, "category_expense.png")
    plt.savefig(filepath)
    plt.close()
    print(f"Category graph saved to {filepath}")


def generate_monthly_graph():
    df = load_dataframe()
    if df.empty:
        print("No expenses to graph.")
        return

    import pandas as pd
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["month"] = df["date"].dt.to_period("M")
    monthly_total = df.groupby("month")["amount"].sum().sort_index()

    plt.figure(figsize=(10, 6))
    months = [str(m) for m in monthly_total.index]
    plt.bar(months, monthly_total.values, color="coral")
    plt.title("Monthly Expense", fontsize=14)
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()

    ensure_graphs_directory()
    filepath = os.path.join(GRAPHS_DIR, "monthly_expense.png")
    plt.savefig(filepath)
    plt.close()
    print(f"Monthly graph saved to {filepath}")


REPORTS_DIR = "reports"


def ensure_reports_directory():
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)


def generate_summary_report():
    df = load_dataframe()
    if df.empty:
        print("No expenses to report.")
        return

    import pandas as pd

    total = df["amount"].sum()
    average = df["amount"].mean()
    count = len(df)
    highest = df.loc[df["amount"].idxmax()]

    category_total = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    payment_total = df.groupby("payment_method")["amount"].sum().sort_values(ascending=False)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["month"] = df["date"].dt.to_period("M")
    monthly_total = df.groupby("month")["amount"].sum().sort_index()

    report_lines = []
    report_lines.append("=" * 50)
    report_lines.append("       EXPENSE SUMMARY REPORT")
    report_lines.append("=" * 50)
    report_lines.append(f"Total Expenses:    {total:.2f}")
    report_lines.append(f"Number of Expenses: {count}")
    report_lines.append(f"Average Expense:   {average:.2f}")
    report_lines.append("")
    report_lines.append("--- Highest Expense ---")
    report_lines.append(f"  ID:          {highest['expense_id']}")
    report_lines.append(f"  Date:        {highest['date']}")
    report_lines.append(f"  Category:    {highest['category']}")
    report_lines.append(f"  Description: {highest['description']}")
    report_lines.append(f"  Amount:      {highest['amount']:.2f}")
    report_lines.append(f"  Payment:     {highest['payment_method']}")
    report_lines.append("")
    report_lines.append("--- Category Wise Summary ---")
    for category, amount in category_total.items():
        report_lines.append(f"  {category:<15} {amount:.2f}")
    report_lines.append("")
    report_lines.append("--- Payment Method Summary ---")
    for method, amount in payment_total.items():
        report_lines.append(f"  {method:<15} {amount:.2f}")
    report_lines.append("")
    report_lines.append("--- Monthly Summary ---")
    for month, amount in monthly_total.items():
        report_lines.append(f"  {str(month):<12} {amount:.2f}")
    report_lines.append("=" * 50)

    report_text = "\n".join(report_lines)
    print("\n" + report_text)

    ensure_reports_directory()
    filepath = os.path.join(REPORTS_DIR, "expense_report.txt")
    with open(filepath, "w") as f:
        f.write(report_text)
    print(f"\nReport saved to {filepath}")
