

class User:
    def __init__(self, name, roll, password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.returned_books = []


class Library:
    def __init__(self, book_list) -> None:
        self.book_list = book_list

    def borow_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print("Age ferot dew")
                    return
                if self.book_list[book] == 0:
                    print("Boi Sesh hoye gese")
                    return
                self.book_list[book] -= 1
                user.borrow_books.append(bookName)
                print("You have borrowed this books")
                return
        print("Book not Available")

    def return_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if book in user.borrow_books:
                    self.book_list[book] += 1
                    user.borrow_books.remove(bookName)
                    user.returned_books.append(bookName)
                    print("Book returned successfully")
                    return
                else:
                    print("Thanks but onner boi nibo na")
                    return

        print("Kar boi ferot dite ascho?")

    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book, self.book_list[book])

    def donate(self, bookName, amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print("Thanks for donating")
                return
        self.book_list[bookName] = amount


library = Library({"English": 2, "Bangla": 3, "Math": 5})
allUsers = []
currentUser = None

while True:
    if currentUser == None:
        print("Not logged in\nPlease login or create account(L/C)")
        option = input()
        if option == "L":
            roll = int(input("Roll: "))
            password = input("Password: ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("Not user found")
        else:
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("Password: ")
            found = False
            for user in allUsers:
                if user.roll == roll:
                    found = True
            if found:
                print("Bhai koibar account kulba?")
                continue
            user = User(name, roll, password)
            currentUser = user
            allUsers.append(user)
    else:
        print("OPTIONS")
        print("__________")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Borrowed books lis")
        print("4. Returned books list")
        print("5.Check available")
        print("6. Donating")
        print("7. LogOut")
        x = int(input("Give options: "))
        if x == 1:
            bookName = input("Book Name: ")
            library.borow_book(bookName, currentUser)
        elif x == 2:
            bookName = input("Book Name: ")
            library.return_book(bookName, currentUser)
        elif x == 3:
            print(currentUser.borrow_books)
        elif x == 4:
            print(currentUser.returned_books)
        elif x == 5:
            library.availability()
        elif x == 6:
            bookName = input("Book name: ")
            amount = int(input("Amount: "))
            library.donate(bookName, amount)
        elif x == 7:
            currentUser = None

        print("\n\n")
