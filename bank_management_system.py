<<<<<<< HEAD
class Create_customer():
    customer_count=100
    def __init__(self,Name,Phone_number,Address):
        Create_customer.customer_count+=1
        self.customer_id=f"C{Create_customer.customer_count}"
        self.Name=Name
        self.Phone_number=Phone_number
        self.Address=Address
    def display(self):
        print("\n-----Customer Details -------")
        print(f"customer id: {self.customer_id}")
        print(f"Name: {self.Name}")
        print(f"Phone_Number:{self.Phone_number}")
        print(f"Address: {self.Address}")
class Account():
    account_number=1000000001
    def __init__(self,cid,pin,balance):
        Account.account_number+=1
        self.account_number=Account.account_number
        self.cid=cid
        self.__pin=pin
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited successfully")
        print(f"balance:{self.balance}")
    def show_balance(self):
        print(f"balance:{self.balance}")
class savings_account(Account):
    def withdraw(self,amount):
        if amount<=0:
            print("please enter amount greater than zero")
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("withdrawal successful")
            print("balance:",self.balance)
class current_account():
    def withdraw(self,amount):
        if amount<=0:
            print("amount entered should be greater than zero")
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("withdrawal successful")
            print(f"balance:{self.balance}")

customers={}
accounts={}
while True:
    print('''===========BANK MANAGEMENT SYSTEM=============
1.Create customer
2.Open Account
3.Deposit
4.Withdraw
5.Balance Enquiry
6.Exit''')

    try:
        choice=int(input("Enter your choice"))
        if choice==1:
            Name=input("Enter customer name:")
            if not Name.isalpha():
                raise Exception("Enter alphabets only")
            Phone_number=input("Enter phone number")
            if len(Phone_number)!=10 or not Phone_number.isdigit():
                raise Exception("Phone number must be exactly 10 digits")
            Address=input("Enter address")
            Account_1=Create_customer(Name,Phone_number,Address)
            customers[Account_1.customer_id]=Account_1
            print("customer created successfully.")
            Account_1.display()
            
        elif choice==2:
            customer_id=input("Enter customer id:")
            if customer_id not in customers:
                raise Exception("customers not found")
            print('''choose account type:
                    1.savings
                    2.current
              ''')
            choice=int(input("Enter the choice"))
            pin=input("set 4-digit pin")
            if len(pin)!=4 or not pin.isdigit():
                raise ValueError("Pin must be exactly 4 digits")
            balance=float(input("Enter initial deposit:"))
            if choice==1:
                account=savings_account(customer_id,pin,balance)
            elif choice==2:
                account=current_account(customer_id,pin,balance)
            else:
                print("invalid choice")
                continue
            accounts[account.account_number]=account
            print("Account created sucessfully")
            print("Account_Number:",account.account_number)
        elif choice==3:
            acc_no=int(input("Enter account number"))
            if acc_no in accounts:
                amount=float(input("Enter amount"))
                accounts[acc_no].deposit(amount)
            else:
                    print("account not found")
        elif choice==4:
            acc_no=int(input("Enter the account no:"))
            if acc_no in accounts:
                amount=float(input("Enter the amount:"))
                accounts[acc_no].withdraw(amount)
            else:
                print("invalid account no")
        elif choice==5:
            acc_no=int(input("enter account number:"))
            if acc_no in accounts:
                accounts[acc_no].show_balance()
            else:
                print("invalid account number")
        elif choice==6:
            print("Thankyou for using bank management system")
            break
        else:
            print("Invalid choice") 
    except ValueError as e:
            print("Error:",e) 
    except Exception as e:
            print("Error:",e)      
=======
class Create_customer():
    customer_count=100
    def __init__(self,Name,Phone_number,Address):
        Create_customer.customer_count+=1
        self.customer_id=f"C{Create_customer.customer_count}"
        self.Name=Name
        self.Phone_number=Phone_number
        self.Address=Address
    def display(self):
        print("\n-----Customer Details -------")
        print(f"customer id: {self.customer_id}")
        print(f"Name: {self.Name}")
        print(f"Phone_Number:{self.Phone_number}")
        print(f"Address: {self.Address}")
class Account():
    account_number=1000000001
    def __init__(self,cid,pin,balance):
        Account.account_number+=1
        self.account_number=Account.account_number
        self.cid=cid
        self.__pin=pin
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited successfully")
        print(f"balance:{self.balance}")
    def show_balance(self):
        print(f"balance:{self.balance}")
class savings_account(Account):
    def withdraw(self,amount):
        if amount<=0:
            print("please enter amount greater than zero")
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("withdrawal successful")
            print("balance:",self.balance)
class current_account():
    def withdraw(self,amount):
        if amount<=0:
            print("amount entered should be greater than zero")
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("withdrawal successful")
            print(f"balance:{self.balance}")

customers={}
accounts={}
while True:
    print('''===========BANK MANAGEMENT SYSTEM=============
1.Create customer
2.Open Account
3.Deposit
4.Withdraw
5.Balance Enquiry
6.Exit''')

    try:
        choice=int(input("Enter your choice"))
        if choice==1:
            Name=input("Enter customer name:")
            if not Name.isalpha():
                raise Exception("Enter alphabets only")
            Phone_number=input("Enter phone number")
            if len(Phone_number)!=10 or not Phone_number.isdigit():
                raise Exception("Phone number must be exactly 10 digits")
            Address=input("Enter address")
            Account_1=Create_customer(Name,Phone_number,Address)
            customers[Account_1.customer_id]=Account_1
            print("customer created successfully.")
            Account_1.display()
            
        elif choice==2:
            customer_id=input("Enter customer id:")
            if customer_id not in customers:
                raise Exception("customers not found")
            print('''choose account type:
                    1.savings
                    2.current
              ''')
            choice=int(input("Enter the choice"))
            pin=input("set 4-digit pin")
            if len(pin)!=4 or not pin.isdigit():
                raise ValueError("Pin must be exactly 4 digits")
            balance=float(input("Enter initial deposit:"))
            if choice==1:
                account=savings_account(customer_id,pin,balance)
            elif choice==2:
                account=current_account(customer_id,pin,balance)
            else:
                print("invalid choice")
                continue
            accounts[account.account_number]=account
            print("Account created sucessfully")
            print("Account_Number:",account.account_number)
        elif choice==3:
            acc_no=int(input("Enter account number"))
            if acc_no in accounts:
                amount=float(input("Enter amount"))
                accounts[acc_no].deposit(amount)
            else:
                    print("account not found")
        elif choice==4:
            acc_no=int(input("Enter the account no:"))
            if acc_no in accounts:
                amount=float(input("Enter the amount:"))
                accounts[acc_no].withdraw(amount)
            else:
                print("invalid account no")
        elif choice==5:
            acc_no=int(input("enter account number:"))
            if acc_no in accounts:
                accounts[acc_no].show_balance()
            else:
                print("invalid account number")
        elif choice==6:
            print("Thankyou for using bank management system")
            break
        else:
            print("Invalid choice") 
    except ValueError as e:
            print("Error:",e) 
    except Exception as e:
            print("Error:",e)      
>>>>>>> db76ca4f307bdc8ebb9759e7e6725c52392f6028
