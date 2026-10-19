from expenses import Expenses

def main():

    print("""
1. get_user_input
2. save_expenses
3. summarise_expenses
4. exist

""")
    while True:
        choosen = input("enter the choosen:")

        if choosen == '1':
            expenses = get_user_input()
        elif choosen == '2':
            file_name_path = "expenses.csv"
            save_expense(expenses,file_name_path)
        elif choosen == '3':    
            summarise_expenses(file_name_path)
        elif choosen == '4':
            exit()
        else:
            print("invalid choosen ! you have to only choose 1 to 4 ")
            


def get_user_input():
    expense_name = input("enter the expense name:")
    expense_amount = float(input("enter the expense amount:"))
    # creating a list of expenses
    expenses_categories = ['food','home','work','fun','music']

    while True:

        for i , expenses_name in enumerate(expenses_categories):
            print(f"{i+1}.{expenses_name}")

        value_range = f"[1-{len(expenses_categories)}]"  
        select_index = int(input(f"enter the category number {value_range}:")) -1

        if select_index in range(len(expenses_categories)):

            select_category = expenses_categories[select_index]

            new_expense = Expenses(name=expense_name,category=select_category,amount=expense_amount)
            print("taking input user sucessfully ")

            return new_expense
            
        else:
            print("invalid categories , please try again")



def save_expense(expenses:Expenses,file_name_path):

    print(f"saving user expenses {expenses} to {file_name_path}")

    with open(file_name_path,"a") as f:
        f.writelines(f"{expenses.name},{expenses.categories},{expenses.amount}\n")


def summarise_expenses(file_name_path):

    with open(file_name_path,"r") as f:
        data= f.read()
        print(data)



if __name__ == '__main__':
    main()



    