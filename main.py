import os

print("=" * 50)
print("             EXPENSE TRACKER")
print("=" * 50)

expenses = []

# -------------------------------
# Load Expenses from File
# -------------------------------
if os.path.exists("expenses.txt"):

    with open("expenses.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if len(data) == 2:

                expenses.append({
                    "category": data[0],
                    "amount": float(data[1])
                })

# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Spending")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # -------------------------------
    # Add Expense
    # -------------------------------
    if choice == "1":

        category = input("\nEnter Expense Category: ").strip().title()

        try:

            amount = float(input("Enter Amount: ₹"))

            expenses.append({
                "category": category,
                "amount": amount
            })

            with open("expenses.txt", "a") as file:
                file.write(f"{category},{amount}\n")

            print("\n✅ Expense added successfully!")

        except ValueError:

            print("\n❌ Please enter a valid amount.")

    # -------------------------------
    # View Expenses
    # -------------------------------
    elif choice == "2":

        if len(expenses) == 0:

            print("\nNo expenses found.")

        else:

            print("\n" + "=" * 50)
            print("               EXPENSE LIST")
            print("=" * 50)

            print(f"{'No.':<5}{'Category':<20}{'Amount'}")
            print("-" * 50)

            for i, expense in enumerate(expenses, start=1):

                print(f"{i:<5}{expense['category']:<20}₹{expense['amount']:.2f}")

            print("-" * 50)

    # -------------------------------
    # Search Expense
    # -------------------------------
    elif choice == "3":

        search = input("\nEnter Expense Category: ").strip().title()

        found = False

        for expense in expenses:

            if expense["category"] == search:

                print("\nExpense Found")
                print("-" * 40)
                print(f"Category : {expense['category']}")
                print(f"Amount   : ₹{expense['amount']:.2f}")
                print("-" * 40)

                found = True

        if not found:

            print("\n❌ Expense not found.")

    # -------------------------------
    # Delete Expense
    # -------------------------------
    elif choice == "4":

        if len(expenses) == 0:

            print("\nNo expenses available.")

        else:

            print()

            for i, expense in enumerate(expenses, start=1):

                print(f"{i}. {expense['category']} - ₹{expense['amount']:.2f}")

            try:

                delete = int(input("\nEnter expense number to delete: "))

                if 1 <= delete <= len(expenses):

                    expenses.pop(delete - 1)

                    with open("expenses.txt", "w") as file:

                        for expense in expenses:

                            file.write(f"{expense['category']},{expense['amount']}\n")

                    print("\n✅ Expense deleted successfully!")

                else:

                    print("\n❌ Invalid expense number.")

            except ValueError:

                print("\n❌ Please enter a valid number.")

    # -------------------------------
    # Total Spending
    # -------------------------------
    elif choice == "5":

        total = sum(expense["amount"] for expense in expenses)

        print("\n" + "=" * 40)
        print(f"Total Spending : ₹{total:.2f}")
        print("=" * 40)

    # -------------------------------
    # Exit
    # -------------------------------
    elif choice == "6":

        print("\nThank you for using Expense Tracker!")
        break

    else:

        print("\n❌ Invalid choice!")