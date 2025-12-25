from fastapi import APIRouter,Query,Depends,HTTPException
from Presentation.API.dependency_injection import get_transaction_business
from BusinessLogic.transaction_business_logic import TransactionBusinessLogic
from Presentation.API.DTOs.create_transaction_dto import CreateTransactionDTO
from Common.Entities.transaction import TransactionTypes

transaction_router = APIRouter(prefix="/api/v1/transactions",tags=["Transactions"])
@transaction_router.get("/")
def get_transactions(
        account_id:int,
        page_number:int=Query(1,ge=1),
        page_size:int=Query(15,le=20),
        transaction_business:TransactionBusinessLogic = Depends(get_transaction_business)):
    response = transaction_business.get_transaction_list(account_id,page_number,page_size)
    if not response.success:
        raise HTTPException(status_code=400,detail=response.message)
    data_as_dict = [transaction.to_dict() for transaction in response.data]
    return data_as_dict

@transaction_router.post("/")
def new_transaction(
        transaction_dto:CreateTransactionDTO,
        transaction_business= Depends(get_transaction_business)
        ):
    transaction_type = TransactionTypes(transaction_dto.transaction_type_id)
    response = transaction_business.create_transaction(transaction_dto.amount,transaction_type,transaction_dto.account_id)
    if not response.success:
        raise HTTPException(status_code=400,detail=response.message)
    return {"message":"Transaction Created."}