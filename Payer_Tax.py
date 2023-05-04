class Payer():
    def __init__ (self,code,name,income,deduction):
        self.code=code
        self.name=name
        self.income=income
        self.deduction=deduction
        if income - deduction <= 5000:
            self.tax = (income - deduction) * 0.05
        elif income - deduction <= 10000:
            self.tax = (income - deduction) * 0.1
        else: 
            self.tax = (income - deduction) * 0.15
    
    def __repr__(self):
        return ("| {} | {} | {} | {} | {} |".format(self.code.center(8), self.name.center(20), str(self.income).center(10), str(self.deduction).center(12),str(self.tax).center(10)))