from abc import ABC,abstractmethod
class IAccountRepository(ABC):
    @abstractmethod
    def get_accounts(self,page_number = 1,page_size = 15):
        pass
    @abstractmethod
    def get_account_by_id(self,account_id):
        pass