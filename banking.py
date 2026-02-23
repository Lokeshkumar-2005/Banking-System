class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited: ${amount}")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn: ${amount}")

    def check_balance(self):
        print(f"💰 Current Balance: ${self.balance}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print("-----------------------\n")


def main():
    print("🏦 Welcome to Python Bank System")
    
    name = input("Enter account holder name: ")
    acc_number = input("Enter account number: ")
    account = BankAccount(name, acc_number)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.display_details()

        elif choice == "5":
            print("👋 Thank you for banking with us!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
