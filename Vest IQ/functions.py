class User:
    def __init__(self, name, age, income, savings, dept, goal):
        self.name = ""
        self.age = 0
        self.income = 0.0
        self.savings = 0.0
        self.debt  = 0.0
        self.goal = ""
        
    def user_info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.income = float(input("Enter your income after taxes:R "))
        self.savings = float(input("Enter your savings:R "))
        self.debt = float(input("Enter your debt: "))
        self.goal = input("Enter your goal: ")
        all_info = [self.name, self.age, self.income, self.savings, self.debt, self.goal]
        return all_info

    def expenses(self):
        self.rent = float(input("Enter your rent expenses: R "))
        self.groceries = float(input("Enter your groceries expenses: R "))
        self.transport = float(input("Enter your transport expenses: R "))
        self.utilities = float(input("Enter your utilities expenses: R "))
        self.insurance = float(input("Enter your insurance expenses: R "))
        self.entertainment = float(input("Enter your entertainment expenses:R "))
        self.all_expenses = [self.rent, self.groceries, self.transport, self.utilities, self.insurance, self.entertainment]
        return self.all_expenses

    def risk_assessment():
        risk_lvl = input("Enter your risk level (low, medium, high)(low is recommended):  ")
        if risk_lvl not in ['low', 'medium', 'high']:
            print("Invalid input. Please enter 'low', 'medium', or 'high'.")
            return risk_lvl

# how much the user is willing to invest 
    def invesst_will(self):
        willing_invest = input("Enter at what level you are willing to invest (low, medium, high): ")
        if willing_invest not in ['low', 'medium', 'high']:
            print("Invalid input. Please enter 'low', 'medium', or 'high'.")
            return willing_invest
        elif willing_invest == 'low':
            based_invest = self.income * 0.1
        elif willing_invest == 'medium':
            based_invest = self.income * 0.2
        elif willing_invest == 'high':
            based_invest = self.income * 0.35
        return based_invest
        #return invesst_will()

# for emergency funds at least 3-6 months of expenses
    def emergency_fund(self):
        emg_fund = self.all_expenses * 6
        return emg_fund