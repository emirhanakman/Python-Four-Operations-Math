#!C:\Python33\python.exe
 
print("1-Toplama")
print("2-��karma")
print("3-B�lme")
print("4-�arpma")
print("5- Kare Al")
print("6- K�k Al")
print("q- ��k��")
 
while True:
    scanner = input("L�tfen yapmak istedi�iniz i�lemin numaras�n� se�iniz ")    
 
    if scanner == "q":
        print("��k��")
        break
 
    elif scanner == "1":
        scannerToplama1 = input("Toplamak istedi�iniz 1. say�y� giriniz: ")
        scannerToplama2 = input("Toplamak istedi�iniz 2. say�y� giriniz: ")
        sonuc = int(scannerToplama1) + int(scannerToplama2)
        print(sonuc)
 
    elif scanner == "2":
        scannerCikarma1 = input("��karma yapmak istedi�iniz say�y� giriniz: ")
        scannerCikarma2 = input("��kar�lacak say�y� giriniz: ")
        sonuc = int(scannerCikarma1)- int(scannerCikarma2)
        print(sonuc)
 
    elif scanner == "3":
        scannerBolme1 = input("B�l�necek say�y� giriniz: ")
        scannerBolme2 = input("B�lmek istedi�iniz say�y� giriniz: ")
        sonuc = int(scannerBolme1) / int(scannerBolme2)
        print(sonuc)
 
    elif scanner == "4":
        scannerCarpma1 = input("�arpmak istedi�iniz 1. say�y� giriniz: ")
        scannerCarpma2 = input("�arpmak istedi�iniz 2. say�y� giriniz: ")
        sonuc = int(scannerCarpma1) * int(scannerCarpma2)
        print(sonuc)
 
    elif scanner == "5":
        scannerKare = input("Karesin almak istedi�iniz say�y� giriniz: ")
        sonuc = int(scannerKare) ** 2
        print(sonuc)
 
    elif scanner == "6":
        scannerKok = input("Karek�k�n� almak istedi�iniz say�y� giriniz: ")
        sonuc = int(scannerKok) ** 0.5
        print(sonuc)
 
    else:
        print("Yanl�� bir rakam girdiniz l�tfen yeniden giriniz.")