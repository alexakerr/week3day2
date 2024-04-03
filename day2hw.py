# Homework
# Task One - done 
class BudgetCategory():
    def __init__(self, category_name, allocated_budget):
        self.category_name = category_name 
        self.__allocated_budget = allocated_budget 
        self.amount = 0

    def get_category_name(self): #getter
        return self._category_name
    
    def set_category_name(self, new_name): #setter
        # new_name = input("What category would you like to add to your budget?")
        self.__category_name = new_name
    
    
    def get_allocated_budget(self): #getter
        return self.__allocated_budget  
       
    
    def set_allocated_budget(self, new_budget): #setter
        self.__allocated_budget = new_budget
        if new_budget > 0:
            self._allocated_budget = new_budget
        else:
            print("Enter an amount greater than zero.")

    def add_expense(self, amount): 
        self.amount += amount

    def display_category_summary(self):
            print(f"Category Name: {self.category_name}")
            print("Allocated Budget: Hidden for security purposes. ")

# budget = BudgetCategory("entertainment", 15)
# budget.add_expense(10)
# print(budget.amount)




    


        





