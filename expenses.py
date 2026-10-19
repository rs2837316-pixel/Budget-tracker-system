class Expenses:

    def __init__(self,name,category,amount):
        self.name=name
        self.amount = amount
        self.categories = category

    def __repr__(self):
        return f"<Expenses:{self.name},{self.categories},{self.amount}>" 


