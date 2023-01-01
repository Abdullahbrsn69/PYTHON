# Bu projede Twitter ın basit bir backend uygulamasını yapacağız. Yani Twitter'ın demosunu, simülasyonunu yapacağız.
# ilk önce kullanıcıya ait bir twitter hesabı oluşturacağız. Bu hesapta kullanıcı adı, şifre, e-posta, telefon numarası bilgileri yer alacak.
# Tweetle diye bir fonksiyon tanımlayacağız. Bu fonksiyon kullanıcıdan mesaj alacak ve bu mesajı kaydedecek.
# Bu uygulamada Anasayfa yani ana fonksiyon olacak. Bu fonksiyon seçilince anasayfaya gidecek. En son.
# Keşfet fonksiyonu olacak. Bu fonksiyonda önceden eklediğimiz kullanıcılar ve bilgileri gösterilecek.
# Bildirimler olacak. Kullanıcıdan girilen mesajların bildirimleri olacak.
# Mesajlar fonksiyonu olacak. Bu fonkisyonda kullanıcı klavyeden mesaj yazacak ve bu mesaj kaydedilecek.
# Listeler fonkisyonu olacak. Buraya kullanıcı favori kişileri veya mesajları ekleyecek.
# Profil fonksiyonu olacak. Burada kullanıcı bilgilerini gösterecek.
""" Şimdi kodlamaya başlayalim. """

# ilk önce bilgileri kaydetmek için dosya işlemlerini yapıyoruz.

# ─── IMPORTS ────────────────────────────────────────────────────────────────────

import os
import time
import json
import random
from os.path import exists


# ─── CONSTANTS ────────────────────────────────────────────────────────────────

FILE_PATH = "Twitter.json"

# ─── DATABASE ────────────────────────────────────────────────────────────────

def get_data():

    if not exists(FILE_PATH): # dosya yoksa
        return {}
    f =open(FILE_PATH, "r")
    data = f.read()

    return json.loads(data) # json dosyasını oku. Buradaki loads fonksiyonu json dosyasını okuyor.

def set_data(data):
    f = open (FILE_PATH, "w")
    json_data = json.dumps(data) # Sözlük veri tipindeki değişkenlerimizi dumps() fonksiyonunu kullanarak JSON formatına çevirebiliriz. 
    f.write(json_data)

# ─── CREATE TWİTTER ACCOUNT ────────────────────────────────────────────────────────────────

def new_create_twitter_account(user_name, password, email, phone_number):
    data = get_data()
    data[user_name] = {
        "password": password,
        "email": email,
        "phone_number": phone_number,
        "tweets": [],
        "following": []
    }
    
    set_data(data)


# ─── TAKE A TWEET ────────────────────────────────────────────────────────────────────────────────

def tweetle(user_name,password, tweet):
    data = get_data()
    if user_name in data:
        if data[user_name]["password"] == password:
            data[user_name]["tweets"].append(tweet)
            set_data(data)
            print("Tweet başariyla gönderildi.")
        else:
            print("Şifre yanliş.")
    else:
        print("Kullanici adi bulunamadi.")



# ─── DİSCOVER PAGE ────────────────────────────────────────────────────────────────────────────────
"""Kullanicilar ve o kullanicilarin mesajlari gösterilecek"""

def discover_page():
    data = get_data()
    for user_name in data:
        print(f"{user_name} adli kullanici")
        for tweet in data[user_name]["tweets"]:
            print(f"Mesaj: {tweet}")
        

# ─── NOTİFİCATİON PAGE ────────────────────────────────────────────────────────────────────────────────
"""Kullanicidan girilen mesajlarin bildirimleri olacak. Kaydedilen tüm kullanicilarin mesajlari gösterilecek ve takip istekleri gösterilecek."""

def notification_page(user_name):
    data = get_data()
    for user_name in data:
        print(f"{user_name} adli kullanici")
        for tweet in data[user_name]["tweets"]:
            print(f"Mesaj: {tweet}")
        for following in data[user_name]["following"]:
            print(f"Takip istegi: {following}")


