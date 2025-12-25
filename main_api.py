from fastapi import FastAPI

print("Starting API server...")

from Presentation.API.transaction_apis import transaction_router
from Presentation.API.account_apis import account_router


app = FastAPI(title="Core Banking API")
app.include_router(transaction_router)
app.include_router(account_router)

@app.get("/say_hello")
def say_hello():
    print("say_hello called")
    return {"message":"Hello"}

