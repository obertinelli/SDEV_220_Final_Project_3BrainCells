class LowStock:
    def __init__(self, title, neededitems, alert):
        self.title = title
        self.neededitems = neededitems
        self.alert = alert
    
    def lowStock(self):
        return self.neededitems <= self.alert
            
    def alert_reader(self):
        if self.alert < 3:
         print("Alert: Low Stock")
        else: 
           print("The Stock is Good!")
# Example usage:
book = LowStock("Harry Potter", 20, 3)
print(f"The book '{book.title}' is low on stock: {book.lowStock()}")
print(f"Current stock of '{book.title}': {book.neededitems}")
book.alert_reader()