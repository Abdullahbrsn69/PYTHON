# Bu projede bir mahkeme provası yapılacaktır. hukukta yapay zeka kullanımı ile ilgili bir çalışma yapılacaktır.



def bilgiAl():
    isim = input("İsminizi giriniz: ")
    soyisim = input("Soyisminizi giriniz: ")
    tc = input("T.C. Kimlik numaranizi giriniz: ")

    dosya = open("Dosya.txt", "w")  
    dosya.write(isim + " " + soyisim + " " + tc)
    dosya.close()

def bilgiOku():
    dosya = open("Dosya.txt", "r")
    bilgi = dosya.read()
    print(bilgi)
    dosya.close()

def kararAl():
    karar = input("Kazanma ihtimaliniz yüksek mi? (E/H) ")
    dosya = open("Dosya.txt", "a")
    dosya.write(" " + karar)
    dosya.close()

def kararOku():
    dosya = open("Dosya.txt", "r")
    karar = dosya.read()
    print(karar)
    dosya.close()

def main():
    bilgiAl()
    bilgiOku()
    kararAl()
    kararOku()

main()

    

