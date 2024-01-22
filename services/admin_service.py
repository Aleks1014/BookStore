from mysql.connector import IntegrityError

from data.models import Author, Publisher, Category, Product, Admin
from data.database import insert_query


def create_admin(admin: Admin):
    generated_id = insert_query(
        'INSERT INTO admin(username, password, email) VALUES(%s,%s,%s)',
        query_params=(admin.username,  admin.password, admin.email)
    )
    return generated_id

def add_author(author: Author):
    generated_id = insert_query(
        'INSERT INTO author(first_name,last_name,image,social_media) VALUES(%s,%s,%s,%s)',
        query_params=(author.first_name, author.last_name, author.image, author.social_media)
    )
    return generated_id

def add_publisher(publisher: Publisher):
    generated_id = insert_query(
        'INSERT INTO publisher(name,social_media) VALUES(%s,%)',
        query_params=(publisher.name, publisher.social_media)
    )
    return generated_id

def add_category(category: Category):
    generated_id = insert_query(
        'INSERT INTO product_category(name,description) VALUES(%s,%s)',
        query_params=(category.name, category.description)
    )
    return generated_id

def add_book(book: Product):
    generated_id = insert_query(
        'INSERT INTO product(title,description,isbn,price,cover,publication_date,publisher_id,author_id'
        'VALUES(%s,%s,%s,%s,%s,%s,%s,%s',
        query_params=(book.title, book.description,book.isbn,book.price,book.cover,book.publication_date,
                          book.publisher_id,book.author_id)
    )
    return generated_id