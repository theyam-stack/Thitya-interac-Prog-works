#P1 Lab 4-2
class BankAccount:
    # Class attribute
    branch_name = "KKU Complex"
    branch_number = 1724
    last_loan_number = 0
    last_saving_number = 0
    
    # Constructor
    def __init__(self, name, account_type ='saving', balance =0.0):
        self.name = name
        self.account_type = account_type.lower()
        self.balance = float(balance)

        if self.account_type == 'saving':
            BankAccount.last_saving_number += 1
            self.account_number = BankAccount.last_saving_number

        elif self.account_type == 'loan':
            BankAccount.last_loan_number += 1
            self.account_number = BankAccount.last_loan_number
        else:
            raise ValueError("Invalid account type")

    # Class method
    @classmethod
    def change_branch_name(cls, new_name):
        cls.branch_name = new_name

    def deposit(self, amount = 0.0):
        if self.account_type != 'saving':
            return "Deposit failed: Not a saving account."
        self.balance += amount
        return f"Deposited {amount:.2f}. New balance: {self.balance:.2f}"

    def pay_loan(self, amount = 0.0):
        if self.account_type != 'loan':
            return "Payment failed: Not a loan account."
        # Add to the balance for paying a loan
        self.balance += amount
        return f"Pay loan {amount:.2f}. New balance: {self.balance:.2f}"

    def withdraw(self, amount = 0.0):
        if self.account_type != 'saving':
            return "Withdrawal failed: Not a saving account."
        self.balance -= amount
        return f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}"

    def get_loan(self, amount = 0.0):
        if self.account_type != 'loan':
            return "Not a loan account. Loan acc request"
        
        # A customer can get more loan when balance is at least -50000
        # After subtracting (more loan), balance must remain >= -50000
        if (self.balance - amount) < -50000:
            return "Loan denied: Exceeds -50000 limit."
        self.balance -= amount
        return f"Loan granted {amount:.2f}. New balance: {self.balance:.2f}"

    @staticmethod
    def calc_interest(bal: float, int_rate: float, payment: float):
        year = 1
        lines = ["----- Loan Plan -----"]
        while bal > 0:
            loan = bal * (1 + int_rate / 100.0)
            pay = min(payment, loan)
            bal = loan - pay
            lines.append(f"Year {year}: loan = {loan:.2f}  payment {pay:.2f}  bal = {bal:.2f}")
            year += 1
        lines.append("----- End Plan -----")
        return "\n".join(lines)
    
# Testing the BankAccount class
if __name__ == "__main__":
    # Saving
    Pin = BankAccount('Pin','saving', 500)
    print(Pin.deposit(200))      # Deposited 200.00. New balance: 700.00
    print(Pin.withdraw(50))      # Withdrew 50.00. New balance: 650.00

    # Loan
    Mary = BankAccount('Mary','loan', -1000)  # negative balance represents outstanding loan
    print(Mary.get_loan(2000))         # Loan granted 2000.00. New balance: -3000.00
    print(Mary.pay_loan(500))          # Paid loan 500.00. New balance: -2500.00

    # Branch name change
    BankAccount.change_branch_name("Khon Kaen Branch")
    print(BankAccount.branch_name)   # Khon Kaen Branch

    # Interest plan
    plan = BankAccount.calc_interest(1000, 5, 100)
    print(plan)