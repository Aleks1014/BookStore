from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from common import utils, oauth2
from data.models import Customer, CustomerResponse
from services import customer_service

customers_router = APIRouter(prefix='/customers', tags=['Customer'])


@customers_router.post('/register', status_code=status.HTTP_201_CREATED)  # add response model?
def register(customer: Customer):
    hashed_password = utils.hash_password(customer.password)
    customer.password = hashed_password
    return customer_service.create_customer(customer)


# get profile

@customers_router.get('/account')
def get_account(user=Depends(oauth2.get_current_user)):
    customer = customer_service.get_account_info(user.email)
    if not customer:
        raise HTTPException(status_code=404, detail='User not found.')
    return (CustomerResponse(first_name=first_name, last_name=last_name, email=email)
            for first_name, last_name, email in customer)

# check orders

# update profile

# get wishlist

@customers_router.get('/wishlist')
def get_wishlist(user=Depends(oauth2.get_current_user)):
    user_id = customer_service.get_account_id(user.email)
    return customer_service.get_wishlist(user_id)

# get reviews
