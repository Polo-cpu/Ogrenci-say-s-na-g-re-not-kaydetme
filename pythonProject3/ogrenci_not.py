import time

with open("C:/Users/atill/Desktop/bilgilerim.txt", "a", encoding="utf-8") as file:
    ogrenci_sayisi = int(input("Lütfen Ögrenci Sayısını Giriniz: " ))
    ogrenci_ortalama = 0
    x = "geçer"
    y = "kalır"
    gecenler = []
    kalanlar = []
    while ogrenci_sayisi-1 >= 0:
        ogrenci_adi = input("lutfen ogrenci adini giriniz: ")
        ogrenci_not1 = int(input("Lütfen öğrencinin birinici notunu giriniz: "))
        ogrenci_not2 = int(input("lütfen öğrencinin ikinci notunu giriniz: "))
        file.write("Öğrenci adı : {}\n".format(ogrenci_adi))
        file.write("Ögrencinin ilk notu : {}\n".format(ogrenci_not1))
        file.write("Öğrencinin ikinci notu : {}\n".format(ogrenci_not2))
        print("----------------------------------")
        ogrenci_ortalama = ((ogrenci_not1 + ogrenci_not2) / 2)
        ogrenci_sayisi = ogrenci_sayisi - 1
        if ogrenci_ortalama >= 50:
            file.write("Öğrenci {} notu ile geçti\n".format(ogrenci_ortalama))
            file.write("-----------------------\n")

        else:
            file.write("Öğrenci {} notu ile kaldı\n".format(ogrenci_ortalama))
            file.write("-----------------------\n")
print("Bilgileriniz kaydediliyor....")
time.sleep(2)
