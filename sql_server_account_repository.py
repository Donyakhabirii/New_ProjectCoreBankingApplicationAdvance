import pymssql
from Common.Repositories.iaccount_repository import IAccountRepository
from Common.Entities.account import Account
from Common.Entities.customer import Customer
class SQLServerAccountRepository(IAccountRepository):
    def create_connection(self):
        connection =  pymssql.connect(host="localhost",database="corebankingDB")
        return connection
    def get_accounts(self, page_number=1, page_size=15):
        account_list = []
        skip_rows = (page_number-1)*page_size
        with self.create_connection() as connection:
            cursor = connection.cursor(as_dict=True)
            cursor.execute("""
            select Account.Id AS AccountId
            ,		AccountNumber 
            ,		OpeningDate
            ,		AccountTypeId
            ,		AccountStatusId
            ,		Customer.Id AS CustomerId
            ,		Customer.FirstName
            ,		Customer.LastName
            ,		Customer.PhoneNumber
            ,		Customer.BirthDate
            ,		Customer.Gender
            From	Account
            Inner	Join
                    Customer
            ON		Account.CustomerId = Customer.Id
            Order   By OpeningDate DESC
            Offset  %d Rows
            Fetch   Next    %d Row Only""",(skip_rows,page_size))
            data = cursor.fetchall()
            for row in data:
                #customer = Customer(
                #    row.get("CustomerId"),
                #    row.get("FirstName"),
                #    row.get("LastName"),
                #    row.get("PhoneNumber"),
                #    row.get("BirthDate"),
                #    row.get("Gender")
                #)
                customer = Customer.create_with_dict(row)
                #account = Account(
                #    row.get("AccountId"),
                #    row.get("AccountNumber"),
                #    row.get("OpeningDate"),
                #    row.get("AccountTypeId"),
                #    row.get("AccountStatusId"),
                #    customer
                #)
                account = Account.create_with_dict(row,customer)
                account_list.append(account)
        return account_list
    def get_account_by_id(self,account_id:int):
        with self.create_connection() as connection:
            cursor = connection.cursor(as_dict=True)
            cursor.execute("""
            select Account.Id AS AccountId
            ,		AccountNumber 
            ,		OpeningDate
            ,		AccountTypeId
            ,		AccountStatusId
            ,		Customer.Id AS CustomerId
            ,		Customer.FirstName
            ,		Customer.LastName
            ,		Customer.PhoneNumber
            ,		Customer.BirthDate
            ,		Customer.Gender
            From	Account
            Inner	Join
                    Customer
            ON		Account.CustomerId = Customer.Id
            Where   Account.Id         = %d""",account_id)
            row = cursor.fetchone()
            if row:
                #customer = Customer(
                #    row.get("CustomerId"),
                #    row.get("FirstName"),
                #    row.get("LastName"),
                #    row.get("PhoneNumber"),
                #    row.get("BirthDate"),
                #    row.get("Gender")
                #)
                customer = Customer.create_with_dict(row)
                #account = Account(
                #    row.get("AccountId"),
                #    row.get("AccountNumber"),
                #    row.get("OpeningDate"),
                #    row.get("AccountTypeId"),
                #    row.get("AccountStatusId"),
                #    customer
                #)
                account = Account.create_with_dict(row, customer)
                return account











