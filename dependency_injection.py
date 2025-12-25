import os
from dotenv import load_dotenv
from DataAccess.Repositories.SQLServer.sql_server_transaction_repository import SQLServerTransactionRepository
from DataAccess.Repositories.SQLServer.sql_server_account_repository import SQLServerAccountRepository
from BusinessLogic.transaction_business_logic import TransactionBusinessLogic
from BusinessLogic.account_business_logic import AccountBusinessLogic

load_dotenv()
sqlserver_server_name= os.getenv("SQLSERVER_SERVER_NAME")
sqlserver_database_name = os.getenv("SQLSERVER_DATABASE_NAME")

def get_transaction_business():
    transaction_repository=SQLServerTransactionRepository(sqlserver_server_name, sqlserver_database_name)
    account_repository=SQLServerAccountRepository(sqlserver_server_name, sqlserver_database_name)
    business= TransactionBusinessLogic(transaction_repository,account_repository)
    return business
def get_account_business():
    account_repository = SQLServerAccountRepository(sqlserver_server_name, sqlserver_database_name)
    business = AccountBusinessLogic(account_repository)
    return business