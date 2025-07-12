import mysql.connector
from sqlconnector import Connector

def addExpenses():
    conn = Connector()
    cursor = conn.cursor()
    amount = float(input("Enter the amount : "))
    category = input("Enter the category : ")
    description = input("Describe the detail of the product : ")

    cursor.execute(
        "INSERT INTO expenses_table(date,amount,category,description) VALUES (CURDATE(),%s,%s,%s)",
        (amount,category,description)
    )  
    conn.commit()
    cursor.close()
    conn.close()