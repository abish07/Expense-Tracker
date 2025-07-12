import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Cr7#united07",
    database="expense_tracker"
)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE expenses_table(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            date DATE,
            amount float,
            category varchar(50),
            description TEXT  
    )
"""
)
print("Table 'expenses' successfully created!!")
conn.commit()
cursor.close()
conn.close()