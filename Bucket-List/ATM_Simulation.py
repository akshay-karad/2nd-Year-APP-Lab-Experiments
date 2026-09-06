
# Scenario 2: ATM Simulation

class ATM:
    bank_name = "ABC Bank"  # Class variable
    atm_count = 0            # Class variable

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private variable
        ATM.atm_count += 1

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        withdrawal_limit = 20000

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > withdrawal_limit:
            print("Withdrawal limit is ₹20,000 per transaction.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.__balance}")

    def display_account(self):
        print("\n--- Account Details ---")
        print(f"Bank: {ATM.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        self.check_balance()


# User interaction
print("===== ATM SIMULATION =====")

name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: ₹"))

atm = ATM(name, initial_balance)

while True:
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: ₹"))
        atm.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))
        atm.withdraw(amount)

    elif choice == "3":
        atm.check_balance()

    elif choice == "4":
        atm.display_account()

    elif choice == "5":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")
