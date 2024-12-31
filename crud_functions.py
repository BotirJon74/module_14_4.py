import sqlite3

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
            )
        ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

def add_product(title,description,price):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products(title, description, price) VALUES( ?, ?, ?)', (title,description,price))
    connection.commit()
    connection.close()
if __name__ == '__main__':
    initiate_db()
    add_product('Product1', 'Напиток 1', 100)
    add_product('Product2', 'Напиток 2', 200)
    add_product('Product3', 'Напиток 3', 300)
    add_product('Product4', 'Напиток 4', 400)