import os

from Common.Repositories.itransaction_repository import ITransactionRepository
from Common.Repositories.iaccount_repository import IAccountRepository
from Common.DTOs.response import Response
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,Image as RLImage
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from Common.Entities.Enums.transaction_types import TransactionTypes
from BusinessLogic.Validators.CreateTransaction.account_status_validator import AccountStatusValidator
from BusinessLogic.Validators.CreateTransaction.positive_amount_validator import PositiveAmountValidator
from BusinessLogic.Validators.CreateTransaction.create_transaction_request import CreateTransactionRequest
from BusinessLogic.Validators.CreateTransaction.balance_validator import BalanceValidator
from BusinessLogic.Validators.CreateTransaction.daily_limit_validator import DailyTransactionLimitValidator
from Common.Entities.transaction import Transaction
from datetime import datetime


class TransactionBusinessLogic:
    def __init__(self, transaction_repository: ITransactionRepository, account_repository: IAccountRepository):
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository

    def get_transaction_list(self, account_id: int, page_number=1, page_size=15):
        transaction_list = self.transaction_repository.get_transactions(account_id, page_number, page_size)
        return Response(True, None, transaction_list)

    def get_all_transaction_list(self, account_id: int):
        try:
            transaction_list = self.transaction_repository.get_all_transactions(account_id)
            return Response(True, None, transaction_list)
        except:
            return Response(False, "Transaction Load Failed!", None)

    def export_to_pdf(self, account_id: int, file_path: str, logo_path: str):
        if not file_path:
            return Response(False, "File Path can not be Empty!", None)

        if not logo_path:
            return Response(False, "Logo path is required.", None)

        response = self.get_all_transaction_list(account_id)
        if not response or not response.success:
            return response if response is not None else Response(False, "Failed to load transactions", None)

        balance = sum([t.amount if t.transaction_type == TransactionTypes.Deposit else -t.amount for t in (response.data or [])])

        elements = []
        doc = SimpleDocTemplate(file_path)
        styles = getSampleStyleSheet()

        try:
            img_reader = ImageReader(logo_path)
            iw, ih = img_reader.getSize()
            desired_width = 150
            scale = desired_width / float(iw)
            desired_height = ih * scale

            img = RLImage(logo_path, width=desired_width, height=desired_height)
            elements.append(img)
            elements.append(Spacer(1, 6))
        except Exception as ex:
            return Response(False, f"Failed to read logo image: {ex}", None)

        doc_paragraph = Paragraph(text=f"Transaction Report (Balance: {balance})", style=styles["Title"])
        elements.append(doc_paragraph)
        elements.append(Spacer(1, 12))

        row_data = [(t.amount, t.transaction_time, t.transaction_type.name) for t in (response.data or [])]
        data = [("Amount", "Transaction Time", "Transaction Type")] + row_data
        data_table = Table(data)

        data_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]))

        elements.append(data_table)

        try:
            doc.build(elements)
        except Exception as ex:
            return Response(False, f"Failed to build PDF: {ex}", None)

        os.startfile(file_path)

        return Response(True, None, file_path)

    def create_transaction(self, amount: float, transaction_type: TransactionTypes, account_id: int):
        account = self.account_repository.get_account_by_id(account_id)
        transactions = self.transaction_repository.get_all_transactions(account_id) or []
        balance = sum([t.amount if t.transaction_type == TransactionTypes.Deposit else -t.amount for t in transactions])

        request = CreateTransactionRequest(account, amount, transaction_type, balance)

        account_validator = AccountStatusValidator()
        positive_validator = PositiveAmountValidator()
        balance_validator = BalanceValidator()
        daily_limit_validator = DailyTransactionLimitValidator(self.transaction_repository)

        account_validator.set_next(positive_validator)
        positive_validator.set_next(balance_validator)
        balance_validator.set_next(daily_limit_validator)

        try:
            account_validator.handler(request)
        except ValueError as error:
            return Response(False, error.args[0], None)

        new_transaction = Transaction(0, amount, datetime.now(), transaction_type.value, account_id)
        self.transaction_repository.insert_transaction(new_transaction)
        return Response(True, None, None)



