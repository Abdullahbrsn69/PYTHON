# Bu proje kütüphane yönetim sistemini simüle eder.

import sys

class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Welcome to the {self.name} library. We have following books for you.")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def borrowBook(self, user, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("Lender-Book database has been updated. You can return the book now.")
        else:
            print("Book is not in the library.")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list.")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")

    while(True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Borrow a Book")
        print("4. Add a Book")
        print("5. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to borrow: ")
            user = input("Enter your name: ")
            harry.borrowBook(user, book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to add: ")
            harry.addBook(book)

        elif user_choice == 5:
            book = input("Enter the name of the book you want to return: ")
            harry.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                sys.exit()

            elif user_choice2 == "c":
                continue


# Path: Python Projects\__pycache__\Test.pyc