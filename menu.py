class Food:
    def __init__(self,name,price,food_type):
        self.name=name
        self.price=price
        self.food_type=food_type


class Burger(Food):
    def __init__(self, name, price, food_type,mid_lyre,size) -> None:
        super().__init__(name, price, food_type)
        self.mid_lyre=mid_lyre
        self.size=size


class Pizza(Food):
    def __init__(self, name, price, food_type,size,catagory):
        super().__init__(name, price, food_type)
        self.size=size
        self.catagory=catagory


class Drinks(Food):
    def __init__(self, name, price, food_type,amount,isHot):
        super().__init__(name, price, food_type)
        self.amount=amount
        self.isHot=isHot


class Menu:
    def __init__(self):
        self.burgers=[]
        self.pizzas=[]
        self.drinks=[]


    def show_menu(self):
        print('Burgers:')
        for burger in self.burgers:
            print(f"name: {burger.name}, Price: {burger.price}, Size: {burger.size}, Lyre: {burger.mid_lyre}")

        print('Pizzas:')
        for pizza in self.pizzas:
            print(f"name: {pizza.name}, Price: {pizza.price}, Size: {pizza.size}, Catagory: {pizza.catagory}")

        print('Drinks:')
        for drink in self.drinks:
            print(f"name: {drink.name}, Price: {drink.price}, Size: {drink.amount}, Hot: {drink.isHot}")


    def add_menu_item(self,item,item_type):
        if item_type=='burger':
            self.burgers.append(item)
        elif item_type=="pizza":
            self.pizzas.append(item)
        elif item_type=='drinks':
            self.drinks.append(item)
        else:
            print("you entered wrong type. plz enter pizza,burger,drinks")
