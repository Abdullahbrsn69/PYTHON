# Bu projede Linked List algoritmasına örnek yapacağız.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self): # burada başlangıçta bir head node oluşturuyoruz.
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head 
        while cur.next != None: 
            cur = cur.next
        cur.next = new_node

    def length(self): # bu fonksiyonun amacı listenin uzunluğunu bulmak.
        cur = self.head
        total = 0
        while cur.next != None: 
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = [] #  Eğer bu listeyi oluşturmazsak sadece son elemanı gösterir.
        cur_node = self.head # Geçerli düğüm = Baş
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    def delete(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node # Geçerli düğümü geçici olarak saklıyoruz.
            cur_node = cur_node.next # Geçerli düğümü bir sonraki düğüme eşitliyoruz.
            if cur_idx == index:  # Eğer geçerli düğüm index'e eşitse
                last_node.next = cur_node.next #  Geçerli düğümü bir sonraki düğüme eşitliyoruz.
                return  # ve fonksiyondan çıkıyoruz.
            cur_idx += 1  # Eğer geçerli düğüm index'e eşit değilse geçerli düğümü bir sonraki düğüme eşitliyoruz.

my_list = LinkedList()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
print("Element at 2nd index: %d" % my_list.get(2))
my_list.delete(1)
my_list.display()

# Output:
# []
# [1, 2, 3, 4, 5]
# Element at 2nd index: 3
# [1, 3, 4, 5]
