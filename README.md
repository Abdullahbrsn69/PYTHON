# PYTHON
Python
# KARGO ÜCRETİ HESAPLAMA. şirket kilo, boy ve ebatlara bakarak fiyat belirleyecek. En yüksek çıkan sonuç gerçek fiyat olacaktır!! Anlaşmalı müşteriye
# yarı yarıya indirim uygulanıyor....
# Ağırlık hesaplaması ----> (ağırlık x mesafe x 5 x 10^-3) + 10 olarak bulunur....
# Ebat hesaplaması  ----> en x boy x yükseklik x mesafe x 5 x 10^-6 + 9   olarak bulunur.
# Ebata göre fiyat ve ağırlığa göre fiyat karşılaştırılır ve hangisi fazlaysa ona göre fiyatlandırma yapılır. KAYNAKÇA: Python yapay zeka kitabı syf (138)

en = input("En yazınız (cm):")
boy = input("Boy yazınız (cm):")
yükseklik = input("yükseklik giriniz (cm):")
ağırlık = input("Ağırlık giriniz(kg) :")
mesafe = input("Mesafe giriniz (km) :")
anlaşmalı_mı = input("Anlaşmalı mısınız? (Evet: 1 , Hayır: 2) :")
en = float(en)
boy = float(boy)
yükseklik = float(yükseklik)
ağırlık = float(ağırlık)
mesafe = float(mesafe)
anlaşmalı_mı = float(anlaşmalı_mı)

ebata_göre_fiyat = (ağırlık * mesafe * 5 * (10 ** -3)) + 10
ağırlığa_göre_fiyat = (en * boy * yükseklik * mesafe * 10 ** -6) + 9

tutar = 0

if ebata_göre_fiyat > ağırlığa_göre_fiyat:
    tutar = ebata_göre_fiyat
else:
    tutar = ağırlığa_göre_fiyat
if anlaşmalı_mı == 1:
    tutar = tutar / 2
print(tutar)
