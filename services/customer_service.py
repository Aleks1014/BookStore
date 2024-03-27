from data.database import insert_query, read_query
from data.models import Customer
from services import product_service


def create_customer(customer: Customer):
    generated_id = insert_query(
        'INSERT INTO customer(first_name,last_name, email, password) VALUES(%s,%s,%s,%s)',
        query_params=(customer.first_name, customer.last_name, customer.email, customer.password)
    )
    return generated_id


def get_account_info(email):
    data = read_query('SELECT first_name, last_name,email FROM customer WHERE email=%s', query_params=(email,))
    return data


def get_account_id(email):
    data = read_query('SELECT id FROM customer WHERE email=%s', query_params=(email,))
    return data[0][0]

def get_wishlist(id):
    ids = read_query('SELECT product_id FROM wishlist WHERE customer_id=%s', query_params=(id,))
    result = []
    for id in ids:
        product = product_service.get_book_by_id(id[0])
        result.append(product)
    return result