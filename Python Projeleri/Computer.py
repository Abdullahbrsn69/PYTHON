class Bilgisayar():

    def __init__(self, model, price, brand) -> None:
        self.model = model
        self.price = {"HP": 5000, "Lenovo": 6000, "Dell": 7000, "Asus": 8000, "Apple": 9000}
        self.brand = ["HP", "Lenovo", "Dell", "Asus", "Apple"]

    def __str__(self) -> str:
        return f"Model: {self.model}, Price: {self.price}, Brand: {self.brand}"

class Laptop(Bilgisayar):

    def __init__(self, model, price, brand) -> None:
        super().__init__(model, price, brand)
        self.screen_size = "13 inch"

    def __len__(self) -> int:
        return len(self.brand)

    def Pazarlık(self):
        return self.price[self.brand[0]] * 0.9
    
    def __str__(self) -> str:
        return super().__str__() + f", Screen Size: {self.screen_size}, Brands: {self.brand}"

    def seç(self):
        seçim = input("Laptop markasını seçiniz: ")

        if seçim in self.brand:
            print(f"{seçim} seçtiniz.")
        else:
            print("Böyle bir laptop markamız bulunmamaktadır.")

class Desktop(Bilgisayar):
    
        def __init__(self, model, price, brand) -> None:
            super().__init__(model, price, brand)
            self.cpu = "i3, i5, i7, i9"
    
        def __str__(self) -> str:
            return super().__str__() + f", CPU: {self.cpu}"


laptop = Laptop("Laptop", 5000, ["HP", "Lenovo", "Dell", "Asus", "Apple"])
desktop = Desktop("Desktop", 5000, ["HP", "Lenovo", "Dell", "Asus", "Apple"])

print(laptop)
print(desktop)

print(laptop.Pazarlık())
print(len(laptop))
laptop.seç()
    
