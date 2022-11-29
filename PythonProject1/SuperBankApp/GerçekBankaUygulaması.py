# PROJEYE EKLENECEK ARGÜMANLAR:
# 2. Faiz kısa ve uzun vadeli olarak eklencek.

# ─── IMPORTS ────────────────────────────────────────────────────────────────────

import math
import json 
import os 
import random
from datetime import datetime
from os.path import exists # exists fonksiyonunu import ediyoruz. Bu fonksiyon dosya var mı yok mu diye kontrol ediyor.


# ─── CONSTANTS ──────────────────────────────────────────────────────────────────


FILE_PATH = "bank.json" # json dosyasının adını belirtiyoruz


# ─── DATABASE ───────────────────────────────────────────────────────────────────


def get_data():
    """
    Reads the bank information from the data file. Yani json dosyasını okuyoruz. Veri dosyasından banka bilglilerini okuyoruz...
    """
    #  varsayılan dosya boş dosya olarak kabul edilir
    if not exists(FILE_PATH): # dosya yoksa
        return {} # boş döndür
    f = open(FILE_PATH, "r") # dosyayı okumak için aç
    data = f.read() # dosyayı oku. Burada data değişkenine json dosyasının içeriği atılıyor.
    # string json'u python objesine dönüştür
    return json.loads(data) # Burada load() şu işe yarıyor: json dosyasını okuyup, içeriğini bir python objesine dönüştürüyor.


def set_data(data): # json dosyasına veri yazmak için kullanılan fonksiyon 
    """
    Writes the bank information into the data file
    """
    f = open(FILE_PATH, "w")
    json_data = json.dumps(data) # json.dumps() fonksiyonu datayı json'a dönüştürüyor.
    f.write(json_data) # json_data değişkenini dosyaya yazıyoruz.


def get_users_as_list(): # Türkçesi "Kullanıcıları listeye dönüştür". Bu fonksiyon json dosyasındaki kullanıcıları listeye dönüştürüyor.
    """
     Bu fonksiyon kullanıcı verilerini yükler ve bunları bir sözlükten bir listeye dönüştürür ve ardından dışarıdan hesap numarasını anahtar olarak ekler.
    """
    result = [] # sonuç diye bir liste oluşturuyoruz.
    users = get_data() # json dosyasındaki verileri users değişkenine atıyoruz. Yukarıda ki fonksiyonu atıyoruz.
    for user_account_number in users: # Kullanıcı değişkeni içindeki her bir kullanıcı için
        user_data = users[user_account_number] # user_data değişkenine kullanıcı bilgilerini atıyoruz.
        user_data["account_number"] = user_account_number # Burada da user_data değişkenine account_number diye bir anahtar ekliyoruz. Bu anahtarın değeri ise user_account_number değişkeninin değeri oluyor.
        result.append(user_data) # Sonuç listesine user_data değişkenini ekliyoruz.
    results_as_ll = list_to_linked_list(result) # Sonuç listesini linked list'e dönüştürüyoruz. Linked list şu demektir: Birbirine bağlı listeler. Örneğin: 1->2->3->4->5->6->7->8->9->10
    return results_as_ll


# ─── LINKED LIST ──────────────────────────────────────────────────────────────── # Linked list şu demektir: Birbirine bağlı listeler. Örneğin: 1->2->3->4->5->6->7->8->9->10


