from fastapi import APIRouter, HTTPException

from data.models import ProductResponse
from services import product_service

products_router = APIRouter(prefix='/products')

@products_router.get('/{id}')
def get_book_by_id(id: int):
    return product_service.get_book_by_id(id)



# leave review (needs to be signed?)

# add to cart (needs to be signed)

# search/filter books

# add to wishlist (needs to be signed)

