# ----- EXPENSE TRACKER------
expenses = [] # list of all dic expenses
print("\n===== WELCOME TO EXPENSE TRACKER===" )

while True:
    print("---- MENU BAR----")
    print("1. Add expanse")
    print("2. View all expenses")
    print("3.view total expenditure")
    print("4. Exit")


    choice = int(input("Enter your choice"))

    if (choice == "1"):
        date = input("Enter a date")
        category= input("Enter a category")
        description = input("Enter detail of item")
        amount = float(input("Enter a amount"))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("\nExpense is added sucessfully")

        # view all expenses:
    elif (choice == 2):
        if len(expense == 0):
            print("No expense found")
        else:
            print("\n All Expenses List")

            for expense in expenses:
                print("date", expense["date"])
                print("category", expense["category"])
                print("description", expense["description"])
                print("amount", expense["amount"])

        # View total expenditure
    elif (choice == 3):
            total = 0
            for expense in expenses:
                total = total + expense(amount)
            print("\n All expenditure =" ,total)

        # For exit
    elif (choice == 4):
         print("Thank you")
    else:
         print("Invalid syntax")
         




