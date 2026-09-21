import sys

from expense_manager import add_expense, view_expenses, delete_expense
from analyzer import (
    display_total_expense,
    display_average_expense,
    display_category_analysis,
    display_payment_analysis,
    display_highest_expense,
    display_monthly_analysis,
)
from report import generate_category_graph, generate_monthly_graph, generate_summary_report


def print_menu():
    print("\n" + "=" * 42)
    print("       PERSONAL EXPENSE ANALYZER")
    print("=" * 42)
    print("1.  Add Expense")
    print("2.  View Expenses")
    print("3.  Delete Expense")
    print("4.  Total Expense")
    print("5.  Average Expense")
    print("6.  Category Analysis")
    print("7.  Payment Analysis")
    print("8.  Highest Expense")
    print("9.  Monthly Analysis")
    print("10. Generate Graphs")
    print("11. Generate Report")
    print("12. Exit")
    print("=" * 42)


def main():
    while True:
        try:
            print_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                delete_expense()
            elif choice == "4":
                display_total_expense()
            elif choice == "5":
                display_average_expense()
            elif choice == "6":
                display_category_analysis()
            elif choice == "7":
                display_payment_analysis()
            elif choice == "8":
                display_highest_expense()
            elif choice == "9":
                display_monthly_analysis()
            elif choice == "10":
                generate_category_graph()
                generate_monthly_graph()
            elif choice == "11":
                generate_summary_report()
            elif choice == "12":
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 12.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit()
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
