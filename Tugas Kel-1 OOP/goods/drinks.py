class Drink:
    __jumlah = 0
    def __init__(self,inputName, inputPrice):
        self.__name = inputName
        self.__price = inputPrice
        self.__jumlah = 0
        self.__total = 0
        self.__level = 0
        Drink.__jumlah += 1

    @classmethod
    def totalDrinks(cls):
        return cls.__jumlah
    
    def getInfo(self):
        level = None
        if (self.__level == 1):
            level = "Biasa"
        elif (self.__level == 2):
            level = "Dingin"
        elif (self.__level == 3):
            level = "Hangat"
        elif (self.__level == 4):
            level = "Panas"
        else:
            print("Nilai yang anda Masukkan salah")
        self.__total = self.__jumlah * self.__price
        print("Nama Menu : {} {}\nHarga : {}\nJumlah : {}\nTotal Harga {}".format(self.__name,level,self.__price,self.__jumlah,self.__total))

    def changeLevel(self, value):
        self.__level = value

    def changeTotal(self, value):
        self.__jumlah = value

    @property
    def name(self):
        return self.__name

    @property
    def total(self):
        self.__total = self.__jumlah * self.__price
        return self.__total

    @property
    def price(self):
        return self.__price

    def orderInfo(self):
        if (self.__level == 1):
            self.__level = "Biasa"
        elif (self.__level == 2):
            self.__level = "Dingin"
        elif (self.__level == 3):
            self.__level = "Hangat"
        elif (self.__level == 4):
            self.__level = "Panas"
        else:
            print("Terdapat Error pada pilihan")
        self.__total = self.__jumlah * self.__price
        print("Pesanan :\n\tNama : {} {}\n\tHarga : {}\n\tSebanyak : {}\n\tTotal Harga : {}".format(self.__name,self.__level,self.__price,self.__jumlah,self.__total))