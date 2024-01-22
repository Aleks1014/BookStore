from data.database import read_query, insert_query, update_query
from data.models import ProductResponse


def get_book_by_id(id):
    data = read_query(
        '''SELECT title, p.description, isbn, price, concat(a.first_name, " ", a.last_name), sub.name, c.name,
        publication_date, cover, pub.name, p.format, pages
        FROM product as p
        JOIN author a ON a.id = p.author_id
        JOIN subcategory sub ON sub.id = p.subcategory_id
        JOIN category c ON c.id = sub.category_id
        JOIN publisher pub ON pub.id = p.publisher_id
        WHERE p.id =%s''', query_params=(id,))
    return (ProductResponse(title=title, description=description, isbn=isbn, price=price, author_name=author_name,
                            subcategory=subcategory, category=category, publication_date=publication_date,
                            cover=cover, publisher=publisher, format=format, pages=pages)
            for
            title, description, isbn, price, author_name, subcategory, category, publication_date, cover, publisher,
            format, pages
            in data)


