from fastapi import APIRouter
from fastapi.responses import FileResponse
from services import product_service


products_router = APIRouter(prefix='/products')

# @products_router.get('/cover/{cover_name}')
# async def visualize_image(cover_name: str):
#     cover_path = f'covers/{cover_name}.jpg'
#     return FileResponse(cover_path, media_type='image/jpeg')
#
# @products_router.get('/{id}')
# def get_book_by_id(id: int):
#     return product_service.get_book_by_id(id)



# leave review (needs to be signed?)

# add to cart (needs to be signed)

# search/filter books

# add to wishlist (needs to be signed)