class LinkedList:
    """
    Bağlı Liste Düğümü
    """

    def __init__(self, _value, _next): # Burada ki value ve next değişkenleri linked list'in içindeki değerleri ve bir sonraki değeri ifade ediyor.
        """
         Bir değer ve bir sonraki nesneye referans vererek düğüm oluşturur.
        """
        self.value = _value
        self.next = _next

    def index(self, index): 
        """
        Similar to A[i], this works as A.index(i) Türkçesi: A'nın i. indeksini döndürür.
        """
        if index == 0: 
            return self.value 
        else:
            if self.next == None:  # sonraki değer yoksa
                return None
            else:
                return self.next.index(index - 1) # sonraki değerin indexini döndürür. Burada index-1 dememizin sebebi: 0. indeks değil 1. indeksi döndürmesi için.

    def set_index(self, index, value):
        """
        Similar to A[i] = value, this is A.set_index(i, value) Türkçesi: A'nın i. indeksine value değerini atar.
        """
        if index == 0: # index 0 ise
            self.value = value  # value değerini atar. 
        else:
            self.next.set_index(index - 1, value) # sonraki değerin indexini value değeri ile değiştirir.

    def size(self): # linked list'in boyutunu döndürür.
        """
        Similar to len(A), this is A.size() Türkçesi: len(A) ile aynı işi yapar.
        """
        if self.next == None: # sonraki değer yoksa
            return 1 
        else:
            return 1 + self.next.size() # sonraki değerin boyutunu döndürür.

    def append(self, x): # linked list'e yeni bir değer ekler.
        """
        Appends a new node to the end of nodes. Düğüme yeni bir düğüm ekler
        """
        if self.next == None:
            self.next = LinkedList(x, None) # sonraki değer yoksa yeni bir linked list oluşturur.
        else:
            self.next.append(x) # sonraki değer varsa sonraki değerin sonuna yeni bir değer ekler.


def list_to_linked_list(arr): # listeyi linked list'e dönüştürür.
    """
    Converts a Python List to a LinkedList 
    """
    n = None  
    for i in range(len(arr) - 1, -1, -1): # listedeki her bir değer için, sondan başa doğru, 1'er 1'er azaltarak. 
        node = LinkedList(arr[i], n) # linked list oluşturur ve n değişkenini next olarak atar, n değişkeni linked list'in sonraki değerini ifade eder.
        n = node
    return n


# ─── HEAP SORT ──────────────────────────────────────────────────────────────────  # Heap sort algoritması. Heap sort algoritması bir sıralama algoritmasıdır. Bu algoritma linked list'i sıralar. 


def heap_sort(input_list, field): # input_list değişkeni linked list'i ifade eder. field değişkeni ise linked list'in içindeki değerleri ifade eder.
    """
    A custom implementation of the heap sort function that
    also gets a field and then assumes the input_list contains
    data objects. So it sorts based on a common key on all those
    functions. This makes possible to sort users based on different
    aspects, like based on full name or phone number. 

    ---Türkçesi: Yığın sıralama işlevinin özel bir uygulamasıdır ve ayrıca bir alan alır ve ardından input_list veri nesnelerini içerir.
    Bu nedenle tüm bu işlevlerde ortak bir anahtar üzerine temel alarak sıralar. 
    Bu, kullanıcıları tam adına veya telefon numarasına göre sıralamanın mümkün olmasını sağlar.
    """
    range_start = int((input_list.size()-2)/2)  # range_start değişkeni linked list'in boyutunu 2 ye böler ve 2 çıkarır
    for start in range(range_start, -1, -1): # range_start değişkeninden başlayarak 0'a kadar 1'er 1'er azaltarak döngü oluşturur.
        sift_down(input_list, field, start, input_list.size()-1) # sift_down fonksiyonunu çağırır. input_list değişkeni linked list'i ifade eder. field değişkeni ise linked list'in içindeki değerleri ifade eder. start değişkeni ise linked list'in boyutunu 2 ye böler ve 2 çıkarır. input_list.size()-1 değişkeni ise linked list'in boyutunu 1 azaltır.

    range_start = int(input_list.size()-1)  # range_start değişkeni linked list'in boyutunu 1 azaltır.
    for end_index in range(range_start, 0, -1): # range_start değişkeninden başlayarak 0'a kadar 1'er 1'er azaltarak döngü oluşturur. end_index değerinin burada kullanılma amacı linked list'in boyutunu 1 azaltmak ve sonraki değerleri sıralamaktır. 
        swap(input_list, end_index, 0) # swap fonksiyonunu çağırır. input_list değişkeni linked list'i ifade eder. end_index değişkeni linked list'in boyutunu 1 azaltır. 0 değişkeni ise linked list'in ilk değerini ifade eder.Swap fonksiyonu linked list'in ilk değerini linked list'in son değeri ile değiştirir.
        sift_down(input_list, field, 0, end_index - 1) # sift_down fonksiyonunu çağırır. input_list değişkeni linked list'i ifade eder. field değişkeni ise linked list'in içindeki değerleri ifade eder. 0 değişkeni ise linked list'in ilk değerini ifade eder. end_index - 1 değişkeni ise linked list'in boyutunu 1 azaltır ve sonraki değerleri sıralamaktır.
    return input_list


