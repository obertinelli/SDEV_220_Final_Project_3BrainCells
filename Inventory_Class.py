class Inventory: 
    def __init__(self, title, author, ISBN, price, storeInventory):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price
        self.books = []
        self.storeInventory = storeInventory
    
    def __str__(self):
      return f"{self.title} by {self.author}, ISBN: {self.ISBN}, Price: ${self.price}"

    def storeInventoryBooks(self):
        self.books = [
            {"ISBN": 173917392, "title": "The Hunger Games", "author": "Suzanne Collins", "price": 10.00},
            {"ISBN": 278865478, "title": "Harry Potter and the Order of the Phoenix", "author": "J.K. Rowling", "price": 10.00},
            {"ISBN": 335784325, "title": "Pride and Prejudice", "author": "Jane Austen", "price": 10.00},
            {"ISBN": 473927348, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 10.00},
            {"ISBN": 584647382, "title": "The Book Thief", "author": "Markus Zusak", "price": 10.00},
            {"ISBN": 643859392, "title": "Twilight", "author": "Stephenie Meyer", "price": 10.00},
            {"ISBN": 784847382, "title": "Animal Farm", "author": "George Orwell", "price": 10.00},
            {"ISBN": 838495478, "title": "The Fault in Our Stars", "author": "John Green", "price": 10.00},
            {"ISBN": 938474633, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "price": 10.00},
            {"ISBN": 102874847, "title": "Wuthering Heights", "author": "Emily Bronte", "price": 10.00}
        ]

    def searchBook(self, query):
       result = []
       query = query
       for book in self.books:
         if query in book["title"]:
            result.append(book)
            return result
    def search_author(self, query):
        result = []
        query = query
        for book in self.books:
            if query in book["Author"]:
                result.append(book)
                return result
    def review_details(self):
        self.storeInventoryBooks()
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}")

        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        ISBN = input("Enter the ISBN: ")
        price = float(input("Enter the price: "))
        storeInventory = int(input("Enter the store inventory count: "))
        self.books.append({
            'title': title,
            'author': author,
            'ISBN': ISBN,
            'price': price,
            'storeInventory': storeInventory
        })

    def create_printing_outputs(self):
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Price: ${book['price']}, Store Inventory: {book['storeInventory']}")

inventory = Inventory('title', 'author', 'ISBN', 'price', 'storeInventory')
inventory.review_details()
inventory.create_printing_outputs()