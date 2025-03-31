expenses = {}

def add_expense(expense_name, description, amount):
    #Add an expense to the expenses dictionary
    expenses[expense_name] = {'description': description, 'amount': amount}
    print(f"Expense added: [ID: {expense_name}, Description: {description}, Amount: ${amount}]")

def view_expenses():
    #View all expenses
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses:")
    for expense_name, details in expenses.items():
        print(f"ID: {expense_name}, Description: {details['description']}, Amount: ${details['amount']}")
    print()

def delete_expense(expense_name):
    #Delete an expense by its ID
    if expense_name in expenses:
        del expenses[expense_name]
        print(f"Expense ID {expense_name} deleted.")
    else:
        print(f"Expense ID {expense_name} not found.")

def main():
    while True:
        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            expense_id = input("Enter Expense ID: ")
            description = input("Enter Description: ")
            amount = float(input("Enter Amount: "))
            add_expense(expense_id, description, amount)  # Fixed: using expense_id instead of expense_name

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            expense_id = input("Enter Expense ID to delete: ")
            delete_expense(expense_id)  # Fixed: using expense_id instead of expense_name

        elif choice == '4':
            print("Exiting the Expense Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

