# This class is intended to collect, the username and information from an employee who will manage the
# # bookstore inventory. Written by Olivia Bertinelli on 9/19/24

class User:
    def __init__(self, id_user, userID, name, password):  # Initialize the user info class
        self.id_user = id_user
        self.userID = userID
        self.name = name
        self.password = password

    def retrieveUser(self):  # Retrieves the user details after being input and displays them (except password)
        return {
            'id_user': self.id_user,
            'userID': self.userID,
            'name': self.name,
        }

    def addUser(self):  # Used to add the current user to the database. This is not functioning within a database yet
        print(f"User {self.userID} added to the database.")
        return True

    def deleteUser(self):  # This is not actually functioning, just prints that it has been deleted
        print(f"User {self.userID} deleted from the database.")
        return True


id_user = int(input("Enter ID: "))
name = input("Enter your name: ")
userID = input("Enter your username: ")
password = input("Enter your password: ")
user = User(id_user, userID, name, password)

while True:
    print("\nOptions:")
    print("1. Display user info")
    print("2. Add current user")
    print("3. Delete current user")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":  # Prints user details minus the password
        user_details = user.retrieveUser()
        print("User Details:")
        for key, value in user_details.items():
            print(f"{key}: {value}")
    elif choice == "2":  # "Adds" user to database. not functioning yet
        user.addUser()
    elif choice == "3":  # "Removes" user from database. Not functioning yet
        user.deleteUser()
    elif choice == "4":  # Ends program
        print("Exiting program.")
        break
    else:  # Input validation
        print("Invalid choice. Please select a valid option.")
