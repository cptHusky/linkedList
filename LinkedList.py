class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        
    def __iter__(self): #? Возвращает экземпляр класса, как это указать? Я где-то видел -> Iterator[self], это было бы верно?
        self.current = self.head
        return self

    def __next__(self):
        if self.current is not None:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    def __getitem__(self, index: int):
        current_node = self.head
        i = 0
        while current_node is not None and i < index:
            current_node = current_node.next
            i += 1
        if i == index and current_node is not None:
            return current_node.data
        else:
            raise IndexError('Index out of range')

    def __len__(self) -> int:
        i = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            i += 1
        return i

    @classmethod
    def is_the_same_type(cls, arg: any) -> bool:
        return isinstance(arg, cls)

    def append(self, data, after=None) -> None:
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

    def prepend(self, data) -> None:
        self.length += 1
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, index=None) -> None:
        if len(self) == 0:
            raise IndexError('Index out of range')
        if index is None:
            return
        else:
            self.length -= 1
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

    def print_list(self) -> None:
        i = 0
        current_node = self.head
        while current_node is not None:
            print(f'N{i} = {current_node.data}')
            current_node = current_node.next
            i += 1



class Comparison:

    def __eq__(self, other) -> bool:
        return len(self) == len(other)

    def __ne__(self, other) -> bool:
        return len(self) != len(other)

    def __lt__(self, other) -> bool:
        return len(self) < len(other)

    def __gt__(self, other) -> bool:
        return len(self) > len(other)

    def __le__(self, other) -> bool:
        return len(self) <= len(other)

    def __ge__(self, other) -> bool:
        return len(self) >= len(other)


class GreatLinkedList(LinkedList, Comparison):
    
    def __init__(self):
        super().__init__()   

    def find(self, data=None) -> int:
        if data is None:
            return
        for i in range(len(self)):
            if self[i] == data:
                return i
        else:
            raise ValueError('Element is not in the list')
