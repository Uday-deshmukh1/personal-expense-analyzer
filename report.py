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
