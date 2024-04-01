from goods.drinks import Drink
from goods.foods import Food
from customer import Customer
import time

class CafeShop:
    def __init__(self, inputName, inputAddress):
        self.__name = inputName
        self.__address = inputAddress
        self.__customer = []
        self.__menu_list = [[],[]]

    def addCustomer(self, value):
        self.__customer.append(value)

    def addFoods(self, value):
        self.__menu_list[0].append(value)

    def addDrinks(self, value):
        self.__menu_list[1].append(value)

    def dilevery():
        print('Proccess 20%')
        time.sleep(1)
        print('Proccess 40%')
        time.sleep(1)
        print('Proccess 60%')
        time.sleep(1)
        print('Proccess 80%')
        time.sleep(1)
        print('Proccess 100%')
    
    def drinksSystem(order, userValue):
        name = order.name
        print(f"Anda Memesan {name}")
        print('1. Biasa\n2. Dingin\n3. Hangat\n4. Panas')
        try:
            level = int(input('Pilih Level : '))
            print('___________________________________________________')
            order.changeLevel(level)
            try:
                jumlah = int(input("Berapa banyak yang anda pesan : "))
                print('___________________________________________________')
                if (jumlah >= 1):
                    order.changeTotal(jumlah)
                    if (userValue.cash() >= order.total):
                        CafeShop.dilevery()
                        buying_his = order.total
                        userValue.buying(buying_his)
                        order.orderInfo()
                        userValue.deliveryFoods(order)
                        print(f"Sisa uang anda : {userValue.cash()}")
                    else:
                        print("Uang anda tidak cukup")
                else:
                    print('Tidak dapat memesan kurang dari 0')
            except:
                print("Printah harus dalam bentuk angka")
                CafeShop.drinksSystem(order, userValue)
        except:
            print("Printah harus dalam bentuk angka")
            CafeShop.drinksSystem(order, userValue)


    def foodsSystem(order, userValue):
        name = order.name
        print(f"Anda Memesan {name}")
        print('1. Sedang\n2. Pedas')
        try:
            level = int(input('Pilih Level : '))
            print('___________________________________________________')
            order.changeLevel(level)
            try:
                jumlah = int(input("Berapa banyak yang anda pesan : "))
                print('___________________________________________________')
                order.changeTotal(jumlah)
                if (jumlah >= 1):
                    if (userValue.cash() >= order.total):
                        CafeShop.dilevery()
                        buying_his = order.total
                        userValue.buying(buying_his)
                        order.orderInfo()
                        userValue.deliveryFoods(order)
                        print(f"Sisa uang anda : {userValue.cash()}")
                    else:
                        print("Uang anda tidak cukup")
                else:
                    print('Tidak dapat memesan kurang dari 0')
            except:
                print("Printah harus dalam bentuk angka")
                CafeShop.foodsSystem(order, userValue)
        except:
            print("Printah harus dalam bentuk angka")
            CafeShop.foodsSystem(order, userValue)

    def system(self):
        nameInput = str(input("Masukkan Nama anda : "))
        user1 = Customer(nameInput)
        print('___________________________________________________')
        user1.sapa()
        opt = '0'
        while (opt != '99999'):
            print(f"Menu Warung {self.__name} di alamat {self.__address}")
            print("Pilih pilihan Mu :")
            print("1. Makanan")
            print("2. Minuman")
            print("3. Keluar")
            opt = str(input("Masukkan Pilihan Anda : "))
            if (opt == '1' or opt == "Makanan" or opt == "1. Makanan"):
                self.orderFoods(user1)
            elif (opt == '2' or opt == "Minuman" or opt == "2. Minuman"):
                self.orderDrinks(user1)
            elif (opt == '3' or opt == "Keluar" or opt == "3. Keluar"):
                print("Anda selesai memesan")
                break
            else:
                print('Pilihan yang anda masukkan salah')

    def orderFoods(self, userValue):
        nasi_goreng = Food("Nasi Goreng", 25000)
        seblak = Food("Seblak", 15000)
        mie_ayam = Food("Mie Ayam", 14000)
        bakso = Food("Bakso", 27000)
        ayam_geprek = Food("Ayam Geprek", 18000)
        self.__menu_list[0].append(nasi_goreng)
        self.__menu_list[0].append(seblak)
        self.__menu_list[0].append(mie_ayam)
        self.__menu_list[0].append(bakso)
        self.__menu_list[0].append(ayam_geprek)
        opt_1 = '0'
        while (opt_1 != '9999'):
            print("Daftar Makanan :")
            print(f"1. {self.__menu_list[0][0].name} : {self.__menu_list[0][0].price}")
            print(f"2. {self.__menu_list[0][1].name} : {self.__menu_list[0][1].price}")
            print(f"3. {self.__menu_list[0][2].name} : {self.__menu_list[0][2].price}")
            print(f"4. {self.__menu_list[0][3].name} : {self.__menu_list[0][3].price}")
            print(f"5. {self.__menu_list[0][4].name} : {self.__menu_list[0][4].price}")
            print("6. Kembali")
            order = str(input("Masukkan Pilihan mu :"))
            print('___________________________________________________')
            if (order == '1' or order == 'Nasi Goreng' or order == '1. Nasi Goreng'):
                order = self.__menu_list[0][0]
                CafeShop.foodsSystem(order, userValue)
            elif (order == '2' or order == 'Seblak' or order == '2. Seblak'):
                order = self.__menu_list[0][1]
                CafeShop.foodsSystem(order, userValue)
            elif (order == '3' or order == 'Mie Ayam' or order == '3. Mie Ayam'):
                order = self.__menu_list[0][2]
                CafeShop.foodsSystem(order, userValue)
            elif (order == '4' or order == 'Bakso' or order == '4. Bakso'):
                order = self.__menu_list[0][3]
                CafeShop.foodsSystem(order, userValue)
            elif (order == '5' or order == 'Ayam Geprek' or order == '5. Ayam Geprek'):
                order = self.__menu_list[0][4]
                CafeShop.foodsSystem(order, userValue)
            elif (order == '6'):
                break
            else:
                print("Opsi Yang anda masukkan Salah")
                self.orderFoods(userValue)

    def orderDrinks(self, userValue):
        teh_manis = Drink("Teh Manis", 5000)
        jus_alpukat = Drink("Jus Alpukat", 12000)
        es_jeruk = Drink("Es Jeruk", 6000)
        kopi = Drink("Kopi", 12000)
        air_mineral = Drink("Air Mineral", 4000)
        self.__menu_list[1].append(teh_manis)
        self.__menu_list[1].append(jus_alpukat)
        self.__menu_list[1].append(es_jeruk)
        self.__menu_list[1].append(kopi)
        self.__menu_list[1].append(air_mineral)
        opt_1 = '0'
        while (opt_1 != '9999'):
            print("Daftar Minuman :")
            print(f"1. {self.__menu_list[1][0].name} : {self.__menu_list[1][0].price}")
            print(f"2. {self.__menu_list[1][1].name} : {self.__menu_list[1][1].price}")
            print(f"3. {self.__menu_list[1][2].name} : {self.__menu_list[1][2].price}")
            print(f"4. {self.__menu_list[1][3].name} : {self.__menu_list[1][3].price}")
            print(f"5. {self.__menu_list[1][4].name} : {self.__menu_list[1][4].price}")
            print("6. Kembali")
            order = str(input("Masukkan Pilihan mu :"))
            print('___________________________________________________')
            if (order == '1' or order == 'Teh Manis' or order == '1. Teh Manis'):
                order = self.__menu_list[1][0]
                CafeShop.drinksSystem(order, userValue)
            if (order == '2' or order == 'Jus Alpukat' or order == '2. Jus Alpukat'):
                order = self.__menu_list[1][1]
                CafeShop.drinksSystem(order, userValue)
            if (order == '3' or order == 'Es Jeruk' or order == '3. Es Jeruk'):
                order = self.__menu_list[1][2]
                CafeShop.drinksSystem(order, userValue)
            if (order == '4' or order == 'Kopi' or order == '4. Kopi'):
                order = self.__menu_list[1][3]
                CafeShop.drinksSystem(order, userValue)
            if (order == '5' or order == 'Air Mineral' or order == '5. Air Mineral'):
                order = self.__menu_list[1][4]
                CafeShop.drinksSystem(order, userValue)
            elif (order == '6'):
                break
            else:
                print("Opsi Yang anda masukkan Salah")
                self.orderDrinks(userValue)
                
iqbal = CafeShop("Toko Iqbal", "Jalan Cumi-Cumi")
iqbal.system()