class Restuarant:
    def __init__(self,name,address,rent):
        self.name=name
        self.address=address
        self.rent=rent
        self.balance=0
        self.expence=0
        self.revenue=0
        self.chefs=[]
        self.managers=[]
        self.servers=[]
        self.expence_description={}

    def add_employee(self,employee,designation):
        if designation=='chef':
            self.chefs.append(employee)
        elif designation=='server':
            self.servers.append(employee)
        elif designation=='manager':
            self.managers.append(employee)


    def pay_expence(self,amount,description):
        if self.balance<amount:
            print("Not Enough Money In balance")
        else:
            self.balance-=amount
            self.expence+=amount
            self.expence_description[description]=amount

    def pay_salary(self,employee):
        if self.balance<employee.salary:
            print("Not Enough Money For Pay Slary")
        else:
            self.balance-=employee.salary
            self.expence+=employee.salary
            employee.salary_due=0

    def pay_bill(self,customer,order):
        if customer.wallet>=order.order_bill:
            customer.wallet-=order.order_bill
            customer.due=0
            self.balance+=order.order_bill
            self.revenue+=order.order_bill
        else:
            print("Not enough Money in {customer.name}'s Wallet")

    def show_employee(self):
        print('Manager:')
        for manager in self.managers:
            print(f"Name: {manager.name}, Salary: {manager.salary}")

        print('Chefs:')
        for chef in self.chefs:
            print(f"Name: {chef.name}, Salary: {chef.salary}")

        print('Servers:')
        for server in self.servers:
            print(f"Name: {server.name}, Salary: {server.salary}")



    
