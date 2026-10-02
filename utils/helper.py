import datetime

def str_to_date(value:str) -> datetime.date:
    return datetime.datetime.strptime(value,"%d/%m/%Y").date()

def date_to_str(value:datetime.date) -> str:
    return value.strftime("%d/%m/%Y")

def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}"