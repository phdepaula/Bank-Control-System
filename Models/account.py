from Models.client import Client
from utils.helper import format_float_str_coin


class Account:
    counter: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.counter
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._calculate_total_balance
        Account.counter += 1

    def __str__(self: object) -> str:
        return f'Account number: {self.number}\nCLient: {self.client}\n' \
               f'Total balance: {format_float_str_coin(self.total_balance)}'

    @property
    def number(self: object) -> int:
        return self.__number

    @property
    def client(self: object) -> str:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, valor: float) -> None:
        self.__total_balance = valor

    @property
    def _calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self._calculate_total_balance
            print('Deposit made successfully!')
        else:
            print('Error when making deposit. Try again!')

    def withdraw(self: object, value: float) -> None:
        if not value < 0 and value < self.total_balance:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.limit = self.limit + remaining
                self.balance = 0
                self.total_balance = self._calculate_total_balance
                print('Withdrawal made successfully!')
        else:
            print('Withdrawal failed, insufficient balance. Try again!')

    def transfer(self: object, destiny: object, value: float) -> None:

        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
                destiny.balance = destiny.balance + value
                destiny.total_balance = destiny._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.balance = 0
                self.limit = self.limit + remaining
                self.total_balance = self._calculate_total_balance
                destiny.balance = destiny.balance + value
                destiny.total_balance = destiny._calculate_total_balance
        else:
            print('Transfer failed, insufficient balance. Try again!')
