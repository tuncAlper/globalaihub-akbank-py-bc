import csv
import datetime
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 10.99)

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 12.99)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza", 14.99)

class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 16.99)

class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__(pizza.get_description(), pizza.get_cost())
        self.pizza = pizza


class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Olives"
        self.cost = 2.99
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Mushrooms(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mushrooms"
        self.cost = 1.99
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Goat Cheese"
        self.cost = 3.49
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Meat"
        self.cost = 4.99
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Onions(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Onions"
        self.cost = 1.49
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Corn"
        self.cost = 0.99
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

     



      
with open("Menu.txt", "r",encoding="utf-8") as menu_file:
    menu = menu_file.read()
    print(menu)
    
    
    pizza_choice = input("Choose a pizza base (1-4): ")
    sauce_choice = input("Choose a sauce (11-16): ")
    
   
    if pizza_choice == "1":
        my_pizza = ClassicPizza()
    elif pizza_choice == "2":
        my_pizza = MargheritaPizza()
    elif pizza_choice == "3":
        my_pizza = TurkPizza()
    elif pizza_choice == "4":
        my_pizza = PlainPizza()
    else:
        print("Invalid pizza choice.")
        
    
    
    if sauce_choice == "11":
        my_pizza = Olives(my_pizza)
    elif sauce_choice == "12":
        my_pizza = Mushrooms(my_pizza)
    elif sauce_choice == "13":
        my_pizza = GoatCheese(my_pizza)
    elif sauce_choice == "14":
        my_pizza = Meat(my_pizza)
    elif sauce_choice == "15":
        my_pizza = Onions(my_pizza)
    elif sauce_choice == "16":
        my_pizza = Corn(my_pizza)
    else:
        print("Invalid sauce choice.") 
print(my_pizza.get_description())  
print(my_pizza.get_cost())

def calculate_payment(pizza):
    return pizza.get_cost()


user_name = input("Enter your name: ")
user_id = input("Enter your user ID: ")
credit_card_info = input("Enter your credit card information: ")
credit_card_password = input("Enter your credit card password: ")

payment = calculate_payment(my_pizza)


now = datetime.datetime.now()
time_order = now.strftime("%Y-%m-%d %H:%M:%S")


with open("Orders_Database.csv", mode="a",newline="\n") as file:
    writer = csv.writer(file)
    writer.writerow([f"name = {user_name}\n "f"id number = {user_id}\n "f"credit card number = {credit_card_info}\n "f"name of product = {my_pizza.get_description()}\n"f"time = {time_order}\n "f"credit card password = {credit_card_password}\n "f"payment = {payment}"])