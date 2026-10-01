import datetime
from utils.helper import date_to_str,str_to_date

class Client:
    counter: int = 101
    
    def __init__(self,name:str,email:str,cpf:str,birth_date:str) -> None:
        self.__name = name
        self.__email = email
        self.__cpf = cpf
        self.__birth_date = str_to_date(birth_date)
        self.__code = Client.counter
        Client.counter += 1  
        self.__registration_date = datetime.date.today()
        
    @property
    def code(self) -> int:
        return self.__code
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @property
    def birth_date(self) -> datetime.date:
        return self.__birth_date
    
    @property
    def registration_date(self) -> datetime.date:
        return self.__registration_date
    
    def __str__(self) -> str:
        return f"Code: {self.code} | Name: {self.name} | Email: {self.email} | CPF: {self.cpf} | birth_date: {date_to_str(self.birth_date)} | registration_date: {date_to_str(self.registration_date)}"
        