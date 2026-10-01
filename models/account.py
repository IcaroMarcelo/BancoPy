from .client import Client
from utils.helper import format_currency

class Account:
    counter:int = 1001
    
    def __init__(self,client:Client) -> None:
        self.__number = Account.counter
        Account.counter += 1
        
        self.__client = client
        self.__balance = 0.0
        self.__limit = 100.0
    @property
    def number(self) -> int:
        return self.__number
    
    @property
    def client(self) -> Client:
        return self.__client
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    @property
    def limit(self) -> float:
        return self.__limit    
    
    @property
    def total_balance(self) -> float:
        return self.__balance + self.__limit
    
    def deposit(self,value: float) -> None:
        if 0 < value:
            self.__balance += value
        else:
            print("Invalid deposit value.")
    
    def withdraw(self, value: float) -> bool:
        if value > 0 <= self.total_balance:
            self.__balance -= value
            return True
        else:
            print("Insufficient balance.")
            return False
    
    def transfer(self, destination: "Account", value: float) -> None:
        if self.withdraw(value):
            destination.deposit(value)
    
    def __str__(self) -> str:
        return (
        f"Account number: {self.number} | "
        f"Client: {self.client} | "
        f"Balance: {format_currency(self.balance)} | "
        f"Limit: {format_currency(self.limit)} | "
        f"Total balance: {format_currency(self.total_balance)}"
        )   