import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store"
        )
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

def connect_to_mysql():
    try:
        cnx = mysql.connector.connect(
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        cursor = cnx.cursor()
        return cnx, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            print(err)
        return None, None

def close_connection(cnx, cursor):
    cursor.close()
    cnx.close()

def main():
    cnx, cursor = connect_to_mysql()
    if cnx is not None and cursor is not None:
        create_database(cursor)
        close_connection(cnx, cursor)

if __name__ == "__main__":
    main()
