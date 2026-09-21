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
