from decimal import Decimal
from BusinessLogic.Validators.base_handler import BaseHandler
from Common.Entities.Enums.transaction_types import TransactionTypes
from datetime import datetime

class DailyTransactionLimitValidator(BaseHandler):
    MAX_DAILY_AMOUNT = 200000000

    def __init__(self, transaction_repository):
        super().__init__()
        self.transaction_repository = transaction_repository

    def handler(self, request):
        all_transactions = self.transaction_repository.get_all_transactions(request.account.account_id) or []
        today = datetime.now().date()
        total_today = sum(
            t.amount if t.transaction_type == TransactionTypes.Deposit else -t.amount
            for t in all_transactions
            if t.transaction_time.date() == today
        )
        new_total = total_today + Decimal(request.transaction_amount)

        if new_total > self.MAX_DAILY_AMOUNT:
            raise ValueError(f"Daily transaction limit exceeded! Max allowed: {self.MAX_DAILY_AMOUNT}")
        if self.next_handler:
            self.next_handler.handler(request)
