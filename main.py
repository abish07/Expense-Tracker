from addExpenses import addExpenses
from readExpenses import readExpenses
from report import monthlyReport

def main():
    while True:
        print("1. Add expenses")
        print("2. Veiw Expenses")
        print("3. Monthly Report")
        print("4. Exit")
        choice = input("Choose a number to perform Operation : ")

        match choice:
            case '1':
                addExpenses()
            case '2':
                readExpenses()
            case '3':
                monthlyReport()
            case '4':
                break
            case _:
                print("invalid input")
if __name__ == "__main__":
    main()
