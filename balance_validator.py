from BusinessLogic.Validators.base_handler import BaseHandler
from Common.Entities.Enums.transaction_types import TransactionTypes

class BalanceValidator(BaseHandler):
    def handler(self,request):
        if request.transaction_type == TransactionTypes.Withdraw and request.transaction_amount > request.balance:
            raise ValueError("Balance not enough!")
        if self.next_handler:
            self.next_handler.handler(request)