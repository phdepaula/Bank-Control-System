from datetime import date
from datetime import datetime


def date_para_str(date: date) -> str:
    return date.strftime('%d/%m/%Y')


def str_para_date(date: str) -> date:
    return datetime.strptime(date, '%d/%m/%Y')


def format_float_str_coin(value: float) -> str:
    return f'$ {value:,.2f}'