def swap(input_list, a, b): 
    """
     Python kısaltmasıyla bir listedeki iki öğeyi değiştirir.
    """
    a_value = input_list.index(a) 
    b_value = input_list.index(b)
    input_list.set_index(a, b_value)
    input_list.set_index(b, a_value)


def sift_down(input_list, field, start_index, end_index): # sift_down fonksiyonu linked list'i sıralar. 
    """
    The "Sift Down" function of the heap sort algorithm,
    customized to also include object fields.
    --Türkçesi: Yığın sıralama algoritmasının "Sift Down" işlevi, ayrıca nesne alanlarını da içeren özel bir işlevdir.
    """
    root_index = start_index # root_index değişkeni linked list'in ilk değerini ifade eder.
    while True:
        child = root_index * 2 + 1 # child değişkeni linked list'in ilk değerinin 2 katını 1 ekler.
        if child > end_index: # Eğer child değişkeni linked list'in boyutundan büyükse döngüden çıkar.
            break
        if child + 1 <= end_index and input_list.index(child)[field] < input_list.index(child + 1)[field]: # Burada ki field değişkeni linked list'in içindeki değerleri ifade eder. Eğer child değişkeni linked list'in boyutundan küçükse ve child değişkeni linked list'in içindeki değerlerden biri diğerinden küçükse child değişkeni 1 arttırılır.
            child += 1
        if input_list.index(root_index)[field] < input_list.index(child)[field]: # Burada ki field değişkeni linked list'in içindeki değerleri ifade eder. Eğer root_index değişkeni linked list'in içindeki değerlerden biri child değişkeninden küçükse root_index değişkeni child değişkeni ile değiştirilir.
            swap(input_list, child, root_index)
            root_index = child
        else:
            break


# ─── BINARY SEARCH ────────────────────────────────────────────────────────────── # Binary Search, bir veri yapısı(data structure) üzerinde belirli bir verinin aranması için kullanılan algoritmalar bütünüdür


def text_binary_search(input_list, field, query): 
    """
    A custom binary search implementation that: Özel bir binary search uygulaması 
    (1) Assumes the input_list to have elements of type object
        and then sorts by a common key in all those objects name
        "field"
         (input_list öğesinin nesne türünde öğelere sahip olduğunu varsayar
        ve sonra tüm bu nesnelerin adındaki ortak bir anahtara göre sıralar
        "field")
    (2) Make the text lowercase and trims the text in the fields
        so for example "foo bar" can match "FooBar" Türkçesi: "foo bar" "FooBar" ile eşleşebilir
    """
    low = 0 # low burada linked list'in ilk değerini ifade eder. Yani 0.
    high = input_list.size() - 1 # Burada size() metodu linked list'in boyutunu ifade eder. Ve bir azaltılır. Sondaki hariç olduğu için.
    query = make_text_searchable(query) # query değişkeni, make_text_searchable(metni aranabilir yap) fonksiyonunun içindeki değerleri ifade eder.
    while low <= high: 
        mid = math.floor((low + high) / 2) # Ortalama alınır.
        if make_text_searchable(input_list.index(mid)[field]) > query:
            high = mid - 1
        elif make_text_searchable(input_list.index(mid)[field]) < query: # Bu kodun manası: Eğer linked list'in içindeki değerlerden biri query değişkeninden büyükse linked list'in boyutu 1 azaltılır.
            low = mid + 1 # Bu kodun manası: Eğer linked list'in içindeki değerlerden biri query değişkeninden küçükse linked list'in boyutu 1 arttırılır.
        else:
            return mid
    return -1


