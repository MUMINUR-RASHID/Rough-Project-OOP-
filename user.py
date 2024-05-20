class Users:
    def __init__(self,name,email):
        self.name=name
        self.email=email


class Customers(Users):
    def __init__(self, name, email,wallet,address):
        super().__init__(name, email)
        self.wallet=wallet
        self.address=address
        self.due=None

    
class Employees(Users):
    def __init__(self, name, email,salary,department,starting_date):
        super().__init__(name, email)
        self.salary=salary
        self.department=department
        self.starting_date=starting_date
        self.salary_due=salary


class Chefs(Employees):
    def __init__(self, name, email, salary, department,starting_date,cooking):
        super().__init__(name, email, salary, department,starting_date,)
        self.cooking=cooking


class Servers(Employees):
    def __init__(self, name, email, salary, department,starting_date,catagory):
        super().__init__(name, email, salary, department,starting_date)
        self.catagory=catagory


class Managers(Employees):
    def __init__(self, name, email, salary, department,starting_date):
        super().__init__(name, email, salary, department,starting_date)

