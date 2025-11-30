from Presentation.view_manager import ViewManager
from BusinessLogic.employee_business_logic import EmployeeBusinessLogic
#from DataAccess.Repositories.SQLite.employee_repository import SQLiteEmployeeRepository
from DataAccess.Repositories.SQLServer.sql_server_employee_repository import SQLServerEmployeeRepository
from BusinessLogic.account_business_logic import AccountBusinessLogic
from DataAccess.Repositories.SQLServer.sql_server_account_repository import SQLServerAccountRepository
from BusinessLogic.transaction_business_logic import TransactionBusinessLogic
from DataAccess.Repositories.SQLServer.sql_server_transaction_repository import SQLServerTransactionRepository
#employee_repository = SQLiteEmployeeRepository()
employee_repository = SQLServerEmployeeRepository()
employee_business_logic = EmployeeBusinessLogic(employee_repository)

account_repository=SQLServerAccountRepository()
account_business_logic=AccountBusinessLogic(account_repository)

transaction_repository = SQLServerTransactionRepository()
transaction_business = TransactionBusinessLogic(transaction_repository,account_repository)


ViewManager(
    employee_business_logic,
    account_business_logic,
    transaction_business
)
