import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self,title,amount):
        self.id = str(uuid.uuid4()) #generate a unique identifier 
        self.title = title 
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
       
              
    def update(self, title=None, amount=None):
        #update title and/or amount if provided
        if title is not None:
            self.title = title 
        if amount is not None:
            self.amount = amount
            
        #update the updated_at timestamp
        self.updated_at = datetime.now(timezone.utc) 
        
    def to_dict(self):
        #convert instance variable to to adictionary
        return{
            "id" : self.id,
            "title" : self.title,
            "amount" : self.amount,
            "created_at" : self.created_at,
            "updated_at": self.updated_at
        }
        
        
        #creating a class expensedatabase
class Expensedatabase:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense):
        #adding an expense
        self.expenses.append(expense)
        
        def remove_expense(self, expense_id):
            #removing an expense
            self.expenses = [expense for expense in self.expenses if expense.id != id]
            
        
    def get_expense_by_id(self, expense_id):
        #getting an expense by id title
        for expense in self.expenses:
            if expense_id == id:
                return expense
        return None
    
    def get_expense_by_title(self, title):
        #getting an expense by title
        return[expense for expense in self.expenses if expense.title ==title]
    
    def to_dict(self):
        #creating a dict method that returns a list of dictionaries
        return[expense.to_dict()for expense in self.expenses]
        
                
                
       
       
        
        
        
        
        