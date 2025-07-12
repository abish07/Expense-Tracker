import mysql.connector
from sqlconnector import Connector
def readExpenses():
    conn = Connector()
    cursor = conn.cursor()
    cursor.execute(
        "select * from expenses_table"
    )
    rows = cursor.fetchall()
    print("-------Details of the products-------")
    for row in rows:
        print()
        print(f"ID : {row[0]}, \ndate : {row[1]}, \nCategory : {row[2]}, \nDescription : {row[3]}")
        print()
        print("***********************************************************")
    print("Read all the data successfully")
    conn.close()
    cursor.close()

