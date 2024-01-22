import mysql.connector


def close(curs, conn):
    curs.close()
    conn.close()


cnx = mysql.connector.connect(user='root', password='0505',
                              host='127.0.0.1',
                              database='bookstore')

cursor = cnx.cursor()



def read_query(query, query_params=()):
    cnx = mysql.connector.connect(user='root', password='0505',
                                  host='127.0.0.1',
                                  database='bookstore')

    cursor = cnx.cursor()
    cursor.execute(query,query_params)
    res = list(cursor)
    close(cursor, cnx)
    return res

def insert_query(query, query_params=(), cursor=cursor, cnx=cnx):
    try:
        cursor.execute(query, query_params)
        cnx.commit()
        close(cursor, cnx)
    except mysql.connector.Error as err:
        return f"Something went wrong: {err.msg}"
    return cursor.lastrowid

def update_query(query, query_params=(), cursor=cursor, cnx=cnx):
    try:
        cursor.execute(query, query_params)
        cnx.commit()
        close(cursor, cnx)
    except mysql.connector.Error as err:
        return f"Something went wrong: {err.msg}"
    return cursor.rowcount



# print(update_query('UPDATE product SET name = %s WHERE id=%s', query_params=('Carrie2', '2')))


# print(inser_query("INSERT INTO product(name,description,isbn,product_category_id,price) Values(%s,%s,%s,%s,%s)",
#                   query_params=('Misery', 'Test', '4444', '1', '1.5')))

# result = read_query('SELECT img FROM product WHERE id=%s', query_params=('9',))
#
# print(result[0][0])





