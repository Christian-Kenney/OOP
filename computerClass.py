class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def computer_arrive(self):
        print("Welcome to the store!")

    def computer_leave(self):
        print("Thank you for shopping with us!")

class Desktop(Computer):
    def __init__(self,  brand, model, year, screen, stock):
        super().__init__(brand, model)
        self.year = year
        self.screen = screen
        self.stock = stock

    def haveScreen(self):
        print("Desktop does not come with a screen")

    def checkStock(self):
        if self.stock > 0:
            print("Desktop is in stock")
        else:
            print("Desktop is out of stock")

class Laptop(Computer):
    def __init__(self,  brand, model, year, screen, stock):
        super().__init__(brand, model)
        self.year = year
        self.screen = screen
        self.stock = stock
    
    def haveScreen(self):
        print("Laptop comes with a screen built in")

    def checkStock(self):
        if self.stock > 0:
            print("Laptop is in stock")
        else:
            print("Laptop is out of stock")

class Tablet(Computer):
    def __init__(self,  brand, model, year, screen, stock):
        super().__init__(brand, model)
        self.year = year
        self.screen = screen
        self.stock = stock

    def haveScreen(self):
        print("Tablet comes with a screen built in")

    def checkStock(self):
        if self.stock > 0:
            print("Tablet is in stock")
        else:
            print("Tablet is out of stock")

def checkStock():
    desktop = Desktop("Dell", "Optiplex", 2021, 0, 0)
    laptop = Laptop("Apple", "Macbook", 2023, 1, 23)
    tablet = Tablet("Microsoft", "Surface", 2022, 1, 12)

    desktop.computer_arrive()
    desktop.haveScreen()
    desktop.checkStock()
    desktop.computer_leave()
    print()

    laptop.computer_arrive()
    laptop.haveScreen()
    laptop.checkStock()
    laptop.computer_leave()
    print()

    tablet.computer_arrive()
    tablet.haveScreen()
    tablet.checkStock()
    tablet.computer_leave()

checkStock()