def make_text_searchable(text):
    """
    Make the text lowercase the text and removes spaces # Türkçesi: Metni küçük harfe çevir ve boşlukları kaldır
    """
    return text.lower().replace(" ", "")


# ─── ACCOUNT NUMBER ─────────────────────────────────────────────────────────────


def generate_account_number():
    """
    Önek olarak verilen 123 rakamlarına ek olarak 3 haneli sayı ekler...
    """
    prefix = "123"
    result = ""
    for _ in range(0, 3): # burada _ kullanılmasının sebebi, for döngüsü içindeki değerlerin kullanılmamasıdır.
        random_number = random.randint(1, 9)
        result += str(random_number)

    return prefix + result # prefix değişkeni 123 rakamlarını ifade eder. result değişkeni ise 3 haneli sayıyı ifade eder.


# ─── TRANSACTION ──────────────────────────────────────────────────────────────── # Transaction, bir işlem anlamına gelir. Bu işlem bir hesaba para yatırma, para çekme, havale gibi işlemlerdir.


def perform_transaction(sender_number, receiver_number, amount):
    """
     İki hesap numarası ve bir işlem tutarı verildiğinde, bu, para gönderen hesaptan alıcının hesabına para taşır.
    """
    users = get_data() # users değişkeni get_data() fonksiyonunun içindeki değerleri ifade eder.

    if sender_number not in users: #Alıcı hesap numarası 
        print("Did not found the account with number: " + sender_number) # sender_number numaralı hesap bulunamadı.
        return  # return, fonksiyonun sonlanmasını sağlar.

    if receiver_number not in users: # Gönderen numarası users ın içinde değilse.
        print("Did not found the account with number: " + receiver_number)
        return

    if users[sender_number]["balance"] < amount:
        print("your account balance is not enough")
        return

    users[sender_number]["balance"] -= amount # Kullanıcılardaki gönderen hesap numarasının bakiyesinden gönderilen miktarı azalt.
    users[receiver_number]["balance"] += amount # ALıcının bakiyesine de ekle.

    set_data(users) # Bu fonksiyon, kullanıcıların bilgilerini günceller.

    print("Transferred ", amount, "$ from account",
          users[sender_number]["full_name"], "to", users[receiver_number]["full_name"])


# ─── update information ────────────────────────────────────────────────────────── # update information, bilgileri güncellemek anlamına gelir. Bu fonksiyon ile kullanıcı bilgilerini güncelleyebilirsiniz.


def update_information(account_number): 
    """
     Bir hesap numarası verildiğinde, bu kullanıcıdan neyi değiştirmek istediğini sorar ve ardından o özellikleri değiştirir.
    """
    users = get_data() 
    print_horizontal_line() # print_horizontal_line() fonksiyonu, yatay çizgi çizer. bu fonksiyon daha önce  tanımlanmıştır.
    print("► 1 ∙ Full Name ")
    print_horizontal_line()
    print("► 2 ∙ Gender ")
    print_horizontal_line()
    print("► 3 ∙ City ")
    print_horizontal_line()
    print("► 4 ∙ Phone Number ")
    print_horizontal_line()
    command = int(input("What to change? "))
    print_horizontal_line()
    if command == 1:
        new_name = input("New Full Name: ")
        users[account_number]["full_name"] = new_name
    if command == 2:
        new_gender = input("New Gender: ")
        users[account_number]["gender"] = new_gender
    if command == 3:
        new_city = input("New City: ")
        users[account_number]["city"] = new_city
    if command == 4:
        new_phone_number = input("New Phone Number: ")
        users[account_number]["phone_number"] = new_phone_number

    set_data(users)
    clean_terminal_screen() # clean_terminal_screen() fonksiyonu, terminal ekranını temizler. Bu fonksiyon daha önce tanımlanmıştır.
    display_account_information_by_given_account_number(account_number) # display_account_information_by_given_account_number() fonksiyonu, verilen hesap numarasına göre hesap bilgilerini gösterir. Bu fonksiyon daha önce tanımlanmıştır.


