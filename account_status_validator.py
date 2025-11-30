from BusinessLogic.Validators.base_handler import BaseHandler

class AccountStatusValidator(BaseHandler):
    def handler(self,request):
        if request.account.account_status!=1:
            raise ValueError("This account can to be create new transaction!")
        if self.next_handler:
            self.next_handler.handler(request)
            print()