class BankAccount:
    def __init__(self, acc_no, name, balance, pin):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance      # Encapsulation
        self.__pin = pin              # Encapsulation

    def verify_pin(self, pin):
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.__balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if amount > self.__balance:
            raise ValueError("Insufficient Balance.")

        self.__balance -= amount
        print(f"₹{amount} withdrawn successfully.")


# Inheritance
class ATM(BankAccount):

    def login(self):
        try:
            pin = int(input("Enter 4-digit PIN: "))

            if self.verify_pin(pin):
                print("\nLogin Successful")
                self.menu()
            else:
                print("Incorrect PIN")

        except ValueError:
            print("PIN should contain only numbers.")

    def menu(self):

        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("Available Balance: ₹", self.get_balance())

                elif choice == 2:
                    amount = float(input("Enter Deposit Amount: "))
                    self.deposit(amount)

                elif choice == 3:
                    amount = float(input("Enter Withdrawal Amount: "))
                    self.withdraw(amount)

                elif choice == 4:
                    print("Thank you for using ATM.")
                    break

                else:
                    print("Invalid Choice")

            except ValueError as e:
                print("Error:", e)

            except Exception as e:
                print("Unexpected Error:", e)


# Main Program
account = ATM(
    acc_no=123456789,
    name="Srija",
    balance=10000,
    pin=1234
)

account.login()