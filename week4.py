class Customer:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def browse_menu(self):
        # Show menu to customer
    
    def place_order(self, order):
        pizza =  order.pizza
        drink = order.drink

    def view_previous_order(self, order_id):
        for x in order_id:
            print(x)

    def track_order(self, order_id)
        return order_id.status

    def cancel_order(self, order_id)
        order_id.status = cancel
    
class Driver:
    def __init__(self, name, phone_numer, email, employeeNum):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.employeeNum = employeeNum
    
    def view_orders(self, order_ids):
         for x in order_ids:
            if x.status = active:
                return x.id

class Manager:
    def __init__(self, name, phone_numer, email, employeeNum):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.employeeNum = employeeNum
    
    def see_employees(self):
        #return all employees

    def view_orders(self, order_ids):
         for x in order_ids:
            if x.status = active:
                return x.id
    
    def refund_order(self, order_id):
        #refund order
    
    def view_sales(self, order_ids):
        for x in order_ids:
            if x.status = complete:
                return x.id

    def check_schedule(self):
        #return schedule