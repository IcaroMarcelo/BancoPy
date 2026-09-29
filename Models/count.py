import datetime
from Utils.Helper import str_to_date

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
        