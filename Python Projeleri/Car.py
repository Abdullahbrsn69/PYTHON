

class Car:
    def __init__(self,model,price,brand) -> None:
        self.model = model
        self.price = price
        self.brand = brand

    def __str__(self) -> str:
        return f"Model: {self.model}, Price: {self.price}, Brand: {self.brand}"

class Mercedes(Car):
    def __init__(self,model,price,brand) -> None:
        super().__init__(model,price,brand)
        self.gear = "Otomatik"
        self.options = ["AMG", "C", "E", "GLA"]
        self.year = 2021

    def __str__(self) -> str:
        return super().__str__() + f", Vites: {self.gear}, Options: {self.options}, Year: {self.year}"

    def version_upgrade(self):
        self.options.append("S")

    def __del__(self,ch) -> None:
        self.options.remove(ch)

    def change_gear(self):
        self.gear = "Manuel"
    
    def bargain_price(self):
        self.price = self.price - (self.price * 0.10)

    def upgrade_model(self,year):
        self.model = year

class BMW(Car):
     
    def __init__(self,model,price,brand) -> None:
         super().__init__(model,price,brand)
         self.gear = "Otomatik"
         self.options = ["M", "X", "Z", "i"]
         self.year = 2021
         self.km = []

    def Km(self,kilometer):
        self.km.append(kilometer)
        print("Your car has been driven {} km.".format(kilometer))
    
    def fuel_consumption(self):
        if self.options == "M":
            print("Your car's fuel consumption is 10 lt.")
        elif self.options == "X":
            print("Your car's fuel consumption is 12 lt.")
        elif self.options == "Z":
            print("Your car's fuel consumption is 8 lt.")
        elif self.options == "i":
            print("Your car's fuel consumption is 6 lt.")

    def price_increase(self):
        self.price = self.price + (self.price * 0.12)

    def __del__(self,choice) -> None:
        self.options.remove(choice)


# şimdi bu uygulamayı çalıştıralım:

while True:
    print("Welcome to our car rental service.")
    print("1. Mercedes")
    print("2. BMW")
    print("3. Exit")
    choice = input("Please select a car brand: ")
    if choice == "1":
        print("1. AMG")
        print("2. C")
        print("3. E")
        print("4. GLA")
        print("5. S")
        print("6. Exit")
        choice = input("Please select a car model: ")
        if choice == "1":
            car = Mercedes("AMG", 5000, "Mercedes")
            print(car)
            print("1. Upgrade model")
            print("2. Bargain price")
            print("3. Change gear")
            print("4. Exit")
            choice = input("Please select an option: ")
            if choice == "1":
                year = input("Please enter the year: ")
                car.upgrade_model(year)
                print(car)
            elif choice == "2":
                car.bargain_price()
                print(car)
            elif choice == "3":
                car.change_gear()
                print(car)
            elif choice == "4":
                break
        elif choice == "2":
            car = Mercedes("C", 4000, "Mercedes")
            print(car)
            print("1. Upgrade model")
            print("2. Bargain price")
            print("3. Change gear")
            print("4. Exit")
            choice = input("Please select an option: ")
            if choice == "1":
                year = input("Please enter the year: ")
                car.upgrade_model(year)
                print(car)
            elif choice == "2":
                car.bargain_price()
                print(car)
            elif choice == "3":
                car.change_gear()
                print(car)
            elif choice == "4":
                break
        elif choice == "3":
            car = Mercedes("E", 3000, "Mercedes")
            print(car)
            print("1. Upgrade model")
            print("2. Bargain price")
            print("3. Change gear")
            print("4. Exit")
            choice = input("Please select an option: ")
            if choice == "1":
                year = input("Please enter the year: ")
                car.upgrade_model(year)
                print(car)
            elif choice == "2":
                car.bargain_price()
                print(car)
            elif choice == "3":
                car.change_gear()
                print(car)
            elif choice == "4":
                break