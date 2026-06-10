class Bank_account:
    def __init__(self,account_number,balance,owner_name,date_opened='today'):
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
        self.date_opened=date_opened
    
    def deposit(self,amount):
        self.balance += amount
        print(f" successfully deposited ksh {amount}.")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"{self.owner_name} withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f" check balance){self.balance}.")

    def display_info(self):
        print(f"account_number:{self.account_number} ,balance:{self.balance} ,owner_name:{self.owner_name} ,date_opened{self.date_opened}")
        
    def close_account(self):
        del Bank_account
        print(f"Account {"Bank_account"} has been deleted.")
    print('------------------------------------------')
    



bank_account1=Bank_account(100,40000,"Jack",)
print(type(bank_account1))
print(bank_account1)
bank_account1.deposit(100000)
bank_account1.withdraw(60000)
bank_account1.check_balance()
bank_account1.close_account()


bank_account2=Bank_account(101,60000,"Juma",)
print(type(bank_account2))
print(bank_account1)
bank_account2.deposit(120000)
bank_account2.withdraw(60000)
bank_account2.check_balance()
bank_account2.close_account()