# ─── MESSAGES PAGE ────────────────────────────────────────────────────────────────────────────────
"""Kullanicidan mesaj alinacak ve kaydedilecek."""

def messages_page(user_name, password):
    data = get_data()
    if user_name in data:
        if data[user_name]["password"] == password:
            message = input("Mesaj giriniz: ")
            data[user_name]["tweets"].append(message)
            set_data(data)
            print("Mesaj kaydedildi.")
        else:
            print("Şifre yanliş.")
    else:
        print("Kullanici adi bulunamadi.")

# ─── LİST PAGE ────────────────────────────────────────────────────────────────────────────────
# data da var olan kullanıcıları ve o kullanıcıların mesajlarını listeye ekleyeceğiz.

def list_page(user_name):

    data = get_data()

    list = []

    for user_name in data:
        list.append(user_name)
        for tweet in data[user_name]["tweets"]:
            list.append(tweet)

print(list)

# ─── PROFILE PAGE ────────────────────────────────────────────────────────────────────────────────
""" Bu fonksiyonda kullanıcı bilgilerini göstereceğiz. Bu bilgiler isim, şifre, email, telefon numarası, mesajlar ve takip edilenler olacak. """

def profile_page(user_name, password):
    data = get_data()
    if user_name in data:
        if data[user_name]["password"] == password:
            print(f"Kullanici adi: {user_name}")
            print(f"Şifre: {password}")
            print(f"Email: {data[user_name]['email']}")
            print(f"Telefon numarasi: {data[user_name]['phone_number']}")
            print(f"Mesajlar: {data[user_name]['tweets']}")
            print(f"Takip edilenler: {data[user_name]['following']}")
        else:
            print("Şifre yanliş.")
    else:
        print("Kullanici adi bulunamadi.")

# ─── FOLLOW PAGE ────────────────────────────────────────────────────────────────────────────────
""" Bu fonksiyonda kullanıcı takip edebilecek. """

def follow_page(user_name, password, following):
    data = get_data()
    if user_name in data:
        if data[user_name]["password"] == password:
            data[user_name]["following"].append(following)
            set_data(data)
            print("Takip istegi gönderildi.")
        else:
            print("Şifre yanliş.")
    else:
        print("Kullanici adi bulunamadi.")


# ─── MAIN ────────────────────────────────────────────────────────────────────────────────

def main():
    while True:
        print("""
        1. Create Twitter Account
        2. Tweetle
        3. Discover Page
        4. Notification Page
        5. Messages Page
        6. List Page
        7. Profile Page
        8. Follow Page
        9. Çikiş
        """)
        secim = input("Lütfen bir secim yapiniz: ") 

        if secim == "1":
            user_name = input("Kullanici adi giriniz: ")
            password = input("Sifre giriniz: ")
            email = input("Email giriniz: ")
            phone_number = input("Telefon numarasi giriniz: ")
            new_create_twitter_account(user_name, password, email, phone_number)
        elif secim == "2":
            user_name = input("Kullanici adi giriniz: ")
            password = input("Sifre giriniz: ")
            tweet = input("Tweet giriniz: ")
            tweetle(user_name, password, tweet)
        elif secim == "3":
            discover_page()
        elif secim == "4":
            user_name = input("Kullanici adi giriniz: ")
            notification_page(user_name)
        elif secim == "5":
            user_name = input("Kullanici adi giriniz: ")
            password = input("Sifre giriniz: ")
            messages_page(user_name, password)
        elif secim == "6":
            user_name = input("Kullanici adi giriniz: ")
            list_page(user_name)
        elif secim == "7":
            user_name = input("Kullanici adi giriniz: ")
            password = input("Sifre giriniz: ")
            profile_page(user_name, password)
        elif secim == "8":
            user_name = input("Kullanici adi giriniz: ")
            password = input("Sifre giriniz: ")
            following = input("Takip edilecek kullanici adini giriniz: ")
            follow_page(user_name, password, following)
        elif secim == "9":
            break

main()
        

