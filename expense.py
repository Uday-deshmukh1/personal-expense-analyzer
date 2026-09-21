class Expense:
    def __init__(self, expense_id, date, category, description, amount, payment_method):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.payment_method = payment_method

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount,
            "payment_method": self.payment_method,
        }

    def __str__(self):
        return (f"ID: {self.expense_id} | Date: {self.date} | Category: {self.category} | "
                f"Description: {self.description} | Amount: {self.amount} | "
                f"Payment: {self.payment_method}")
