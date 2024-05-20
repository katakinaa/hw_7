import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f"Error connecting to database: {error}")
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error creating table: {error}")


def insert_product(connection, product):
    try:
        sql = '''
            INSERT INTO products
            (product_title, price, quantity)
            VALUES 
            (?, ?, ?)
        '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error inserting product: {error}")


def update_product_quantity(connection, product_id, new_quantity):
    try:
        sql = '''
            UPDATE products
            SET quantity = ?
            WHERE id = ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (new_quantity, product_id))
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error updating product quantity: {error}")


def update_product_price(connection, product_id, new_price):
    try:
        sql = '''
            UPDATE products
            SET price = ?
            WHERE id = ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (new_price, product_id))
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error updating product price: {error}")


def delete_product(connection, product_id):
    try:
        sql = '''
            DELETE FROM products
            WHERE id = ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (product_id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error deleting product: {error}")


def select_products_under_limit(connection, price_limit, quantity_limit):
    try:
        sql = '''
            SELECT * FROM products
            WHERE price < ? AND quantity > ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f"Error selecting products under limit: {error}")


def search_products_by_title(connection, search_term):
    try:
        sql = '''
            SELECT * FROM products
            WHERE product_title LIKE ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + search_term + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f"Error searching products by title: {error}")


def select_all_products(connection):
    try:
        sql = '''
            SELECT * FROM products
        '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f"Error selecting all products: {error}")


sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection('hw.db')
if my_connection:
    print('Connected successfully to database!')
    # create_table(my_connection, sql_to_create_products_table)

    # insert_product(my_connection, ("Гель для душа", 129.99, 100))
    # insert_product(my_connection, ("Жидкое мыло с запахом ванили", 149.99, 50))
    # insert_product(my_connection, ("Шампунь восстанавливающий", 299.99, 200))
    # insert_product(my_connection, ("Маска для волос", 199.00, 30))
    # insert_product(my_connection, ("Крем для рук", 99.99, 150))
    # insert_product(my_connection, ("Средство для мытья посуды", 99.99, 20))
    # insert_product(my_connection, ("Мыло детское", 100.00, 300))
    # insert_product(my_connection, ("Мыло хозяйственное", 20.00, 80))
    # insert_product(my_connection, ("Кондиционер для белья", 140.00, 60))
    # insert_product(my_connection, ("Ночной крем для лица", 200.00, 100))
    # insert_product(my_connection, ("Зубная паста", 120.00, 40))
    # insert_product(my_connection, ("Шампунь для окрашенных волос", 350.00, 25))
    # insert_product(my_connection, ("Тканевая маска для лица", 18.00, 120))
    # insert_product(my_connection, ("Дневной крем для лица", 199.99, 170))
    # insert_product(my_connection, ("Кондиционер для волос", 400.00, 90))

    # update_product_quantity(my_connection, 11, 100)
    # update_product_price(my_connection, 4, 250)
    # delete_product(my_connection, 15)
    # select_products_under_limit(my_connection, 100, 50)
    # search_products_by_title(my_connection,'крем')
    # select_all_products(my_connection)

    my_connection.close()
else:
    print('Error')
