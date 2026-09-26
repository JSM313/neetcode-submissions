class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_account = 0
    total_balance = 0
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_account += 1
        BankAccount.total_balance += balance
    
    def get_details(self):
        print(f"{self.name}'s balance: ${self.balance}")
    

    


# TODO: Create two accounts
alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
alice_account.get_details()
bob_account.get_details()
print(f"Total Accounts: {BankAccount.total_account}")
print(f"Total Balance: ${BankAccount.total_balance}")

