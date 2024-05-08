class PersonalFinanceManager:
    def __init__(self):
        self.finances = {"income": {}, "expenses": {}}

    def add_income(self):
        source = input("Enter the income source: ")
        amount = float(input("Enter the amount: "))
        self.finances["income"][source] = self.finances["income"].get(source, 0) + amount

    def add_expense(self):
        category = input("Enter the expense category: ")
        amount = float(input("Enter the amount: "))
        self.finances["expenses"][category] = self.finances["expenses"].get(category, 0) + amount

    def view_summary(self):
        total_income = sum(self.finances["income"].values())
        total_expenses = sum(self.finances["expenses"].values())
        net_balance = total_income - total_expenses
        print("Total Income: $", total_income)
        print("Total Expenses: $", total_expenses)
        print("Net Balance: $", net_balance)

    def run(self):
        while True:
            print("\nPersonal Finance Manager")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Summary")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.add_income()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.view_summary()
            elif choice == "4":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    manager = PersonalFinanceManager()
    manager.run()


