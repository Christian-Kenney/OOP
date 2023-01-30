class CheckingAccount:
    def __init__(self, name, address, account_number, balance):
        self.name = name
        self.address = address
        self.account_number = account_number
        self._balance = balance

    def withdraw(self, withdraw):
        if self._balance >= withdraw:
            self._balance -= withdraw
        else:
            print("Not enough money")


    def deposit(self, deposit):
        self._balance += deposit


    def get_balance(self):
        return self._balance


def main():
    account = CheckingAccount("Christian Kenney", "San Antonio, Texas", "000001", 10000)
    print("Balance:", account.get_balance())

    account.deposit(1000)
    print("Balance: ", account.get_balance())

    account.withdraw(20000)
    print("Balance:", account.get_balance())

    account.withdraw(3000)
    print("Balance:", account.get_balance())

if __name__ == "__main__":
    main()