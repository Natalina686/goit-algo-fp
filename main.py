class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо наступний вузол
            current.next = prev       # Змінюємо посилання
            prev = current            # Переміщаємо prev вперед
            current = next_node       # Переміщаємо current вперед
        self.head = prev             # Оновлюємо голову списку

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо наступний вузол
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged_list = LinkedList()
        current1 = list1.head
        current2 = list2.head
        
        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            else:
                merged_list.append(current2.data)
                current2 = current2.next
        
        # Додаємо залишки з обох списків
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next
        
        while current2:
            merged_list.append(current2.data)
            current2 = current2.next
            
        return merged_list

# Приклад
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)

    print("Початковий список:")
    ll.print_list()

    ll.reverse()
    print("Список після реверсування:")
    ll.print_list()

    ll.insertion_sort()
    print("Список після сортування вставками:")
    ll.print_list()

    # Об'єднання двох відсортованих списків
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    merged_list = LinkedList.merge_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    merged_list.print_list()