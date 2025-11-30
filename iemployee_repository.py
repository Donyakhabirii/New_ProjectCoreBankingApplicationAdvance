import sqlite3
from abc import ABC,abstractmethod

class IEmployeeRepository(ABC):
    @abstractmethod
    def get_by_username_password(self,username:str,password:str):
        pass
