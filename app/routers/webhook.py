import json

from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/webhook",
    tags=["webhook"],
    responses={404: {"description": "Not found"}},
)


@router.post("/new_user")
async def new_user_handler(request: Request):
    try:
        data = await request.json()
    except:
        data = {}
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return {"message": "Webhook received"}


@router.post("/payment")
async def payment_handler(request: Request):
    try:
        data = await request.json()
    except:
        data = {}
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return {"message": "Webhook received"}
