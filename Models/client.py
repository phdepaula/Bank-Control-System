from datetime import date

from utils.helper import date_para_str, str_para_date


class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, cpf: str, birth_date: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birth_date: date = str_para_date(birth_date)
        self.__registration_date: date = date.today()
        Client.counter += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def birth_date(self: object) -> str:
        return date_para_str(self.__birth_date)

    @property
    def registration_date(self: object) -> str:
        return date_para_str(self.__registration_date)

    def __str__(self: object) -> str:
        return f'Code: {self.code}\nName: {self.name}\nBirth date: {self.birth_date}\n' \
               f'Registration: {self.registration_date}'
