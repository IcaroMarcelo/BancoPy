from models.client import Client
from models.account import Account  

def create_account(accounts: list[Account]) -> None:
    name: str = input("Enter your name: ")
    email: str = input("Enter your email: ")
    cpf: str = input("Enter your CPF: ")
    birth_date: str = input("Enter your birth date (DD/MM/YYYY): ")
    client = Client(name,email,cpf,birth_date)
    account = Account(client)
    accounts.append(account)
    
def find_account(accounts: list[Account],account_number: int) -> Account | None:
    for account in accounts:
        if account.number == account_number:
            return account
    return None

def deposit(accounts: list[Account]) -> None:
    account_number: int = int(input("Enter account number: "))
    
    account = find_account(accounts, account_number)
    
    if account is not None:
        value = float(input("Enter value: "))
        account.deposit(value)
    else:
        print("Account not found!")

def withdraw(accounts: list[Account]) -> None:
    account_number: int = int(input("Enter account number: "))
    
    account = find_account(accounts, account_number)
    
    if account is not None:
        value: float = float(input("Enter value: "))
        account.withdraw(value)
    else:
        print("Account not found!")

def transfer(accounts: list[Account]) -> None:
    source_number: int = int(input("Enter source account number: "))
    source_account = find_account(accounts, source_number)

    destination_number: int = int(input("Enter destination account number: "))
    destination_account = find_account(accounts, destination_number)

    if source_account is not None and destination_account is not None:
        value: float = float(input("Enter value: "))
        source_account.transfer(destination_account, value)
    else:
        print("Account not found!")

def list_accounts(accounts:list[Account]) -> None:
    if not accounts:
        print('No accounts registered')
    else:
        for account in accounts:
            print(account)

def main() -> None:
    accounts: list[Account] = []
    
    
    while True:
        print("=== BANCOPY ===")
        print("1 - Create account")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Transfer")
        print("5 - List accounts")
        print("6 - Exit")
        
        choice: int = int(input("Choose an option: "))
    
        if choice == 1:
            create_account(accounts)
        elif choice == 2:
            deposit(accounts)
        elif choice == 3:
            withdraw(accounts)
        elif choice == 4:
            transfer(accounts)
        elif choice == 5:
            list_accounts(accounts)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main()