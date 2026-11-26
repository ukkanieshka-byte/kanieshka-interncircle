import csv
import os
from datetime import date
FN="expenses.csv"
def setup_file():
    if not os.path.exists(FN):
        with open(FN,mode="w",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["Date","Category","Amount","Note"])
def add_expense():
    today=str(date.today())
    category=input("Enter category (e.g., Food,Travel,Bills):").strip().title()
    try:
        amount=float(input("Enter amount:"))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    note=input("Enter a short note (optional):").strip()
    with open(FN,mode="a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([today,category,amount,note])
    print("Expense saved!")
def view_expenses():
    print("\n---All Expenses---")
    with open(FN,mode="r",newline="") as file:
        reader=csv.reader(file)
        rows=list(reader)
        if len(rows)<=1:
            print("No expenses recorded yet.")
            return
        for row in rows[1:]:
            print(f"Date:{row[0]}|Category:{row[1]}|Amount:{row[2]}|Note:{row[3]}")
def filter_expenses():
    target=input("Enter category to filter by:").strip().title()
    print(f"\n---Expenses in '{target}'---")
    found=False
    with open(FN,mode="r",newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["Category"].title()==target:
                print(f"Date:{row['Date']}|Amount:{row['Amount']}|Note:{row['Note']}")
                found=True
    if not found:
        print("No expenses found for this category.")
def category_summary():
    totals={}
    with open(FN,mode="r",newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            category=row["Category"].title()
            amount=float(row["Amount"])
            totals[category]=totals.get(category,0)+amount
    print("\n---Category Summary---")
    if not totals:
        print("No data to summarize.")
        return
    for category,total in totals.items():
        print(f"{category}:{total:.2f}")
    print(f"Grand Total:{sum(totals.values()):.2f}")
def main():
    setup_file()
    while True:
        print("\n===Personal Expense Tracker===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")
        choice=input("Choose an option(1-5):").strip()
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            filter_expenses()
        elif choice=="4":
            category_summary()
        elif choice=="5":
            print("Goodbye!!")
            break
        else:
            print("Invalid choice.Please enter 1 to 5.")
if __name__=="__main__":
    main()
        
