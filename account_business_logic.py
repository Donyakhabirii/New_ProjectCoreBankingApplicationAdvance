from Common.Repositories.iaccount_repository import IAccountRepository
from Common.DTOs.response import Response
class AccountBusinessLogic:
    def __init__(self,account_repository:IAccountRepository):
         self.account_repository = account_repository
    def get_account_list(self,page_number = 1,page_size = 15):
        try:
            account_list = self.account_repository.get_accounts(page_number,page_size)
            return Response(True,None,account_list)
        except:
            return Response(False,"Loade Account List Failed!",None)



