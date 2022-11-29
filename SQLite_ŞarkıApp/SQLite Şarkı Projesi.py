import sqlite3

import time


class Şarkı():
    def __init__(self, sarkıcı, sarkı_ismi, albüm, prodüksiyon_sirketi, şarkı_süresi):
        self.sarkıcı = sarkıcı
        self.sarkı_ismi = sarkı_ismi
        self.albüm = albüm
        self.prodüksiyon_sirketi = prodüksiyon_sirketi
        self.şarkı_süresi = şarkı_süresi

    def __str__(self):
        return "Şarkıcı: {}\nŞarkı ismi: {}\nAlbüm: {}\nProdüksiyon sirketi: {}\nŞarkı süresi: {}\n".format(
            self.sarkıcı, self.sarkı_ismi, self.albüm, self.prodüksiyon_sirketi, self.şarkı_süresi)


class Müzik():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("şarkılar.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists şarkılar (sarkıcı TEXT,sarkı_ismi TEXT,albüm TEXT,prodüksiyon_sirketi TEXT,şarkı_süresi INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def şarkıları_goster(self):
        sorgu = "Select * From şarkılar"  # şarkılar tablosundaki bütün şarkıları listeler
        self.cursor.execute(sorgu)  # Parantez içindeki SQL sorgusunu çalıştırır.
        şarkılar = self.cursor.fetchall()  # fetchall() fonksiyonu ile tüm satırları alırız.
        if (len(şarkılar) == 0):  # Eğer şarkılar tablosunda şarkı yoksa
            print("Şarkı bulunmuyor...")
        else:
            for i in şarkılar:
                şarkı = Şarkı(i[0], i[1], i[2], i[3], i[4])  # Şarkı sınıfından şarkı nesnesi oluşturuyoruz.
                print(şarkı)
        # Burda her adım bir mantıksal algoritmaya göre yazılmıştır. Önce bir sorgu makinesi oluşturuyoruz. Sonra şarkıcı parametresini makinenin içine atıyoruz. Makine bunu işliyor ve fetchall ile bize geri sunuyor. Sonra şarkılar tablosunda şarkı yoksa "Şarkı bulunmuyor..." yazdırıyoruz. Yoksa şarkılar tablosundaki bütün şarkıları listeliyoruz.

    def şarkı_sorgula(self, sarkıcı):
        sorgu = "Select * From şarkılar where sarkıcı = ?"  # sarkıcı parametresi ile sorgu yapar
        self.cursor.execute(sorgu, (sarkıcı,))  # sarkıcı parametresini sorguya ekler
        şarkılar = self.cursor.fetchall()  # sorgu sonucunda gelen şarkıları alır
        if len(şarkılar) == 0:
            print("Böyle bir şarkı bulunmuyor...")
        else:
            for şarkı in şarkılar:  # şarkılar listesindeki şarkıları tek tek dolaşır
                şarkı = Şarkı(şarkı[0], şarkı[1], şarkı[2], şarkı[3],
                              şarkı[4])  # Şarkı sınıfından şarkı nesnesi oluşturuyoruz.
                print(şarkı)

    def şarkı_ekle(self, şarkı):
        sorgu = "Insert into şarkılar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu, (
        şarkı.sarkıcı, şarkı.sarkı_ismi, şarkı.albüm, şarkı.prodüksiyon_sirketi, şarkı.şarkı_süresi))
        self.baglanti.commit()

    def şarkı_sil(self, sarkıcı):
        sorgu = "Delete From şarkılar where sarkıcı = ?"
        self.cursor.execute(sorgu, (sarkıcı,))
        self.baglanti.commit()

    def şarkı_güncelle(self, şarkı):
        sorgu = "Update şarkılar set sarkı_ismi = ? , albüm = ? , prodüksiyon_sirketi = ? where sarkıcı = ?"
        self.cursor.execute(sorgu, (şarkı.sarkı_ismi, şarkı.albüm, şarkı.prodüksiyon_sirketi, şarkı.sarkıcı))
        self.baglanti.commit()

    def toplam_şarkı_süresi(self, sarkıcı):
        sorgu = "Select şarkı_süresi From şarkılar where sarkıcı = ?"
        self.cursor.execute(sorgu, (sarkıcı,))
        şarkılar = self.cursor.fetchall()
        toplam_süre = 0  # toplam süreyi 0 dan başlatıyoruz
        for şarkı in şarkılar:
            toplam_süre += şarkı[0]  # şarkı[0] şarkı süresini verir.
        print("Şarkıcı {}'ın toplam şarkı süresi: {} dk".format(sarkıcı, toplam_süre))


müzik = Müzik()

while True:
    print("""
    1. Şarkıları Göster
    2. Şarkı Sorgula
    3. Şarkı Ekle
    4. Şarkı Sil
    5. Şarkı Güncelle
    6. Toplam Şarkı Süresi
    Çıkmak için 'q' ya basın.
    """)
    işlem = input("İşlemi seçiniz : ")

    if (işlem == "q"):
        print("Programdan çıkılıyor...")
        time.sleep(2)
        break
    elif (işlem == "1"):
        müzik.şarkıları_goster()
    elif (işlem == "2"):
        sarkıcı = input("Şarkıcı ismi : ")
        müzik.şarkı_sorgula(sarkıcı)
    elif (işlem == "3"):
        sarkıcı = input("Şarkıcı ismi : ")
        sarkı_ismi = input("Şarkı ismi : ")
        albüm = input("Albüm ismi : ")
        prodüksiyon_sirketi = input("Prodüksiyon şirketi : ")
        şarkı_süresi = int(input("Şarkı süresi : "))
        yeni_şarkı = Şarkı(sarkıcı, sarkı_ismi, albüm, prodüksiyon_sirketi, şarkı_süresi)
        müzik.şarkı_ekle(yeni_şarkı)
        print("Şarkı eklendi...")
    elif (işlem == 4):
        sarkıcı = input("Şarkıcı ismi : ")
        müzik.şarkı_sil(sarkıcı)
        print("Şarkı silindi...")
    elif (işlem == 5):
        sarkıcı = input("Şarkıcı ismi : ")
        sarkı_ismi = input("Şarkı ismi : ")
        albüm = input("Albüm ismi : ")
        prodüksiyon_sirketi = input("Prodüksiyon şirketi : ")
        şarkı_süresi = int(input("Şarkı süresi : "))
        yeni_şarkı = Şarkı(sarkıcı, sarkı_ismi, albüm, prodüksiyon_sirketi, şarkı_süresi)
        müzik.şarkı_güncelle(yeni_şarkı)
        print("Şarkı güncellendi...")

    elif (işlem == 6):
        sarkıcı = input("Şarkıcı ismi:")
        print("Şarkı süresi hesaplanıyor...")
        time.sleep(2)
        müzik.toplam_şarkı_süresi(sarkıcı)
    else:
        print("Geçersiz işlem...")
