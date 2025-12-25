from fastapi import APIRouter,Query,Depends,HTTPException
from typing import List
from Presentation.API.dependency_injection import get_account_business
from BusinessLogic.account_business_logic import AccountBusinessLogic
from Presentation.API.DTOs.create_account_dto import CreateAccountDTO, UpdateAccountDTO
from Common.DTOs.response import Response as ServiceResponse

account_router = APIRouter(prefix="/api/v1/accounts",tags=["Accounts"])

@account_router.get("/")
def get_account(
    page_number: int = Query(1, ge=1),
    page_size: int = Query(15, ge=1, le=50),
    account_business: AccountBusinessLogic = Depends(get_account_business),
):
    response : ServiceResponse= account_business.get_account_list(page_number, page_size)
    if not response.success:
        raise HTTPException(status_code=400, detail=response.message)
    data_as_dict = [account.to_dict() for account in response.data]
    return data_as_dict
@account_router.post("/")
def new_account(
    account_dto: CreateAccountDTO,
    account_business: AccountBusinessLogic = Depends(get_account_business),
):
    response :ServiceResponse= account_business.create_account(customer_id=account_dto.customer_id,account_type_id=account_dto.account_type_id,initial_deposit=account_dto.initial_deposit,opening_date=account_dto.opening_date,)
    if not response.success:
        raise HTTPException(status_code=400,detail=response.message)
    return {"message":"Account Created."}
@account_router.put("/{account_id}")
def update_account(
    account_id: int,
    account_dto: UpdateAccountDTO,
    account_business: AccountBusinessLogic = Depends(get_account_business),
):
    response :ServiceResponse= account_business.update_account(account_id, account_dto)
    if not response.success:
        raise HTTPException(status_code=400,detail=response.message)
    return {"message": "Account updated."}
@account_router.delete("/{account_id}")
def block_account(
    account_id: int,
    account_business: AccountBusinessLogic = Depends(get_account_business),
):
    response :ServiceResponse= account_business.block_account(account_id)
    if not response.success:
        raise HTTPException(status_code=400,detail=response.message)
    return {"message": "Account Blocked."}
