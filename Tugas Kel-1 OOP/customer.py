class Customer:
    def __init__(self, inputName, cash = 200000):
        self.__name = inputName
        self.__cash = cash
        self.__drinks = []
        self.__foods = []

    def sapa(self):
        print(f"Selamat Datang {self.__name} di toko Kami.\nUang anda : {self.__cash}")

    def getStatus(self):
        print(f"Nama Pelanggan : {self.__name}\nUang : {self.__cash}")

    def deliveryDrinks(self, value):
        self.__drinks.append(value)

    def deliveryFoods(self, value):
        self.__foods.append(value)

    def cash(self):
        return self.__cash
    
    def buying(self, value):
        self.__cash -= value