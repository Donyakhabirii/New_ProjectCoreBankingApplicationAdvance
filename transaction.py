from Common.Entities.Enums.transaction_types import TransactionTypes
class Transaction:
    def __init__(self,id,amount:float,transaction_time,transaction_type_id,account_id ):
        self.transaction_id = id
        self.amount = amount
        self.transaction_time = transaction_time
        self.transaction_type = TransactionTypes(transaction_type_id)
        self.account_id = account_id
    @classmethod
    def create_with_dict(cls,dict_data):
        return cls(
            dict_data.get("Id"),
            dict_data.get("Amount"),
            dict_data.get("TransactionTime"),
            dict_data.get("TransactionTypeId"),
            dict_data.get("AccountId")

        )
