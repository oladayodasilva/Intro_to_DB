# MySQLServer.py
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    cursor = connection.cursor()

    # Create the database (must match ALX checker pattern)
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
