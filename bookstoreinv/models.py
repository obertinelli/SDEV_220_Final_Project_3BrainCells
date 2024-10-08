from django.db import models
from django.utils import timezone

# Create your models here.

# There is no way to update the details of a book in the Book model.
# This is because an ISBN is a unique identifier for a specific release of a book, 
# and thus the details of the book itself are constant.
# If information is incorrect, update the information via the admin panel.
class Book(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(max_length=50, default='General')
    quantity = models.IntegerField(default=0)
    should_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def shouldStock (self):
        return self.should_stock 
    
    def set_should_stock(self, should_stock):
        self.should_stock = should_stock
        self.save()
    
    def lowStock(self):
        return self.quantity == 0 and self.should_stock
    
    def order(self, quantity):
        self.quantity += quantity
        self.save()
        
# Notice that the Book instance does not self destruct when the quantity reaches 0. 
# This is to preserve the book's information in the sale and order history.
    def sell(self, quantity):
        if self.quantity < quantity:
            return False
        self.quantity -= quantity
        self.save()
        return True
        
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='order')
    quantity = models.IntegerField()
    date = models.DateField(default=timezone.now)
    filled = models.BooleanField(default=False)
    date_filled = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.book.title} - {self.quantity} - {self.date}"
    
    def fill(self):
        self.book.order(self.quantity)
        self.filled = True
        self.date_filled = timezone.now()
        self.save()
        
    def cancel(self):
        self.delete()
        
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sale')
    quantity = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    refunded = models.BooleanField(default=False)
    refunded_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.book.title} - {self.quantity} - {self.date}"
    
# This method should be called immediately after creating a Sale instance.
# We don't notify the user when a sale fails due to insufficient stock,
# because the ui should prevent the user from selling more than the stock.
# If the user somehow breaks or circumvents the ui, the sale will fail silently.
    def approve(self):
        if self.book.sell(self.quantity):
            self.date = timezone.now()
            self.save()
        else:
            self.delete()

# Notice that the Sale instance does not self destruct when refunded.
# This is to preserve the sale history, as well as to keep track of refunds.
    def refund(self):
        self.book.order(self.quantity)
        self.refunded = True
        self.refunded_date = timezone.now()
        self.save()
