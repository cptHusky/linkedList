class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                if current_node.next is not None:
                    current_node.next.prev = current_node
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

if __name__ == '__main__':
    a = DoublyLinkedList()
    a.append(1)
    a.append(2)
    a.prepend(3)
    a.print_list()