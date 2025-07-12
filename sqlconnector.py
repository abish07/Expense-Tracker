import mysql.connector

def Connector():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cr7#united07",
    database="expense_tracker"
    )