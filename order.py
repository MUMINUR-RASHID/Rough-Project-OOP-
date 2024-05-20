class Order:
    def __init__(self,customer,orders):
        self.order_bill=0
        for order in orders:
            self.order_bill+=order.price
        customer.due=self.order_bill