from datetime import date
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
import re


class Category(BaseModel):
    id: Optional[id] = None
    name: str
    description: Optional[str] = None


class Publisher(BaseModel):
    id: Optional[id] = None
    name: str
    social_media: Optional[str] = None


class Author(BaseModel):
    id: Optional[id] = None
    first_name: str
    last_name: str
    image: Optional[str] = None
    social_media: str | None


class Product(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    isbn: str
    price: float
    author_id: int
    subcategory_id: int
    publication_date: date
    cover: Optional[str] = None
    publisher_id: int
    format: str = Field(pattern=r'^(paperback|hardcover|ebook)$')
    pages: int


class ProductResponse(BaseModel):
    title: str
    description: str
    isbn: str
    price: float
    author_name: str
    subcategory: str
    category: str
    publication_date: date
    cover: Optional[str] = None
    publisher: str
    format: str = Field(pattern=r'^(paperback|hardcover|ebook)$')
    pages: int


class Review(BaseModel):
    id: int | None
    review: str | None
    stars: int = Field(ge=1, le=5)
    product_id: int
    customer_id: int

class Inventory(BaseModel):
    quantity: int
    product_id: int

class Admin(BaseModel):
    username: str
    password: str
    email: EmailStr

    @field_validator('password')
    @classmethod
    def validate_password(cls, password: str):
        pattern = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
        if re.match(pattern, password):
            return password
        else:
            raise ValueError('Password not strong enough')

    @classmethod
    def from_query_result(cls, id, username, password, email):
        return cls(
            id=id,
            username=username,
            password=password,
            email=email,
        )


class Customer(BaseModel):
    email: EmailStr
    password: str
    first_name: str = Field(pattern=r'^[a-zA-Z]{2,30}$')
    last_name: str = Field(pattern=r'^[a-zA-Z]{2,30}$')

    @field_validator('password')
    @classmethod
    def validate_password(cls, password: str):
        pattern = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
        if re.match(pattern, password):
            return password
        else:
            raise ValueError('Password not strong enough')

    @classmethod
    def from_query_result(cls, id, first_name, last_name, email, password):
        return cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )


class CustomerResponse(BaseModel):
    first_name: str
    last_name: str
    email: str


class CustomerLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None