# ─── CREATE A NEW USER ────────────────────────────────────────────────────────── 


def create_new_user(full_name, balance, gender, city, phone_number):
    """
    Creates a new user with the given information.
    """
    users = get_data()
    date = datetime.today().strftime('%Y-%m-%d') # datetime.today() fonksiyonu, günün tarihini alır. strftime() fonksiyonu ise tarihi istediğimiz formatta alırız. Bunun sayesinde kayıt olduğumuz tarihi alabiliriz.
    account_number = generate_account_number() # generate_account_number() fonksiyonu, 123 rakamlarına 3 haneli sayı ekler. 
    users[account_number] = {
        "full_name": full_name,
        "gender": gender,
        "balance": balance,
        "account_creation_date": date,
        "city": city,
        "phone_number": phone_number
    }
    set_data(users) # set_data fonkisyonunda json dosyasına kullanıcı bilgilerini kaydeder.
    display_account_information_by_given_account_number(account_number)# Tercüme: Verilen hesap numarasına göre hesap bilgilerini görüntüle. 


# ─── SEARCH ACCOUNT ───────────────────────────────────────────────────────────── # Search Account, bir hesap aramak anlamına gelir. Bu fonksiyon ile kullanıcı bilgilerini arayabilirsiniz.


def search_account(field, query):
    """
    Searches the "query" from the user data in the "field" fields. türkçesi: "alan" alanlarındaki kullanıcı verilerinden "sorgu"yu arar.
    """
    users = get_users_as_list() # get_users_as_list() fonksiyonu, kullanıcıları listeye dönüştürür.
    users = heap_sort(users, field) # heap_sort() fonksiyonu, kullanıcıları sıralar. Bu fonksiyon daha önce tanımlanmıştır.
    index = text_binary_search(users, field, query) # Kulanıcıları sıraladıktan sonra users,field,query parametrelerini text_binary_search() fonksiyonuna gönderir. Bu fonksiyon daha önce tanımlanmıştır.
    if index == -1: # indeks -1 olması demek, kullanıcı bulunamadığı anlamına gelir.
        print("──── Error ──────────────────────────────────")
        print("Found no one as", query)
    else:
        user = users.index(index) # Kullanıcıyı bulduktan sonra, kullanıcı bilgilerini ekrana yazdırır.
        display_user_object(user, user["account_number"]) # buradaki birinci parametre, kullanıcı bilgilerini, ikinci parametre ise kullanıcı hesap numarasını gösterir.


# ─── DELETE AN ACCOUNT ──────────────────────────────────────────────────────────


def delete_account(account_number): 
    """
    Deletes an account if exists, otherwise displays an error. türkçesi: Hesabı varsa siler, yoksa bir hata görüntüler.
    """
    users = get_data()
    if account_number not in users:
        print("Did not found the account with number: " + account_number) 
        return
    del users[account_number] 
    set_data(users)
    print("Account number", account_number, "removed.")


# ─── INTERFACE TOOLS ──────────────────────────────────────────────────────────── # Interface Tools, arayüz araçları anlamına gelir. Bu fonksiyonlar arayüzü oluşturur.


