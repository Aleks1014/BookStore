from data.database import read_query
from data.models import Customer, Admin


def get_user(email):
    data = read_query('SELECT * FROM customer WHERE email=%s', query_params=(email,))
    return next((Customer.from_query_result(*row) for row in data), None)

# def get_password(email):
#     return read_query('SELECT password FROM customer WHERE email=%s', query_params=(email,))

#
def get_admin(username):
    data = read_query('SELECT * FROM admin WHERE username=%s', query_params=(username,))
    return next((Admin.from_query_result(*row) for row in data), None)