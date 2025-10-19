# MySQLServer.py
import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    cursor = connection.cursor()
    # Create the database (note: no underscore in name)
    cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
    print("Database 'alxbookstore' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

