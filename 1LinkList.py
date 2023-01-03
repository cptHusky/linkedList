class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def append(self, value):
        end = Node(value)
        _ = self
        while _.next:
            _ = _.next
        _.next = end


if __name__ == '__main__':
    llist = Node()
    llist.append(2)
    llist.append(3)
    node = llist
    print(node.data)
    while node.next:
        node = node.next
        print(node.data)
