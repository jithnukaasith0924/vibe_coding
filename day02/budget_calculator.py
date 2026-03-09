def main():
    try:
        total_budget = float(input("Enter your total monthly budget: "))
        
        expense1 = float(input("Enter expense 1: "))
        expense2 = float(input("Enter expense 2: "))
        expense3 = float(input("Enter expense 3: "))
        
        total_expenses = expense1 + expense2 + expense3
        remaining_balance = total_budget - total_expenses
        
        print("\n--- Budget Summary ---")
        print(f"Total Budget:      LKR {total_budget:.2f}")
        print(f"Total Expenses:    LKR {total_expenses:.2f}")
        print(f"Remaining Balance: LKR {remaining_balance:.2f}")
        
        if remaining_balance < 500:
            print("Warning: Low Funds")
        
    except ValueError:
        print("Invalid input. Please enter numerical values for the budget and expenses.")

if __name__ == "__main__":
    main()
