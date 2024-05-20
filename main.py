from user import Users,Customers,Employees,Chefs,Servers,Managers
from menu import Burger,Pizza,Drinks,Menu
from restaurant import Restuarant
from order import Order

def main():
    
    #resturant creation


    customer1=Customers("Abul","abul@gmail.com",20000,"Gulshan 1")
    customer2=Customers("abdul","abdul@gmail.com",30000,"Gulshan 2")
    customer3=Customers("kabul","kabul@gmail.com",20000,"Mirpor 1")

    restuarant=Restuarant("Vai-Vai","Sylhet",1500)

    chef1=Chefs("Rostom Baburchi",'rustombaburchi@gmail.com',1000,'Cooking',"jan 2,2022","Biriyani")
    chef2=Chefs("Joglo Baburchi",'joglobaburchi@gmail.com',800,'Cooking',"jan 2,2024","Vat-torkari")
    server1=Servers('jibon da','jibondacleaner@gmail.com',400,"Cleaning","jan 1,2024","Cleaner")
    server2=Servers('Kolim uddin','kolimthewater@gmail.com',600,"serving","jan 1,2024","waiter")
    manager=Managers("Akkas Ali","akkasali@gmail.com",1200,"Office","Jan 2,2022")

    restuarant.add_employee(chef1,"chef")
    restuarant.add_employee(chef2,"chef")
    restuarant.add_employee(server1,"server")
    restuarant.add_employee(server2,"server")
    restuarant.add_employee(manager,"manager")
    print("-----------------Employes------------------")
    restuarant.show_employee()


    print("------------------------MENU-----------------------")
    #menu creation
    menu=Menu()
    burger1=Burger("Chicken_Burger",600,"Fast_Food","Chicken","Large")
    menu.add_menu_item(burger1,"burger")
    burger2=Burger("Beaf_Burger",700,"Fast_Food","Beaf","Large")
    menu.add_menu_item(burger2,"burger")
    pizza1=Pizza("Chili_pizza",500,"Fast_Food","Large","mutton")
    menu.add_menu_item(pizza1,"pizza")
    pizza2=Pizza("Veg_pizza",600,"Fast_Food","Large","mexican")
    menu.add_menu_item(pizza2,"pizza")
    drink1=Drinks("Chocolate Coffee",120,"Drink",'250ml',"YES")
    menu.add_menu_item(drink1,"drinks")
    drink2=Drinks("CAPACHINU",180,"Drink",'250ml',"NO")
    menu.add_menu_item(drink2,"drinks")

    menu.show_menu()

    print(restuarant.revenue,restuarant.balance)
    order1=Order(customer1,[burger1,pizza1,drink1])
    restuarant.pay_bill(customer1,order1)
    print("after customer1",restuarant.revenue,restuarant.balance)
    order2=Order(customer2,[burger2,drink2,pizza2])
    restuarant.pay_bill(customer2,order2)
    print("after customer2",restuarant.revenue,restuarant.balance)
    order3=Order(customer3,[burger1,pizza2,drink2])
    restuarant.pay_bill(customer3,order3)
    print("after customer3",restuarant.revenue,restuarant.balance)

    restuarant.pay_salary(chef1)
    print("after pay salary",restuarant.revenue,restuarant.balance)
    restuarant.pay_expence(1500,"rent")
    print("after pay rent",restuarant.revenue,restuarant.balance)

    #print(customer1.name)

if __name__=="__main__":
    main()


