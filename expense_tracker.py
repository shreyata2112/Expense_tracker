from datetime import datetime 
from expense import Expense
from colorama import Fore,Style,init
init(autoreset=True)
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self):
        print("/n Add a New Expense ")
        name = input("Name :  ")
        category = input("Category :  ")
        try:
         amount = float(input("Amount :  "))
        except ValueError:
         print(Fore.RED + "Invalid amount! Try again.")
         return
        date = input("Date(DD-MM-YYYY) or press Enter for today :  ")
        if date.strip()=="":
            date =datetime.today().strftime("%d-%m-%y")
        note = input("Note(optional) :  ")

        expense = Expense(name,category,amount,date,note)
        self.expenses.append(expense)
        print("Expense added.")
    def view_expenses(self):
        print("\n All Expenses :  ")
        if not self.expenses:
            print(Fore.RED + "No Expenses found.")
            return 
        for i, e in enumerate (self.expenses,1):
            print(f"{i}.  |{e.date}| {e.name} | {e.category} | {e.amount} | {e.note} |")
    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"\n Total Spent :  {total}")
    def run(self):
        while True:
            print(Fore.LIGHTGREEN_EX+"\n -----EXPENSE TRACKER MENU-----")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Show Total Money Spent")
            print("4. Exit")
            choice = input(Fore.BLUE +"Enter your option number(1-4) :  ")
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.total_spent()
            elif choice == '4':
                print("")
                print("Your session has ended. Thank you for using Expense Tracker!")
                print("")
                break
            else:
                print(Fore.RED+"Invalid Option! Try again.")

if __name__== "__main__":
    print("")
    print(Fore.LIGHTCYAN_EX+"|:| Welcome to Personal Expense Tracker |:|")
    print("")
    print("To proceed, please choose an option from the menu below.\n")
    tracker= ExpenseTracker()
    tracker.run()
