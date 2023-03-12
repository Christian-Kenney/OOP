from flask import Flask, url_for,render_template 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzahut.db'

db = SQLAlchemy(app)


class CustomersModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False, unique=True)

class OrdersModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer)
    cheese = db.Column(db.Integer)
    sauce = db.Column(db.Integer)
    toppings = db.Column(db.Integer)
    status = db.Column(db.String(200), nullable=False)
    cook = db.Column(db.Integer)
    driver = db.Column(db.Integer)

class EmployeesModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    clockedIn = db.Column(db.Integer, nullable=False)
    manager = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(200), nullable=False)




class CustomerActions():
    def __init__(self):
        customer = CustomersModel.query(CustomersModel).\
        filter(CustomersModel.name == self.name & CustomersModel.address == self.address)
        self.name = customer.name
        self.email = customer.email
        self.address = customer.address
        self.id = customer.id
        
    @app.route('/customer/add', methods=['GET', 'POST'])
    def createCustomer(self):
        
        print("enter name")
        self.name = input()
        print("enter email")
        self.email = input()
        print("enter address")
        self.address = input()
        customer = CustomersModel(name=self.name, email=self.email, address=self.address)
        db.session.add(customer)
        db.session.commit()
        

    def browseMenu(self):
        print("MENU OPTIONS")
        print("Cheese Option... 1: Mozzarella, 2: American, 3: None")
        print("Sauce Option.... 1: Regular, 2: Meat, 3:Spicy")
        print("Toppings Option... 1: Meat, 2: Pineapple, 3: None")    

    @app.route('/orders/add', methods=['GET', 'POST', 'PUT'])
    def placeOrder(self):
        print("enter your Cheese choice. 1, 2 or 3")
        self.cheese = input()
        print("enter your Sauce choice. 1, 2 or 3")
        self.sauce = input()
        print("enter your Toppings choice. 1, 2 or 3")
        self.toppings = input()
        self.status = "ordered"

        order = OrdersModel(customerId=self.id, cheese=self.cheese, sauce=self.sauce, toppings=self.toppings, status=self.status)
        db.session.add(order)
        db.session.commit()
    
    def viewOrders(self):
        
        our_orders = OrdersModel.query(OrdersModel).\
        filter(OrdersModel.customerId == self.id)
        print("HERE ARE YOUR PREVIOUS ORDERS")
        print(our_orders)

class ManagerActions():
    def __init__(self):
        print("enter name")
        self.name = input()
        print("print email")
        self.email = input()
        manager = EmployeesModel.query(EmployeesModel).\
        filter(EmployeesModel.name == self.name & EmployeesModel.email == self.email)
        self.clockedIn = manager.clockedIn

    def createEmployee(self):
        print("enter employee name")
        self.name = input()
        print("enter employee email")
        self.email = input()
        oldClockin = self.clockedIn
        self.clockedIn = 0
        print("enter employee role")
        self.role = input()
        self.clockedIn = oldClockin

        employee = EmployeesModel(name=self.name, email=self.email, clockedIn = self.clockedIn, manager = 0, role = self.role)
        db.session.add(employee)
        db.session.commit()
    def clockIn(self):
        if(self.clockIn == 1):
            print("you are no clocked out")
            self.clockIn = 0
        else:
            print("you are now clocked in")
            self.clockIn = 1
        db.session.commit()

    def refundOrder(self, orderId):
        order = OrdersModel.query(OrdersModel).\
        filter(OrdersModel.id == orderId)
        order.status = "refunded"
        db.session.commit()


    def viewSales(self):
        print("HERE ARE THE SALES")
        sales = OrdersModel.query(OrdersModel)
        print(sales)

    def checkSchedules(self):
        print("Here are the currently logged in employees")
        schedule = EmployeesModel.query(EmployeesModel).\
        filter(EmployeesModel.clockedIn == 1)
        print(schedule)

class CookActions():
    def __init__(self):
        print("enter name")
        self.name = input()
        print("print email")
        self.email = input()
        cook = EmployeesModel.query(EmployeesModel).\
        filter(EmployeesModel.name == self.name & EmployeesModel.email == self.email)
        self.clockedIn = cook.clockedIn

    def assignOrder(self):
        print("enter id of order to assign")
        selection = input()
        OrdersModel.query(OrdersModel).\
        filter(OrdersModel.id == selection)
        selection.status = "cooked"
        selection.cook = self.Id
        db.session.commit()

    def viewOrders(self):
        orders = OrdersModel.query(OrdersModel).\
        filter(OrdersModel.staus == "ordered")
        print(orders)
    
    def clockIn(self):
        if(self.clockIn == 1):
            print("you are no clocked out")
            self.clockIn = 0
        else:
            print("you are now clocked in")
            self.clockIn = 1
        db.session.commit()

class DriverActions():
    def __init__(self):
        print("enter name")
        self.name = input()
        print("print email")
        self.email = input()
        driver = EmployeesModel.query(EmployeesModel).\
        filter(EmployeesModel.name == self.name & EmployeesModel.email == self.email)
        self.clockedIn = driver.clockedIn

    def assignOrder(self):
        print("enter id of order to assign")
        selection = input()
        OrdersModel.query(OrdersModel).\
        filter(OrdersModel.id == selection)
        selection.status = "delivered"
        selection.cook = self.Id
        db.session.commit()
    
    def viewOrders(self):
        orders = OrdersModel.query(OrdersModel).\
        filter(OrdersModel.staus == "cooked")
        print(orders)
    
    def clockIn(self):
        if(self.clockIn == 1):
            print("you are no clocked out")
            self.clockIn = 0
        else:
            print("you are now clocked in")
            self.clockIn = 1
        db.session.commit()


with app.app_context():
    db.create_all()


def main():
    cust = CustomerActions()
    man = ManagerActions()
    cook = CookActions()
    drive = DriverActions()
    cust.createCustomer()
    cust.browseMenu()
    cust.placeOrder()
    man.clockIn()
    man.createEmployee()
    man.checkSchedules()
    man.viewSales()
    man.refundOrder(1)
    cook.clockIn()
    cook.viewOrders()
    cook.assignOrder()
    drive.clockIn()
    drive.viewOrders()
    drive.assignOrder()

    
    


if __name__ == "__main__":
    main()
    