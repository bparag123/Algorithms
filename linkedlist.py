class Node:
    def __init__(self, value):
        self.value  = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        return

    def print_linked_list(self):
        current_node = self.head
        while current_node.next != None:
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)    

    def insert_at(self, index, value):
        if index == 0:
            new_node = Node(value)
            old_node = self.head
            new_node.next = old_node
            self.head = new_node
            return
        current_node = self.head
        
        while index>1:
            if current_node.next != None:
                current_node = current_node.next
            else:
                print("Invalid Index")
                return
            index -= 1
        
        old_reference = current_node.next
        new_reference = Node(value)
        current_node.next = new_reference
        new_reference.next = old_reference

    def delete_at(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        while index>1:
            if current_node.next != None:
                current_node = current_node.next
            else:
                print("Invalid Index")
                return
            index-=1
        ele_to_be_deleted = current_node.next
        current_node.next = ele_to_be_deleted.next

    def search(self, value):
        current_node = self.head
        if current_node.value == value:
            return True
        while current_node.next != None:
            current_node = current_node.next
            if current_node.value == value:
                return True
        return False

ls = LinkedList()
ls.add("a")
ls.add("b")
ls.add("c")
ls.insert_at(1, 'x')
ls.print_linked_list()
ls.delete_at(0)
ls.print_linked_list()
print(ls.search('x'))