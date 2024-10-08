class UpdatingInventory:
    def __init__(self, title, author, genre, description, ISBN, edition):
        self._id_updating = None  
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.ISBN = ISBN
        self.edition = edition
        self.books = []

    def displayDetails(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, "
              f"Description: {self.description}, ISBN: {self.ISBN}, Edition: {self.edition}")

    def add(self, book):
        self.books.append(book)

    def delete(self, ISBN):
        self.books = [book for book in self.books if book['ISBN'] != ISBN]

    def updateStatus(self, ISBN, new_details):
        for book in self.books:
            if book['ISBN'] == ISBN:
                book.update(new_details)

inventory = UpdatingInventory("Sample Title", "Sample Author", "Fiction", "Sample Description", 1234567890, 1)
inventory.add({"title": "The Hunger Games", "author": "Suzanne Collins", "ISBN": 173917392, "edition": 1})
inventory.displayDetails()
inventory.updateStatus(173917392, {"edition": 2, "description": "Updated Description"})
inventory.delete(1234567890) 
