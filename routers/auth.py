from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from common import utils, oauth2
from data.models import CustomerLogin
from services import auth_service

auth_router = APIRouter(prefix='/user-login',tags=['Authentication'])

@auth_router.post('/')
def user_login(customer: OAuth2PasswordRequestForm=Depends()):
    user = auth_service.get_user(customer.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid customer.')
    if not utils.verify_password(customer.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials.')
    access_token = oauth2.create_access_token(data={"email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


admin_auth_router = APIRouter(prefix='/admin-login', tags=['Admin Authentication'])

@admin_auth_router.post('/')
def admin_login(admin: OAuth2PasswordRequestForm=Depends()):
    user = auth_service.get_admin(admin.username)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid admin.')
    if not utils.verify_password(admin.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials.')
    access_token = oauth2.create_admin_access_token(data={'username': user.username})
    return {"access_token": access_token, "token_type": "bearer"}

