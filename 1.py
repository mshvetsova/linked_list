class Node:
    def __init__(self, value, index=0, next=None,):
        self.value = value
        self.next = next
        self.index = index

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_index(self):
        return self.index


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None


    def del_list(self):
        return self.head is None

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.last = new_node
            new_node.index = 0
        else:
            tmpi = self.last.index
            self.last.next = new_node
            self.last = new_node
            self.last.index = tmpi + 1

    def __len__(self):
        return self.last.index

    def find_value(self, indx):   #найти значение узла по индексу
        if indx > self.last.index:
            raise IndexError("Index out of range")
        else:
            node = self.head
            for i in range(indx):
               node = node.next
            return node.get_value()

    def find_index(self, value):    #найти индекс узла по значению
        node = self.head
        for i in range(self.last.index + 1):
            if value != node.value:
                node = node.next
            else:
                return node.get_index()
        return 'Not on the list'
