class Node:
    def __init__(self, value, index=0, nxt=None):
        self.value = value
        self.nxt = nxt
        self.index = index

    def get_value(self):
        return self.value

    def get_next(self):
        return self.nxt

    def get_index(self):
        return self.index


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None


    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.last = new_node
            new_node.index = 0
        else:
            tmpi = self.last.index
            self.last.nxt = new_node
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
               node = node.nxt
            return node.get_value()

    def find_index(self, value):    #найти индекс узла по значению
        node = self.head
        for i in range(self.last.index + 1):
            if value != node.value:
                node = node.nxt
            else:
                return node.get_index()
        return 'Not on the list'

    def __iter__(self):
        self.__curr = self.head
        return self

    def __next__(self):
        if self.__curr is None:
            raise StopIteration()
        val = self.__curr.get_value()
        ind = self.__curr.get_index()
        self.__curr = self.__curr.get_next()
        return ind, val

    def remove_node(self, indx):   # удаление по индексу
        if indx > self.last.index:
            raise IndexError("Index out of range")
        elif indx == self.last.index:
            node = self.head
            for i in range(indx - 1):
                node = node.nxt
            node.nxt = None
            self.last = node
        elif indx == 0:
            tmp = self.head.nxt.nxt
            self.head = self.head.nxt
            self.head.nxt = tmp
            node = self.head
            for i in range(indx, self.last.index):
                node.index -= 1
                node = node.nxt

        else:
            node = self.head
            for i in range(indx-1):
                node = node.nxt
            node.nxt = node.nxt.nxt
            for i in range(indx, self.last.index):
                node = node.nxt
                node.index -= 1
            self.last = node

    def remove_value(self, value):    # удаление по значению
        if self.find_index(value) == 'Not on the list':
            print('Not on the list')
        else:
            self.remove_node(self.find_index(value))



    def show(self):      # вывести список
        for i in self:
            print('node №{}: {}'.format(i[0], i[1]))



    def values(self):
        node = self.head
        while node:
            yield node.value
            node = node.nxt

    def display_values(self):
        for x in self.values():
            print(x, end=' ')
        print()


def decor(func):
    def wrapped():
        print('у меня не получается')
        func()
    return wrapped

@decor
def aaaa():
    print('запихнуть декоратор в класс')

aaaa()

s = LinkedList()
for i in range(7):
    s.add_to_end(i*2)

s.display_values()
