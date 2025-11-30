from BusinessLogic.Validators.base_handler import BaseHandler

class PositiveAmountValidator(BaseHandler):
    def handler(self,request):
        if request.transaction_amount <10:
            raise ValueError("Invalid amount for new transaction.")
        if self.next_handler:
            self.next_handler.handler(request)