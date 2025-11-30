from dataclasses import dataclass
from Common.Entities.account import Account
from Common.Entities.Enums.transaction_types import TransactionTypes


@dataclass
class CreateTransactionRequest:
    account: Account
    transaction_amount: float
    transaction_type: TransactionTypes
    balance: float
