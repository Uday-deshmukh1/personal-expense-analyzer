from datetime import datetime

VALID_CATEGORIES = ["Food", "Travel", "Shopping", "Education", "Entertainment", "Health", "Bills", "Other"]
VALID_PAYMENT_METHODS = ["UPI", "Cash", "Card", "Net Banking", "Wallet"]


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(amount_string):
    try:
        amount = float(amount_string)
        if amount <= 0:
            return False, "Amount must be greater than zero."
        return True, amount
    except ValueError:
        return False, "Invalid amount. Please enter a number."


def validate_category(category):
    if category in VALID_CATEGORIES:
        return True
    return False


def validate_payment_method(method):
    if method in VALID_PAYMENT_METHODS:
        return True
    return False


def get_validated_expense_input():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if not date:
            print("Date cannot be empty.")
            continue
        if not validate_date(date):
            print("Invalid date format. Use YYYY-MM-DD.")
            continue
        break

    while True:
        print(f"Categories: {', '.join(VALID_CATEGORIES)}")
        category = input("Enter category: ").strip().title()
        if not category:
            print("Category cannot be empty.")
            continue
        if not validate_category(category):
            print("Invalid category. Choose from the list.")
            continue
        break

    while True:
        description = input("Enter description: ").strip()
        if not description:
            print("Description cannot be empty.")
            continue
        break

    while True:
        amount_input = input("Enter amount: ").strip()
        if not amount_input:
            print("Amount cannot be empty.")
            continue
        valid, result = validate_amount(amount_input)
        if not valid:
            print(result)
            continue
        amount = result
        break

    while True:
        print(f"Payment methods: {', '.join(VALID_PAYMENT_METHODS)}")
        payment_method = input("Enter payment method: ").strip().title()
        if not payment_method:
            print("Payment method cannot be empty.")
            continue
        if not validate_payment_method(payment_method):
            print("Invalid payment method. Choose from the list.")
            continue
        break

    return date, category, description, amount, payment_method
