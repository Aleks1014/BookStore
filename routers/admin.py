from fastapi import APIRouter, status, Depends

from common import utils, oauth2
from data.models import Author, Category, Publisher, Product, Admin
from services import admin_service

admin_router = APIRouter(prefix='/admin', tags=['Admin'])


@admin_router.post('/register', status_code=status.HTTP_201_CREATED)  # add response model?
def register(new_admin: Admin, current_admin=Depends(oauth2.get_current_admin)):
    hashed_password = utils.hash_password(new_admin.password)
    new_admin.password = hashed_password
    return admin_service.create_admin(new_admin)


@admin_router.post('/author')
def add_author(author: Author, admin=Depends(oauth2.get_current_admin)):
    return admin_service.add_author(author)


@admin_router.post('/category')
def add_category(category: Category, admin=Depends(oauth2.get_current_admin)):
    return admin_service.add_category(category)


@admin_router.post('/publisher')
def add_publisher(publisher: Publisher, admin=Depends(oauth2.get_current_admin)):
    return admin_service.add_publisher(publisher)


@admin_router.post('/book')
def add_book(book: Product, admin=Depends(oauth2.get_current_admin)):
    return admin_service.add_book(book)
