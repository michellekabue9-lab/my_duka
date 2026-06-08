class bank_account:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
        self.date_opened=date_opened
    
    def deposit(self,amount):
        print(f" successfully deposited ksh {amount}.")
    
    def withdraw(self,amount):
        print(f" successfull withdraw ksh {amount}.")


    def check_balance(self):
        print(f" check balance){self.balance}.")

    def display_info(self):
        print(f"account_number:{self.account_number} ,balance:{self.balance} ,owner_name:{self.owner_name} ,date_opened{self.date_opened}")
        print('___bank_Details___')
        print('______________________________________')

# Student1=Student("Jack",20,"s001","Computer")
# print(type(Student1))
# print(Student1)
# Student1.display_info()
# Student1.study("002")
# Student1.eat("rice")
# Student1.sleep("12.00pm")

bank_account1=bank_account(100,40000,"Jack","12-06-2025")
print(type(bank_account1))
print(bank_account1)
bank_account1.deposit(100000)
bank_account1.withdraw(60000)
bank_account1.check_balance()


bank_account2=bank_account(101,60000,"Jack","12-06-2025")
print(type(bank_account2))
print(bank_account1)
bank_account2.deposit(120000)
bank_account2.withdraw(60000)
bank_account2.check_balance()




