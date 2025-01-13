class Checkbook:
    """
    This class represents a simple checkbook for managing a bank account.
    It supports deposit, withdrawal, and balance checking operations.
    """

    def __init__(self):
        """
        Initializes the Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Parameters:
        amount (float): The amount to deposit into the account.
        """
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.

        Parameters:
        amount (float): The amount to withdraw from the account.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the account.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.
    It allows the user to deposit, withdraw, or check balance.
    The program continues until the user chooses to exit.
    """
    cb = Checkbook()
    
    while True:
        # Get user input for the desired action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        
        if action == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif action == 'deposit':
            # Error handling for non-numeric input during deposit
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'withdraw':
            # Error handling for non-numeric input during withdrawal
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
