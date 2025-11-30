from Common.Entities.customer import Customer

class Account:
    def __init__(self,
                 id,
                 account_number,
                 opening_date,
                 account_type,
                 account_status,
                 customer:Customer):
        self.account_id = id
        self.account_number = account_number
        self.opening_date = opening_date
        self.account_type = account_type
        self.account_status = account_status
        self.customer = customer

    @classmethod
    def create_with_dict(cls,dict_data,customer):
        return cls(
            dict_data.get("AccountId"),
            dict_data.get("AccountNumber"),
            dict_data.get("OpeningDate"),
            dict_data.get("AccountTypeId"),
            dict_data.get("AccountStatusId"),
            customer
        )