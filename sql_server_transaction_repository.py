import pymssql
from datetime import datetime
from Common.Entities.transaction import Transaction
from Common.Repositories.itransaction_repository import ITransactionRepository

class SQLServerTransactionRepository(ITransactionRepository):
    def create_connection(self):
        connection = pymssql.connect(host="localhost",database="corebankingDB")
        return connection

    def get_transactions(self, account_id, page_number=1, page_size=15):
        transaction_list = []
        skip_rows = (page_number - 1) * page_size
        with self.create_connection() as connection:
            cursor = connection.cursor(as_dict=True)
            cursor.execute("""
                SELECT Id, Amount, TransactionTime, TransactionTypeId, AccountId
                FROM [Transactions]
                WHERE AccountId = %d
                ORDER BY TransactionTime DESC
                OFFSET %d ROWS
                FETCH NEXT %d ROWS ONLY
            """, (account_id, skip_rows, page_size))
            data = cursor.fetchall()
            for row in data:
                try:
                    transaction= Transaction.create_with_dict(row)
                except Exception:
                    transaction = Transaction(
                    row.get("Id"),
                    row.get("Amount"),
                    row.get("TransactionTime"),
                    row.get("TransactionTypeId"),
                    row.get("AccountId")
                )
                transaction_list.append(transaction)
        return transaction_list
    def get_all_transactions(self,account_id:int):
        transaction_list = []
        with self.create_connection() as connection:
            cursor = connection.cursor(as_dict=True)
            cursor.execute("""
                        SELECT Id
                        , Amount
                        , TransactionTime
                        , TransactionTypeId
                        , AccountId
                        FROM [Transactions]
                        WHERE AccountId = %s
                        ORDER BY TransactionTime DESC
                        """, (account_id,))
            data = cursor.fetchall()
            for row in data:
                try:
                    transaction = Transaction.create_with_dict(row)
                except Exception:
                    transaction = Transaction(
                        row.get("Id"),
                        row.get("Amount"),
                        row.get("TransactionTime"),
                        row.get("TransactionTypeId"),
                        row.get("AccountId")
                )
                transaction_list.append(transaction)
        return transaction_list

    def insert_transaction(self,new_transaction:Transaction):
        with self.create_connection() as connection:
            cursor = connection.cursor(as_dict=True)
            cursor.execute("""
            INSERT Transactions(Amount,TransactionTime,TransactionTypeId,AccountId)
            VALUES (%s,%s,%s,%s)""",(new_transaction.amount,
                                     new_transaction.transaction_time,
                                     new_transaction.transaction_type.value,
                                     new_transaction.account_id))
            connection.commit()


    def get_total_transactions_today(self, account_id: int):
        transaction_list = self.get_all_transactions(account_id) or []
        today = datetime.now().date()
        total = 0
        for t in transaction_list:
            tt = getattr(t, "transaction_time", None)
            try:
                tt_date = tt.date() if tt is not None else None
            except Exception:
                tt_date = None
            if tt_date == today:
                total += t.amount
        return total