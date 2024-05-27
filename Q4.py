class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been deposited.")
        else:
            print("Invalid amount to deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount} has been withdrawn.")
        else:
            print("Invalid amount to withdraw or insufficient funds.")

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.get_balance()}"

# Subclass that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        if self.interest_rate > 0 and self.balance > 0:
            interest_amount = self.balance * (self.interest_rate / 100)
            self.deposit(interest_amount)
            print(f"Interest applied at {self.interest_rate}%. New balance is ${self.balance}.")
        else:
            print("Interest rate must be positive and balance must not be negative.")

    def __str__(self):
        return super().__str__() + f", Interest Rate: {self.interest_rate}%"

# Main Program Execution

# Creating an instance of BankAccount
bank_account = BankAccount("1234511", "kheder")
bank_account.deposit(1000)
bank_account.withdraw(500)
print(bank_account)  # Using the __str__ method to print current balance

# Creating an instance of SavingsAccount
savings_account = SavingsAccount("6789011", "khedeeer audi", interest_rate=5)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account)  # Using the __str__ method to print current balance and rate
