from datetime import datetime
class BankAccount:
    # Interest rate for the account
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Initialize with account holder's name and zero balance
        self.account_holder = account_holder
        self.balance = 0

    def  get_current_date(self):
        "Return the current date as string."
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def display_account_info(self):
        "Show account details."
        print(f"🌟 Account Holder: {self.account_holder}")
        print(f"💰 Current Balance: ${self.balance:.2f}")


    def deposit(self, amount):
        "Add money to the account."
        if amount > 0:
            self.balance += amount
            print(f"You've deposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit successful.")

    def withdraw(self, amount):
        "withdraw money from account."
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Success! You've withdrawn ${amount:.2f}. Remaining balance: ${self.balance:.2f}.")
            else:
                print("Request failed! Insufficient funds.")

            

    def display_account_info(self):
        "Show account details."
        print(f"🌟 Account Holder: {self.account_holder}")
        print(f"💰 Current Balance: ${self.balance:.2f}")


    def apply_interest(self):
        "Add interest to the balance."
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f}.New balance: ${self.balance:.2f}.")
        print(f"💰 Current Balance:.New balance: ${self.balance:.2f}")
# Example usage of the BankAccount class

if __name__ == "__main__":
      account = BankAccount("Dombo Trevor ")
      account.display_account_info()  # Show account info
      account.deposit(100000)  # Deposit some money
      account.apply_interest()  # Apply interest
      account.withdraw(30000)   # Withdraw some money
      account.display_account_info()  # Show account info  

if __name__ == "__main__":
    account = BankAccount("Kayi Andrew")
    account.display_account_info()  # Show account info      
    account.deposit(100000)  # Deposit some money
    account.apply_interest()  # Apply interest
    account.withdraw(50000)   # Withdraw some money
    account.display_account_info()  # Show account info  