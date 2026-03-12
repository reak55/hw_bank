class BankAccount:
    def __init__(self,name,balance,secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    def verify(self, input__secret):

        return self.__secret == input__secret

    def transfer(self, amount, to_acc):
        if amount > self.__balance:
            print("Not enough balance!")
        else:
            self.__balance -= amount
            to_acc._BankAccount__balance += amount
            print("Transfer successful!")
            print(f"Your balance: {self.__balance}")

    def check_balance(self):
        print("Checking balance!")

        secret = input("Input ur password: ")

        if secret == self.__secret:
            print(f"Hola :{self.name}")
            print(f"Ur Balance is: {self.__balance}")
        else:
            print("Sorry ur password is incorrect")

    def withdraw(self):
        print("User is withdrawing")
        secret = input("Input ur password: ")
        print(f"ur balance is{self.__balance}")

        if secret == self.__secret:
            amount = float(input("Input ur amount: "))
            remain = self.__balance - amount

            if remain < 0:
                print("Ur balance is not enough")
            else:
                self.__balance = remain
                print("withdraw succsessfully...")
                print(f"Ur reamining balance is: {self.__balance}")
        else:
                print("we dont know you.")

    def deposit(self):
        print("==Deposit ur money==")
        secret = input("Input ur password: ")

        if secret == self.__secret:
            amount = float(input("Input ur money here: "))
            self.__balance += amount
            print("Deposit successful!!")
            print(f"Ur new balance is {self.__balance}")
        else:
            print("ur password is incorrect.")

class SavingAccount(BankAccount):
        def calculate_interest(self):
            print("Calculate interest")
            SavingAccount.__balance += 10
            print(f"ur balance now is {self._BankAccount__balance}")

class StudentbankAccount(BankAccount):
     def withdraw(self): 
        print ("===Student is withdrawing===")
        secret = input("Input ur password: ")
        
        if secret == self._BankAccount__secret:
            amount = float(input("input ur amount: "))

            if amount > 500:
                print("Student accoount can't withdraw more than 500$")
            else:
                remain = self._BankAccount__balance - amount

                if remain < 0:
                    print("Ur balance is not enough to withdraw")
                else: 
                    self._BankAccount__balance = remain
                    print("Withdraw succesful...")
                    print(f"Ur remaining balance is: {self._BankAccount__balance}")
                    
        else: 
            print("We don't know you.")

# PremiumSaving inherit from SavingAccount
class PremiumSaving(SavingAccount):

    # override deposit method (2% bonus every deposit)
    def deposit(self):
        print("==== Premium Deposit ====")
        secret = input("Input your secret number: ")

        if secret == self._BankAccount__secret:
            amount = float(input("Input deposit amount: "))

            bonus = amount * 0.02   # 2% bonus
            total = amount + bonus

            self._BankAccount__balance += total

            print(f"You received 2% bonus: {bonus}$")
            print(f"Your new balance is: {self._BankAccount__balance}")
        else:
            print("Sorry we don't know you.")


# BusinessAccount inherit from BankAccount
class BusinessAccount(BankAccount):

    def take_loan(self):
        print("==== Business Loan ====")
        secret = input("Input your secret number: ")

        if secret == self._BankAccount__secret:
            loan = float(input("Input loan amount: "))
            self._BankAccount__balance += loan
            print(f"Loan approved. Your new balance is: {self._BankAccount__balance}")
            print("====1khea ber ot song vinh kat dick joal!!====")
        else:
            print("Access denied.")

    accounts = {}
    current_user = None

    accounts["reak"] = BankAccount("reak", 5000,"5544")
    accounts["nami"] = BankAccount("nami", 2000,"2233")

    while True:
            print(''' ===ATM System===
              Choose Menu
        ==========================
        1. CREATE ACCOUNT
        2.LOGIN    
        3.CHECK BALANCE
        4.WITHDRAW
        5.DEPOSIT
        6.TRANSTER          
        7.LOGOUT          
        ===========================          
    ''')
    
            choice = input("Select Menu: ")
    
            if choice == "1":
                name = input("Input account name: ")
                if current_user in accounts:
                    print("Account name is exist.")
                    continue

                balance = float(input("Input initial balance: "))
                secret = input("Input ur secret: ")

                acc = BankAccount(name, balance,secret)
                accounts[name] = acc

                print("bank Account is create successfully!")

            elif choice == "2":
                name = input ("input account name: ")  
                secret = input("input ur secret PIN: ")

                if name in accounts and accounts[name].verify(secret):
                    print("")
                    print(f"Login success Welcome {name}! ")
                    print("")
                    current_user =accounts[name]
                    continue

                print("Invalid account name or secret")

            elif choice == "3":
                if current_user is None:
                    print("Please login first")
                    continue
                
                current_user.check_balance()


            elif choice == "4":
                if current_user is None:
                    print("Please login first")
                    continue
                
                amount = float(input("Input amount: "))
                current_user.withdraw()

            elif choice == "5":
                if current_user is None: 
                    print("login first")
                    continue
                
                amount_to_deposit = float(input("Input amount to deposit: "))
                current_user.deposit()

            elif choice == "6":
                if current_user is None:
                    print("Login first")
                    continue
                to_name = input("Input destination account name: ")
                if to_name in accounts and to_name != current_user.name:
                    to_acc = accounts[to_name]
                    amount = float(input("Input amount to transfer: "))
                    current_user.transfer(amount, to_acc)
                else:
                    print("account not found!")

            elif choice == "7":
                current_user = None
                print("Logout successfully!!")
        
        




reak = BankAccount(name="reak", balance=5000, secret="achko")
rong = BankAccount(name="rong", balance=2000, secret="ruk" )
    #reak.check_balance()
    #reak.withdraw()

peyly = SavingAccount(name="peyly", balance=5319, secret="123")
    #peyly.calculate_interest()
    #rong.check_balance()
#peyly.check_balance()

reak = StudentbankAccount(name="reak", balance=5000, secret="achko")
    #reak.withdraw()
    #reak.deposit()

reak = BusinessAccount(name="reak", balance=5000, secret="achko")
    #reak.take_loan()

reak = PremiumSaving(name="luffy", balance= 5000, secret= "3344")
    #reak.deposit()

reak = accounts()
