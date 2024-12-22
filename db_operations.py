import MySQLdb

def connect_to_db():
    connection = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="sourajabera@2002",
        db="grocery"
    )
    return connection


def add_product(name, price, stock):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, price, stock))
    conn.commit()
    conn.close()


def view_products():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    conn.close()
    return products


def update_stock(product_id, new_stock):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "UPDATE products SET stock = %s WHERE id = %s"
    cursor.execute(query, (new_stock, product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    conn.close()
