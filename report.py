import mysql.connector
from sqlconnector import Connector

def monthlyReport():
    conn = Connector()
    cursor = conn.cursor()
    month = int(input("Enter the month"))
    year = int(input("Enter the Year"))
    cursor.execute(
        "select * from expenses_table where month(date)=%s and year(date)=%s",(month,year)
    )
    rows = cursor.fetchall()
    total = 0
    for row in rows:
        total += row[2]
    print(f"The total amount spent in {month}-{year} is : {total}")