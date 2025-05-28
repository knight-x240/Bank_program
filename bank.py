import getpass

class Bank:
    def __init__(self):
        self.accounts = {}  # username -> {'password': ..., 'balance': ...}

    def create_account(self):
        username = input("Choose a username: ")
        if username in self.accounts:
            print("Username already exists.")
            return
        password = getpass.getpass("Choose a password: ")
        self.accounts[username] = {'password': password, 'balance': 0.0}
        print(f"Account created for {username}.")

    def login(self):
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        account = self.accounts.get(username)
        if not account or account['password'] != password:
            print("Invalid credentials.")
            return None
        print(f"Welcome back, {username}!")
        return username

    def deposit(self, username):
        amount = float(input("Enter amount to deposit: "))
        self.accounts[username]['balance'] += amount
        print(f"${amount:.2f} deposited. New balance: ${self.accounts[username]['balance']:.2f}")

    def withdraw(self, username):
        amount = float(input("Enter amount to withdraw: "))
        if self.accounts[username]['balance'] >= amount:
            self.accounts[username]['balance'] -= amount
            print(f"${amount:.2f} withdrawn. New balance: ${self.accounts[username]['balance']:.2f}")
        else:
            print("Insufficient funds.")

    def check_balance(self, username):
        balance = self.accounts[username]['balance']
        print(f"Your balance is: ${balance:.2f}")

    def transfer(self, username):
        recipient = input("Enter recipient username: ")
        if recipient not in self.accounts:
            print("Recipient account not found.")
            return
        amount = float(input("Enter amount to transfer: "))
        if self.accounts[username]['balance'] >= amount:
            self.accounts[username]['balance'] -= amount
            self.accounts[recipient]['balance'] += amount
            print(f"Transferred ${amount:.2f} to {recipient}.")
        else:
            print("Insufficient funds.")

    def main_menu(self):
        while True:
            print("\n==== Online Banking ====")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                user = self.login()
                if user:
                    self.user_menu(user)
            elif choice == '3':
                print("Thank you for using our service.")
                break
            else:
                print("Invalid option.")

    def user_menu(self, username):
        while True:
            print(f"\n--- {username}'s Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.check_balance(username)
            elif choice == '2':
                self.deposit(username)
            elif choice == '3':
                self.withdraw(username)
            elif choice == '4':
                self.transfer(username)
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    bank = Bank()
    bank.main_menu()
      
