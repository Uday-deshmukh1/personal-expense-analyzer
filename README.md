# Personal Expense Analyzer

A Python-based command-line application for recording and analyzing personal expenses.

## Features

- Add, view, and delete expenses
- Calculate total and average expenses
- Category-wise expense analysis
- Payment method analysis
- Highest expense detection
- Monthly expense analysis
- Category-wise and monthly expense graphs
- Text-based expense summary report
- CSV-based persistent storage
- Input validation and error handling

## Tech Stack

- Python
- Pandas
- Matplotlib
- CSV

## Project Structure

```
personal-expense-analyzer/
├── main.py
├── expense.py
├── expense_manager.py
├── analyzer.py
├── report.py
├── data_manager.py
├── validation.py
├── requirements.txt
├── README.md
├── data/
│   └── expenses.csv
├── graphs/
└── reports/
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Uday-deshmukh1/personal-expense-analyzer.git
cd personal-expense-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

## Example Usage

```
========================================
       PERSONAL EXPENSE ANALYZER
========================================
1.  Add Expense
2.  View Expenses
...
Enter your choice: 1

--- Add New Expense ---
Enter date (YYYY-MM-DD): 2026-09-15
Categories: Food, Travel, Shopping, Education, Entertainment, Health, Bills, Other
Enter category: Food
Enter description: Lunch
Enter amount: 250
Payment methods: UPI, Cash, Card, Net Banking, Wallet
Enter payment method: UPI

Expense #1 added successfully.
```

## Future Improvements

- Export expenses to Excel
- Budget limit alerts
- Recurring expense support
- Category-wise budget tracking

## Author

Uday Deshmukh
