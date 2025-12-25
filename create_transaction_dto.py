from pydantic import BaseModel,Field

class CreateTransactionDTO(BaseModel):
    account_id : int = Field(ge=1)
    amount : float = Field(ge=10)
    transaction_type_id :int