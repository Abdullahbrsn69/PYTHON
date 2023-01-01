# Bu projemizde LibraryDataManagementSystem.py dosyasında oluşturduğumuz sınıfı test edeceğiz.

import unittest
from LibraryDataManagementSystem import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library("Kütüphane", {}, {})
        self.library.addBook("Kitap1", "Yazar1")
        self.library.addBook("Kitap2", "Yazar2")
        self.library.addBook("Kitap3", "Yazar3")

    def test_addBook(self):
        self.library.addBook("Kitap4", "Yazar4")
        self.assertEqual(self.library.bookList, {"Kitap1": "Yazar1", "Kitap2": "Yazar2", "Kitap3": "Yazar3", "Kitap4": "Yazar4"})
        self.library.addBook("Kitap1", "Yazar1")
        self.assertEqual(self.library.bookList, {"Kitap1": "Yazar1", "Kitap2": "Yazar2", "Kitap3": "Yazar3", "Kitap4": "Yazar4"})
        self.library.addBook("Kitap5", "Yazar5")
        self.assertEqual(self.library.bookList, {"Kitap1": "Yazar1", "Kitap2": "Yazar2", "Kitap3": "Yazar3", "Kitap4": "Yazar4", "Kitap5": "Yazar5"})
        
        

    def test_deleteBook(self):
        self.library.deleteBook("Kitap1")
        self.assertEqual(self.library.bookList, {"Kitap2": "Yazar2", "Kitap3": "Yazar3"})
        self.library.deleteBook("Kitap2")
        self.assertEqual(self.library.bookList, {"Kitap3": "Yazar3"})   


    def test_lendBook(self):
        self.library.lendBook("Kitap1", "User1")
        self.assertEqual(self.library.LendBook, {"Kitap1": "User1"})
        self.library.lendBook("Kitap2", "User2")
        self.assertEqual(self.library.LendBook, {"Kitap1": "User1", "Kitap2": "User2"})
        self.library.lendBook("Kitap3", "User3")
        self.assertEqual(self.library.LendBook, {"Kitap1": "User1", "Kitap2": "User2", "Kitap3": "User3"})

    def test_returnBook(self):
        self.library.lendBook("Kitap1", "User1")
        self.library.lendBook("Kitap2", "User2")
        self.library.lendBook("Kitap3", "User3")
        self.library.returnBook("Kitap1")
        self.assertEqual(self.library.LendBook, {"Kitap2": "User2", "Kitap3": "User3"})
        self.assertEqual(self.library.bookList, {"Kitap1": "Yazar1", "Kitap2": "Yazar2", "Kitap3": "Yazar3"})
        self.library.returnBook("Kitap2")
        self.assertEqual(self.library.LendBook, {"Kitap3": "User3"})
        self.assertEqual(self.library.bookList, {"Kitap1": "Yazar1", "Kitap2": "Yazar2", "Kitap3": "Yazar3"})
        self.library.returnBook("Kitap3")
        self.assertEqual(self.library.LendBook, {})
        self.assertEqual(self.library.bookList, {"Kitap1": "Yazar1", "Kitap2": "Yazar2", "Kitap3": "Yazar3"})


if __name__ == "__main__":
    unittest.main()