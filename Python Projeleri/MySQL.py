# şimdi json dosyasını kullanarak bir bilgi yönetim sistemi oluşturacağız. Mysql kullanacağız.


import json
import mysql.connector

# json dosyasını okuyoruz
with open("C:\\Users\\user\\Desktop\\Python Projects\\MySQL.json", "r") as file:
    data = json.load(file)

# mysql bağlantısı
mydb = mysql.connector.connect( host = "localhost ", user = " root ", password = " 123456", database = " MySQL " )
mycursor = mydb.cursor()

# tablo oluşturma
mycursor.execute("CREATE TABLE IF NOT EXISTS deneme (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), age INT(3))")

# verileri tabloya ekleme
for i in data:
    name = i["name"]
    surname = i["surname"]
    age = i["age"]
    mycursor.execute("INSERT INTO deneme (name, surname, age) VALUES (%s, %s, %s)", (name, surname, age))
    mydb.commit()

# tablodaki verileri okuma
mycursor.execute("SELECT * FROM MySQL")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

# tablodaki verileri güncelleme 
mycursor.execute("UPDATE deneme SET name = 'Ahmet' WHERE id = 1")
mydb.commit()

# tablodaki verileri silme
mycursor.execute("DELETE FROM deneme WHERE id = 1")
mydb.commit()

# tabloyu silme
mycursor.execute("DROP TABLE MySQL")



