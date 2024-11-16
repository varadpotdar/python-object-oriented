class Account:
    def __init__(self, account_number, account_type, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.initial_balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            self.initial_balance = self.initial_balance + amount
            print(f'Deposited {amount}')
            print(f'New Balance is: {self.initial_balance}')
        else:
            print(f'{amount} is an invalid amount.')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.initial_balance:
            self.initial_balance = self.initial_balance - amount
            print(f'withdrswal: {amount}')
            print(f'New Balance: {self.initial_balance}')
        else:
            if amount < 0:
                print(f'{amount} is an invalid amount.')
            else:
                print('Insufficient funds.')
                print('Current balance is {self.initial_balance}')

my_account = Account('123-456','savings',1_000.00) 

my_account.account_number
print(f'account number is:{my_account.account_number}')
my_account.account_type
print(f'account type is:{my_account.account_type}')
my_account.initial_balance
print(f'balance is:{my_account.initial_balance}')

my_account.deposit(2500)



             
       