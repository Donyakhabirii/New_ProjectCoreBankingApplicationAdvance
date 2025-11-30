from abc import ABC,abstractmethod
from Common.Entities.transaction import Transaction
from datetime import datetime
class ITransactionRepository(ABC):
    @abstractmethod
    def get_transactions(self,account_id: int,page_number = 1,page_size = 15):
        pass
    @abstractmethod
    def insert_transaction(self,new_transaction:Transaction):
        pass
    @abstractmethod
    def get_all_transactions(self, account_id: int):
        pass
    @abstractmethod
    def get_total_transactions_today(self,account_id:int):
        pass
