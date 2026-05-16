"""Custom exceptions for the Magic ATM exercise."""


class BankError(Exception):
    """Base class for all business-rule ATM errors."""


class EmptyAccountNameError(BankError):
    """Raised when an account name is empty."""


class DuplicateAccountError(BankError):
    """Raised when trying to create an account that already exists."""


class AccountNotFoundError(BankError):
    """Raised when an account does not exist."""


class InvalidAmountError(BankError):
    """Raised when an amount is zero, negative, or otherwise invalid."""


class InsufficientFundsError(BankError):
    """Raised when an account does not have enough money."""


class TransferToSameAccountError(BankError):
    """Raised when sender and receiver are the same account."""
