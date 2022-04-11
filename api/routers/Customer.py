import DifferentFunctions
from fastapi import APIRouter
import json
from pydantic import BaseModel

router=APIRouter(prefix='/customer',tags=['customer'])

class customer(BaseModel):
    Customer_first_name: str
    Customer_last_name:str
    Customer_Phone:int
    Customer_email_id:str

@router.post('/add_customer')
def add_customer(cust: customer):
    return DifferentFunctions.add_customer(cust.Customer_first_name,cust.Customer_last_name,cust.Customer_Phone,cust.Customer_email_id)

@router.post('/update_customer')
def update_customer(id,request):
    req = json.loads(request)
    return DifferentFunctions.update_Customer(id,req)

@router.get('/get_all_customer')
def get_all_customer_data():
    return DifferentFunctions.get_all_customer_data()

@router.get('/get_particular_customer_info')
def get_specific_user_data(id):
    return DifferentFunctions.get_specific_user_data(id)
