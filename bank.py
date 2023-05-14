from typing import List
from time import sleep

from Models.client import Client
from Models.account import Account


accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('================================')
    print('==============ATM===============')
    print('===========Pedro Bank===========')
    print('================================')

    print('Select an option from the menu: ')
    print('1 - Create an Account')
    print('2 - Withdraw Money')
    print('3 - Make Deposit')
    print('4 - Make Transfer')
    print('5 - List Accounts')
    print('6 - Exit System')

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        make_withdraw()
    elif option == 3:
        make_deposit()
    elif option == 4:
        make_transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('Check back often!')
        sleep(2)
        exit(0)
    else:
        print('Invalid Option!')
        sleep(2)
        menu()


def create_account() -> None:
    print('================================')
    print('======Creating an Account======= ')
    print('================================')

    name: str = input('Client name: ')
    email: str = input('Customer email: ')
    cpf: str = input("Customer's CPF: ")
    birth_date: str = input("Customer's date of birth (dd/mm/aaaa): ")

    client: Client = Client(name, email, cpf, birth_date)

    account: Account = Account(client)

    accounts.append(account)

    print('Account created successfully!')
    print('Account details: ')
    print(account)
    print('================================')
    sleep(2)
    menu()


def make_withdraw() -> None:
    if len(accounts) > 0:
        print('================================')
        print('=======Making Withdrawal========')
        print('================================')

        number: int = int(input('Provide your account number: '))
        account: Account = search_account_by_number(number)

        if account:
            valor: float = float(input('Enter withdrawal amount: '))

            account.withdraw(valor)
        else:
            print(f'Account number not found {number} ...')
    else:
        print('There are no registered accounts yet!')
    sleep(2)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        print('================================')
        print('=========Making Deposit=========')
        print('================================')
    
        number: int = int(input('Provide your account number: '))

        account: Account = search_account_by_number(number)

        if account:
            value: float = float(input('Enter the deposit amount: '))

            account.deposit(value)
        else:
            print(f'No account was found with the number {number} ...')
    else:
        print('There are no registered accounts yet!')
    sleep(2)
    menu()


def make_transfer() -> None:
    
    if len(accounts) > 0:
        print('================================')
        print('========Making Transfer=========')
        print('================================')

        number_o: int = int(input('Provide your account number: '))

        account_o: Account = search_account_by_number(number_o)

        if account_o:
            number_d: int = int(input('Enter the destination account number: '))

            account_d: Account = search_account_by_number(number_d)

            if account_d:
                valor: float = float(input('Enter the amount of the transfer: '))

                account_o.transfer(account_d, valor)
            else:
                print(f'The destination account with number {number_d} was not found ...')
        else:
            print(f'No account was found with the number {number_o} ...')
    else:
        print('There are no registered accounts yet!')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('================================')
        print('========Account listing=========')
        print('================================')

        for account in accounts:
            print(account)
            print('================================')
            sleep(1)
    else:
        print('There are no registered accounts yet!')
    sleep(2)
    menu()


def search_account_by_number(number: int) -> Account:
    c: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == number:
                c = account
    return c


if __name__ == '__main__':
    main()