import uvicorn
from fastapi import FastAPI
from routers.admin import admin_router
from routers.auth import auth_router, admin_auth_router
from routers.customers import customers_router
from routers.products import products_router

app=FastAPI()
app.include_router(admin_router)
app.include_router(customers_router)
app.include_router(auth_router)
app.include_router(admin_auth_router)
app.include_router(products_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)