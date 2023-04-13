class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    index = 0

    def __init__(self):
        self.head = None
        self.length = 0

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.index < len(self):
            node = self.current.data
            self.current = node.next
            return node
        else:
            raise StopIteration

    @classmethod
    def is_the_same_type(cls, arg: any) -> bool:
        return isinstance(arg, cls)

    def append(self, data, after=None):
        self.length += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print('List was empty, Node was added as Head')
            return
        # current_node = self.head
        if after is None:
            current_node = self.head #? Точно ли нужно, если есть строка выше?
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        else:
            current_node = self.head #? Точно ли нужно, если есть строка выше?
            while current_node is not None:
                if current_node.data == after:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                current_node = current_node.next
            raise ValueError('Node not found in list')

    def prepend(self, data):
        self.length += 1
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, index=None,):
        self.length -= 1
        if index is None:
            return
        else:
            if index == 0:
                self.head = self.head.next
                #? Нормально ли то, что я не удаляю явно хэд? Это будет утекающая память? Возможно, надо разобраться самому.
                return
            current_node = self.head
            i = 0
            while current_node.next is not None and i < index - 1:
                current_node = current_node.next
                i += 1
            if i == index - 1 and current_node.next is not None:
                current_node.next = current_node.next.next
                return
            else:
                raise IndexError('Index out of range')

###
    def get_node(self, index):
        current_node = self.head
        i = 0
        while current_node is not None and i < index:
            current_node = current_node.next
            i += 1
        if i == index and current_node is not None:
            return current_node.data
        else:
            raise IndexError('Index out of range')
###
    def print_list(self):
        i = 0
        current_node = self.head
        while current_node is not None:
            print(f'N{i} = {current_node.data}')
            current_node = current_node.next
            i += 1

    
class Comparison:

    def __eq__(self, other):
        return len(self) == len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __ge__(self, other):
        return len(self) >= len(other)


class GreatLinkedList(Comparison, LinkedList):
###
    def __getitem__(self, index):
        return self.get_node(index)
###    
    def __len__(self):
        i = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            i += 1
        return i
    
    def find(self, data) -> int:
        pass

        
if __name__ == '__main__':
    a = GreatLinkedList()
    b = GreatLinkedList()
    a.append(1)
    a.append(2, 1)
    a.append(3, 2)
    a.append(4, 2)
    a.prepend(5)
    a.print_list()
    # a.delete_node(1)
    print()
    # a.print_list()
    print(next(a))
    print()
    print(a == b)
    print(a != b)
    print(a < b)
    print(a > b)
    print(a <= b)
    print(a >= b)
