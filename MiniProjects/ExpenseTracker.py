expenses = {}
print("=== EXPENSE TRACKER ===")
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        print("Expense Added Successfully!")
    elif choice == "2":
        print("\nExpenses:")
        for category, amount in expenses.items():
            print(category, ":", amount)

    elif choice == "3":
        total = sum(expenses.values())
        print("Total Expense:", total)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
