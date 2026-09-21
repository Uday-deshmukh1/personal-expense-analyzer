import csv
import os

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "expenses.csv")
COLUMNS = ["expense_id", "date", "category", "description", "amount", "payment_method"]


def ensure_data_directory():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def ensure_csv_file():
    ensure_data_directory()
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=COLUMNS)
            writer.writeheader()


def save_expense(expense_dict):
    ensure_csv_file()
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writerow(expense_dict)


def get_next_id():
    ensure_csv_file()
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        ids = [int(row["expense_id"]) for row in reader if row["expense_id"].isdigit()]
    if ids:
        return max(ids) + 1
    return 1


def load_all_expenses():
    ensure_csv_file()
    expenses = []
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["expense_id"]:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    return expenses


def delete_expense_by_id(expense_id):
    expenses = load_all_expenses()
    updated = [e for e in expenses if e["expense_id"] != str(expense_id)]
    if len(updated) == len(expenses):
        return False
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(updated)
    return True
