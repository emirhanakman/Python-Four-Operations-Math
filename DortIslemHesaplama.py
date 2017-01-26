#!C:\Python33\python.exe
 
print("1-Toplama")
print("2-Çýkarma")
print("3-Bölme")
print("4-Çarpma")
print("5- Kare Al")
print("6- Kök Al")
print("q- Çýkýþ")
 
while True:
    scanner = input("Lütfen yapmak istediðiniz iþlemin numarasýný seçiniz ")    
 
    if scanner == "q":
        print("Çýkýþ")
        break
 
    elif scanner == "1":
        scannerToplama1 = input("Toplamak istediðiniz 1. sayýyý giriniz: ")
        scannerToplama2 = input("Toplamak istediðiniz 2. sayýyý giriniz: ")
        sonuc = int(scannerToplama1) + int(scannerToplama2)
        print(sonuc)
 
    elif scanner == "2":
        scannerCikarma1 = input("Çýkarma yapmak istediðiniz sayýyý giriniz: ")
        scannerCikarma2 = input("Çýkarýlacak sayýyý giriniz: ")
        sonuc = int(scannerCikarma1)- int(scannerCikarma2)
        print(sonuc)
 
    elif scanner == "3":
        scannerBolme1 = input("Bölünecek sayýyý giriniz: ")
        scannerBolme2 = input("Bölmek istediðiniz sayýyý giriniz: ")
        sonuc = int(scannerBolme1) / int(scannerBolme2)
        print(sonuc)
 
    elif scanner == "4":
        scannerCarpma1 = input("Çarpmak istediðiniz 1. sayýyý giriniz: ")
        scannerCarpma2 = input("Çarpmak istediðiniz 2. sayýyý giriniz: ")
        sonuc = int(scannerCarpma1) * int(scannerCarpma2)
        print(sonuc)
 
    elif scanner == "5":
        scannerKare = input("Karesin almak istediðiniz sayýyý giriniz: ")
        sonuc = int(scannerKare) ** 2
        print(sonuc)
 
    elif scanner == "6":
        scannerKok = input("Karekökünü almak istediðiniz sayýyý giriniz: ")
        sonuc = int(scannerKok) ** 0.5
        print(sonuc)
 
    else:
        print("Yanlýþ bir rakam girdiniz lütfen yeniden giriniz.")