# import pymysql
# from pymysql import MySQLError

# try:

#     with pymysql.connect(host="localhost", user="root", password="1233") as connection:

#         print("Connected")

#         with connection.cursor() as cursor:
#             create_db = "CREATE DATABASE IF NOT EXISTS alx_book_store"

#             cursor.execute(create_db)
#             print("Database 'alx_book_store' created successfully!")

#             cursor.execute("USE alx_book_store")

#         # results = cursor.fetchall()
#         # for row in results:
#         #     print(row)
# except MySQLError as e:
#     print(f"Error {e}")

import mysql.connector
from mysql.connector import Error

try:

    connection = mysql.connector.connect(host="localhost", user="root", password="1233")

    print("Connected")

    cursor = connection.cursor()
    create_db = "CREATE DATABASE IF NOT EXISTS alx_book_store"

    cursor.execute(create_db)
    print("Database 'alx_book_store' created successfully!")

    cursor.execute("USE alx_book_store")


except Error as e:
    print(f"Error {e}")
