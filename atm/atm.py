"""Skeleton for the Magic ATM Simulator exercise.

Implement the TODOs yourself. Keep business logic in the first section and
user interaction in the second section.
"""

import os

from exceptions import (
    AccountNotFoundError,
    BankError,
    DuplicateAccountError,
    EmptyAccountNameError,
    InsufficientFundsError,
    InvalidAmountError,
    TransferToSameAccountError,
)


Accounts = dict[str, float]


# -------------------------
# Business logic functions
# -------------------------


def create_account(accounts: Accounts, name: str) -> None:
    """Create a new account with a starting balance of 0."""
    # TODO: clean/validate the account name.
    name = name.strip()
    # TODO: raise EmptyAccountNameError if the name is empty.
    if not name:
        raise EmptyAccountNameError()
    # TODO: raise DuplicateAccountError if the account already exists.
    if name in accounts:
        raise DuplicateAccountError(name)
    # TODO: add the account to the accounts dictionary with balance 0.
    accounts[name] = 0.0


def deposit(accounts: Accounts, name: str, amount: float) -> None:
    """Deposit money into an existing account."""
    # TODO: raise AccountNotFoundError if the account does not exist.
    if name not in accounts:
        raise AccountNotFoundError(name)
    # TODO: raise InvalidAmountError if amount is not greater than 0.
    if amount <= 0:
        raise InvalidAmountError(amount)
    # TODO: increase the account balance.
    accounts[name] += amount


def withdraw(accounts: Accounts, name: str, amount: float) -> None:
    """Withdraw money from an existing account."""
    # TODO: raise AccountNotFoundError if the account does not exist.
    if name not in accounts:
        raise AccountNotFoundError(name)
    # TODO: raise InvalidAmountError if amount is not greater than 0.
    if amount <= 0:
        raise InvalidAmountError(amount)
    # TODO: raise InsufficientFundsError if the balance is too low.
    if accounts[name] < amount:
        raise InsufficientFundsError(name, accounts[name], amount)
    # TODO: decrease the account balance.
    accounts[name] -= amount


def transfer(accounts: Accounts, sender: str, receiver: str, amount: float) -> None:
    """Transfer money from one account to another account."""
    # TODO: raise AccountNotFoundError if either account does not exist.
    if sender not in accounts:
        raise AccountNotFoundError(sender)
    if receiver not in accounts:
        raise AccountNotFoundError(receiver)
    # TODO: raise TransferToSameAccountError if sender and receiver match.
    if sender == receiver:
        raise TransferToSameAccountError(sender)
    # TODO: raise InvalidAmountError if amount is not greater than 0.
    if amount <= 0:
        raise InvalidAmountError(amount)
    # TODO: raise InsufficientFundsError if sender balance is too low.
    if accounts[sender] < amount:
        raise InsufficientFundsError(sender, accounts[sender], amount)
    # TODO: move the money from sender to receiver.
    accounts[sender] -= amount
    accounts[receiver] += amount


def show_balance(accounts: Accounts, name: str) -> float:
    """Return the balance for an existing account."""
    # TODO: raise AccountNotFoundError if the account does not exist.
    if name not in accounts:
        raise AccountNotFoundError(name)
    # TODO: return the account balance.
    return accounts[name]


def list_accounts(accounts: Accounts) -> None:
    """Optional stretch goal: display all accounts and balances."""
    # TODO: implement this only if you want the Level 1 extension.
    for name, balance in accounts.items():
        print(f"{name}: ${balance:.2f}")


# -------------------------
# User interaction helpers
# -------------------------


def print_menu() -> None:
    """Print the main menu options."""
    print()
    print("Magic ATM Simulator")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check balance")
    print("6. List accounts")
    print("7. Exit")


def clear_terminal() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def read_amount(prompt: str) -> float:
    """Read an amount from the user and convert it to a number."""
    # TODO: use input(prompt) to read text from the user.
    text = float(input(prompt))
    # TODO: convert the text to float.
    # TODO: let ValueError happen here so the menu can catch it.
    return text


def handle_create_account(accounts: Accounts) -> None:
    """Ask for account details and call create_account."""
    # TODO: ask the user for the account name.
    input_name = input("Enter account name: ")
    # TODO: call create_account(accounts, name).
    create_account(accounts, input_name)


def handle_deposit(accounts: Accounts) -> None:
    """Ask for deposit details and call deposit."""
    # TODO: ask the user for the account name.
    name = input("Enter account name: ")
    # TODO: use read_amount() to ask for the amount.
    amount = read_amount("Enter deposit amount: ")
    # TODO: call deposit(accounts, name, amount).
    deposit(accounts, name, amount)


def handle_withdraw(accounts: Accounts) -> None:
    """Ask for withdrawal details and call withdraw."""
    # TODO: ask the user for the account name.
    name = input("Enter account name: ")
    # TODO: use read_amount() to ask for the amount.
    amount = read_amount("Enter withdrawal amount: ")
    # TODO: call withdraw(accounts, name, amount).
    withdraw(accounts, name, amount)


def handle_transfer(accounts: Accounts) -> None:
    """Ask for transfer details and call transfer."""
    # TODO: ask the user for the sender account.
    sender = input("Enter sender account name: ")
    # TODO: ask the user for the receiver account.
    receiver = input("Enter receiver account name: ")
    # TODO: use read_amount() to ask for the amount.
    amount = read_amount("Enter transfer amount: ")
    # TODO: call transfer(accounts, sender, receiver, amount).
    transfer(accounts, sender, receiver, amount)


def handle_show_balance(accounts: Accounts) -> None:
    """Ask for an account name and display its balance."""
    # TODO: ask the user for the account name.
    name = input("Enter account name: ")
    # TODO: call show_balance(accounts, name).
    balance = show_balance(accounts, name)
    # TODO: print the returned balance.
    print(f"Balance for {name}: ${balance:.2f}")

def run_menu() -> None:
    """Run the main menu loop."""
    accounts: Accounts = {}

    while True:
        print_menu()
        choice = input("Choose an option: ")

        try:
            # TODO: call the correct handler based on choice.
            match choice:
                case "1":
                    handle_create_account(accounts)
                case "2":
                    handle_deposit(accounts)
                case "3":
                    handle_withdraw(accounts)
                case "4":
                    handle_transfer(accounts)
                case "5":
                    handle_show_balance(accounts)
                case "6":
                    list_accounts(accounts)
                case "7":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")

        except ValueError:
            # TODO: handle invalid number conversion from read_amount().
            print("Invalid amount. Please enter a valid number.")
        except BankError:
            # TODO: handle your custom business-rule exceptions.
            print("Error occurred while processing the transaction.")
        else:
            # TODO: add code that should run only when no exception happened.
            print("Action completed successfully.")
        finally:
            if choice != "6":
                print("Returning to main menu...")
                input("Press Enter to continue...")
                clear_terminal()


if __name__ == "__main__":
    run_menu()