def clean_terminal_screen():
    """
    Cleans the terminal screen by performing a system
    clear command. Cls on windows and Clear on UNIX ones. türkçesi: Sistem temizleme komutunu gerçekleştirerek terminal ekranını temizler. Windows'da cls, UNIX'te Clear.
    """
    os.system('cls' if os.name == 'nt' else 'clear') 


def print_horizontal_line():
    """
    A pretty decorative horizontal line.
    """
    print("─────────────────────────────────────────────")


# ─── DISPLAY USER OBJECT ──────────────────────────────────────────────────────── # Display User Object, bir kullanıcı nesnesini göstermek anlamına gelir. Bu fonksiyon ile kullanıcı bilgilerini görebilirsiniz.


def display_account_information_by_given_account_number(account_number): # Tercüme: Verilen hesap numarasına göre hesap bilgilerini görüntüle.
    """
    Displays the information about a given account number
    """
    users = get_data()
    user = users[account_number] 
    display_user_object(user, account_number) # display user object, kullanıcı bilgilerini gösterir.


def display_user_object(user_object, account_number):
    """
    Displays a single user object. The account_number is taken
    separately since there can be either a list input or a dictionary
    input. In a list input the account_number is within the user object
    and in the dictionary form the account_number is the key mapped
    to the dictionary. Türkçesi: Tek bir kullanıcı nesnesini görüntüler. Hesap numarası ayrı olarak alınır, çünkü bir liste girişi veya sözlük girişi olabilir. Bir liste girişinde hesap numarası kullanıcı nesnesi içindedir ve sözlük formunda hesap numarası sözlüğe eşlenen bir anahtardır.
    """
    print_horizontal_line()
    print("Full name:      ", user_object["full_name"])
    print("Account number: ", account_number)
    print("Created at:     ", user_object["account_creation_date"])
    print("Balance:        ", user_object["balance"])
    print("Gender:         ", user_object["gender"])
    print("City:           ", user_object["city"])
    print("Phone:          ", user_object["phone_number"])


def display_all_accounts_sorted_by(field): # Tercüme: Alanlara göre tüm hesapları görüntüle.
    """
    Displays all the users one after the other, sorted by a given field. Türkçesi: Verilen bir alana göre tüm kullanıcıları birbirinden sonra görüntüler.
    """
    users = get_users_as_list() # get_users_as_list() fonksiyonu, kullanıcıları listeye dönüştürür. Bu fonksiyonun kullanma amacı 
    users = heap_sort(users, field) # Heap_sort() fonksiyonuna kullanıcılar ve field parametreleri gönderilir. Bu fonksiyon daha önce tanımlanmıştır.
    clean_terminal_screen() # clean_terminal_screen() fonksiyonu, terminal ekranını temizler.
    for i in range(0, users.size()): #users.size() fonksiyonu, kullanıcıların sayısını döndürür. 0 ise başlangıç, users.size() ise bitiş değeridir.
        user = users.index(i) # users ın i. indeksini user değişkenine atar. i burada kullanıcıların sırasını gösterir.
        display_user_object(user, user["account_number"]) # display_user_object() fonksiyonu, kullanıcı bilgilerini gösterir. Burada hesap numarasını gösterir


def beatify_field_name(field):
    if field == "full_name":
        return "Full Name"
    if field == "account_creation_date":
        return "Account Creation Data"
    if field == "city":
        return "City"
    if field == "gender":
        return "Gender"
    if field == "phone_number":
        return "Phone Number"
    return "Unknown"


