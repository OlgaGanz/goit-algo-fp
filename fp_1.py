class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print("None\n")

    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def sorted_insert(self, head_ref, new_node):
        current = None

        if (head_ref == None or (head_ref).data >= new_node.data):
            new_node.next = head_ref
            head_ref = new_node
        else:
            current = head_ref
            while (current.next != None and
                    current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        return head_ref

    def insertion_sort(self, head_ref):
        sorted = None
        current = head_ref

        while (current != None):
            next = current.next
            sorted = self.sorted_insert(sorted, current)
            current = next

        head_ref = sorted
        return head_ref

    def merge_sorted_lists(self, list_1, list_2):
        head_1 = list_1.head
        head_2 = list_2.head
        dummyNode = Node(0)
        tail = dummyNode

        while True:
            if head_1 is None:
                tail.next = head_2
                break
            if head_2 is None:
                tail.next = head_1
                break

            if head_1.data <= head_2.data:
                tail.next = head_1
                head_1 = head_1.next
            else:
                tail.next = head_2
                head_2 = head_2.next
    
            tail = tail.next
    
        return dummyNode.next

if __name__ == '__main__':

    first_list = LinkedList()

    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Зв'язний список:")
    first_list.print_list()

    first_list.reverse()
    print("Зв'язний список після реверсування:")
    first_list.print_list()

    first_list.head = first_list.insertion_sort(first_list.head)
    print("Зв'язний список відсортовано:")
    first_list.print_list()

    second_list = LinkedList()
    second_list.insert_at_beginning(59)
    second_list.insert_at_beginning(35)
    second_list.insert_at_beginning(20)
    print("Другий зв'язний список:")
    second_list.print_list()

    first_list.merge_sorted_lists(first_list, second_list)
    print("Зв'язний список відсортовано та замерджено:")
    first_list.print_list()
