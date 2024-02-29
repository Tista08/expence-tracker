def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def view_expenses(expenses):
    total_expenses = 0
    print("Expense Tracker:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount}")
        total_expenses += amount
    print(f"Total Expenses: ${total_expenses}")

def main():
    expenses = {}
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
            print("Expense added successfully!")
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