def ask_user_what_field_to_sort_the_display_by():
    """
    Shows a menu so that the user cas pick a field to sort the data by. Türkçesi: Verileri sıralamak için bir alan seçmesi için bir menü gösterir.
    """
    print("Sorting by:")
    print_horizontal_line()
    print("► 1 ∙ Full Name ")
    print_horizontal_line()
    print("► 2 ∙ Gender ")
    print_horizontal_line()
    print("► 3 ∙ City ")
    print_horizontal_line()
    print("► 4 ∙ Phone Number ")
    print_horizontal_line()
    print("► 5 ∙ Account Creating Date ")
    print_horizontal_line()
    print("► 6 ∙ Account Number ")
    print()
    command = input("Your option: ")
    if command == "1":
        return "full_name"
    if command == "2":
        return "gender"
    if command == "3":
        return "city"
    if command == "4":
        return "phone_number"
    if command == "5":
        return "account_creation_date"
    if command == "6":
        return "account_number"
    return "full_name"


# ─── DISPLAY MENU ───────────────────────────────────────────────────────────────

def display_menu():
    """
    Displays the welcome menu and asks the user for a
    command to perform (which then performs). Türkçesi: Hoşgeldiniz menüsünü görüntüler ve yapılacak bir komut isteyerek kullanıcıdan komut alır.

    This also acts as the UI and receives the information
    regarding of the respective functions. Türkçesi: Bu aynı zamanda UI olarak hareket eder ve ilgili fonksiyonlar hakkında bilgi alır.
    """
    clean_terminal_screen() # clean_terminal_screen() fonksiyonu, terminal ekranını temizler.

    print()

    print("  ┌────────────────┐  ╭───────────────────────╮           ")
    print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Create Account  │           ")
    print("  │  ╰┼┼╮          │  ├───────────────────────┴─────╮     ")
    print("  │  ╰┼┼╯          │  │ ▶︎ 2 • Perform Transaction   │     ")
    print("  │                │  ├────────────────────────────┬╯     ")
    print("  │  D R A G O N   │  │ ▶︎ 3 • Update Account Info  │      ")
    print("  │  B A N K       │  ├───────────────────────┬────╯      ")
    print("  │                │  │ ▶︎ 4 • Delete Account  │           ")
    print("  │                │  ├───────────────────────┴────╮      ")
    print("  │                │  │ ▶︎ 5 • Search Account Info  │      ")
    print("  │                │  ├────────────────────────────┴╮     ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 6 • View Customer's List  │     ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  ├────────────────────┬────────╯     ")
    print("  │                │  │ ▶︎ 7 • Exit System  │              ")
    print("  └────────────────┘  ╰────────────────────╯              ")

    user_choice = int(input("\n  ☞ Enter your command: "))

    clean_terminal_screen()

    if user_choice == 1:
        print("── Creating a new user ──────────────────────")
        user_name = input("Full Name: ")
        balance = float(input("Balance: "))
        gender = input("Gender: ")
        city = input("City of Residence: ")
        phone_number = input("Phone Number: ")
        create_new_user(user_name, balance, gender, city, phone_number)

    if user_choice == 2:
        print("── Requesting Transaction ───────────────────")
        sender = input("Sender's Account Number:    ")
        receiver = input("Recipient's Account Number: ")
        amount = float(input("Transaction Amount: "))
        perform_transaction(sender, receiver, amount)

    if user_choice == 3:
        print("── Changing Account Information ─────────────")
        account_number = input("Account Number To Change: ")
        update_information(account_number)

    if user_choice == 4:
        print("── Deleting an Account ──────────────────────")
        account_number = input("Account number to delete: ")
        delete_account(account_number)

    if user_choice == 5:
        print("── Search Account ───────────────────────────")
        query = input("Searching for: ")
        clean_terminal_screen()
        search_account("full_name", query)

    if user_choice == 6:
        print("── Displaying all Accounts ──────────────────")
        field = ask_user_what_field_to_sort_the_display_by()
        display_all_accounts_sorted_by(field)

        print("\n\nSorted by user", beatify_field_name(field))

    if user_choice == 7:
        quit()

    print()
    print_horizontal_line()
    input("PRESS ENTER TO CONTINUE ")
    print()


# ─── MAIN ───────────────────────────────────────────────────────────────────────


while True:
    display_menu()


# ────────────────────────────────────────────────────────────────────────────────