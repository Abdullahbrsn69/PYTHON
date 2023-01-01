"""  
Projemiz, Kütüphane Bilgi yönetim sistemi olacak. 
Projemizde kitaplarin tutulduğu bir liste olacak. Gelen kullanicilar kitap seçip ödünç alabilecek. Bu kitabin ödünç süresi olacak. 
Kullanici kitabi iade ederse, kitap tekrar kütüphaneye eklenir. Ödünç alinan kitaplarin listesi tutulacak. 
Kitaplarin yazari da olacak. kitap ekleme, kitap silme, kitap ödünç alma, iade etme ve kitap sorgulama olarak 5 fonksiyon olacak.
"""

print("---------- Kütüphane Bilgi Yönetim Sistemi ----------")
print("-----------Kütüphanemize Hoşgeldiniz------------")

class Library:
    def __init__(self, name, bookList, LendBook) -> None:
        self.name = name
        self.bookList = {"İleri Python": "Abdullah", "İleri Java": "Ahmet", "Harry Potter": "J.K. Rowling", "İleri C++": "Mehmet", "L.O.T.R.": "J.R.R. Tolkien"}
        self.LendBook = {}

    def addBook(self,bookName, author):
        if bookName in self.bookList:
            print("Kitap zaten var")
        else:
            # burada zip fonksiyonunu kullanmayı tercih ediyorum.
            book_name = list(zip(self.bookList.keys(), self.bookList.values()))
            book_name.append((bookName, author))
            self.bookList = dict(book_name)
            print("Kitap eklendi")
   
    def deleteBook(self, bookName):
        if bookName in self.bookList:
            self.bookList.pop(bookName)
            print("Kitap silindi")
        else:
            print("Kitap bulunamadi")

    def lendBook(self, bookName, user):
        if bookName in self.bookList:
            self.LendBook.update({bookName: user})
            print("Kitap ödünç alindi")
        else:
            print("Kitap bulunamadi")

    
    def retrunBook(self, bookName):
        if bookName in self.LendBook:
            self.LendBook.pop(bookName)
            self.bookList.update({bookName: self.bookList[bookName]})
            print("Kitap iade edildi")
            print("Kitap tekrar kütüphaneye eklendi...")
        else:
            print("Kitap bulunamadi")


    def bookQuery(self, bookName):
        if bookName in self.bookList:
            print(f"Kitap adi: {bookName} Yazar: {self.bookList[bookName]}")
        else:
            print("Kitap bulunamadi")

    
    def showBooks(self):
        # burada items() fonksiyonunu kullanmayı tercih ediyorum.
        for book, author in self.bookList.items():
            print(f"Kitap adi: {book} Yazar: {author}")



if __name__ == "__main__":
    library = Library("Kütüphane", {}, {})

    while True:
        print("1. Kitap ekle")
        print("2. Kitap sil")
        print("3. Kitap ödünç al")
        print("4. Kitap iade et")
        print("5. Kitap sorgula")
        print("6. Kitapları göster")
        print("7. Çıkış")

        choice = int(input("Lütfen yapmak istediğiniz işlemi seçiniz: "))

        if choice == 1:
            bookName = input("Lütfen eklemek istediğiniz kitabin adini giriniz: ")
            author = input("Lütfen eklemek istediğiniz kitabin yazarini giriniz: ")

            library.addBook(bookName, author)

        elif choice == 2:
            bookName = input("Lütfen silmek istediğiniz kitabin adini giriniz: ")

            library.deleteBook(bookName)

        elif choice == 3:
            bookName = input("Lütfen ödünç almak istediğiniz kitabin adini giriniz: ")
            user = input("Lütfen ödünç almak istediğiniz kitabin kullanici adini giriniz: ")

            library.lendBook(bookName, user)

        elif choice == 4:
            bookName = input("Lütfen iade etmek istediğiniz kitabin adini giriniz: ")

            library.retrunBook(bookName)

        elif choice == 5:
            bookName = input("Lütfen sorgulamak istediğiniz kitabin adini giriniz: ")

            library.bookQuery(bookName)

        elif choice == 6:
            library.showBooks()

        elif choice == 7:
            print("Çikiş yapiliyor...")
            break

        else:
            print("Lütfen geçerli bir işlem giriniz")

        print("--------------------------------------------------")
        
