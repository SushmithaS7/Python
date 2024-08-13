class ATM:
    def __init__(self, initial_balance=0, pin="1234"):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, input_pin):
        """Check if the input PIN matches the stored PIN."""
        return input_pin == self.pin

    def account_balance(self):
        """Return the current account balance."""
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Balance inquiry")

    def cash_withdrawal(self, amount):
        """Withdraw cash from the account if sufficient balance is available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. You withdrew ${amount:.2f}.")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds.")
            self.transaction_history.append("Failed withdrawal attempt due to insufficient funds")

    def cash_deposit(self, amount):
        """Deposit cash into the account."""
        self.balance += amount
        print(f"Deposit successful. You deposited ${amount:.2f}.")
        self.transaction_history.append(f"Deposited ${amount:.2f}")

    def change_pin(self, old_pin, new_pin):
        """Change the account PIN if the old PIN is correct."""
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("PIN successfully changed.")
            self.transaction_history.append("PIN changed")
        else:
            print("Incorrect old PIN.")
            self.transaction_history.append("Failed PIN change attempt")

    def show_transaction_history(self):
        """Print all the transactions that have been made."""
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    # Initialize the ATM with a balance and a default PIN
    atm = ATM(initial_balance=1000)

    # Simulation of ATM operations
    while True:
        print("\n--- ATM Machine ---")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            atm.account_balance()
        
        elif choice == "2":
            try:
                amount = float(input("Enter the amount to withdraw: "))
                atm.cash_withdrawal(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        elif choice == "3":
            try:
                amount = float(input("Enter the amount to deposit: "))
                atm.cash_deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        elif choice == "4":
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            atm.change_pin(old_pin, new_pin)
        
        elif choice == "5":
            atm.show_transaction_history()
        
        elif choice == "6":
            print("Exiting the ATM. Thank you!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
