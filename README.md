# 💸 Expense Tracker

A simple CLI-based Python app to record and manage personal expenses using a MySQL database.

---

## 🔧 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:abish07/Expense-Tracker.git
   ```

2. **Set Up MySQL Database**:
   - Create a database named: `expense_tracker`
   - Run this SQL to create the table:
     ```sql
     CREATE TABLE expenses_table (
         id INTEGER PRIMARY KEY AUTO_INCREMENT,
         date DATE,
         amount FLOAT,
         category VARCHAR(50),
         description TEXT
     );
     ```

3. **Update MySQL Credentials**:
   In `sqlconnector.py`, change this part:
   ```python
   def Connector():
       return mysql.connector.connect(
           host="localhost",
           user="root",     
           password="YOUR_MYSQL_PASSWORD",   
           database="expense_tracker"
       )
   ```

4. **Install Required Package**:
   ```bash
   pip install mysql-connector-python
   ```

5. **Run the App**:
   ```bash
   python main.py
   ```

---

## 🗂️ Project Files

```
expense_tracker/
│
├── main.py               # Runs the program menu
├── addExpenses.py        # Adds new expenses
├── readExpenses.py       # Shows all stored expenses
├── report.py             # Monthly report generator
├── sqlconnector.py       # DB connection logic
└── create_table.py       # (Optional) To create the table in MySQL
```

---

## 📋 Features

- Add expenses with amount, category, and description
- View all expenses in the terminal
- Monthly report showing total expenses for a given month
- MySQL database stores everything

---

## 🛠 Requirements

- Python 3.x
- MySQL server
- `mysql-connector-python` package

---

## 🚀 How to Use

After setup, run this:

```bash
python main.py
```

Then pick:
- 1 to add expense
- 2 to view expenses
- 3 for monthly report
- 4 to exit

---

## 🙋‍♂️ Author

Created by **Abish Shrestha**
