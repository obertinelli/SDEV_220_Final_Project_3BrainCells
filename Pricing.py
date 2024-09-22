class Pricing:
    def __init__(self, userID, ISBN, price):
        self.id_price = {}
        self.userID = userID
        self.ISBN = ISBN
        self.order = {}
        self.price = price
        
    def add_order(self, userID, ISBN, order):
        self.order[(userID, ISBN)] = order
        
    def update(self, userID, ISBN, order):
        if (userID, ISBN) in self.order:
            self.order[(userID, ISBN)] = order
        else:
            print("Book not found")
        
    def totalPrice(self, price, order):
        total = price * order['quantity']
        print(f"{order}: ${price}, Total: ${total}")

    def order_details(self):
        print(f"UserID: {self.userID}")
        print(f"ISBN: {self.ISBN}")
        print(f"Order: {self.order}")
        print(f"Total Price: {self.price}")
    #Example Run
pricing = Pricing(userID=1, ISBN="927503617", price=10.00)
pricing.add_order(userID=1, order={'quantity':1}, ISBN="927503617")
pricing.order_details()
order_details = {'quantity':2}
pricing.totalPrice(price=10.00, order=order_details)
pricing.update(userID=1, ISBN="927503617", order={'quantity': 2})


