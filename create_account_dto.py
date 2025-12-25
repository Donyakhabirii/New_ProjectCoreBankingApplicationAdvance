from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class CreateAccountDTO(BaseModel):
    customer_id: int = Field(ge=1)
    account_type_id: int = Field(ge=1)
    initial_deposit: float = Field(ge=0)
    opening_date: Optional[date] = None

class UpdateAccountDTO(BaseModel):
    account_type_id: Optional[int] = Field(None, ge=1)
    account_status_id: Optional[int] = Field(None, ge=1)
    account_number: Optional[str] = None
    opening_date: Optional[date] = None


