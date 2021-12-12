import time
import pickle


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        delta = (te - ts) * 1000
        print(f'{method.__name__} was working for {delta:2.2f} ms')
        return result
    return timed


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

    @timeit
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

    @timeit
    def find_value(self, indx):   # найти значение узла по индексу
        if indx > self.last.index:
            raise IndexError("Index out of range")
        else:
            node = self.head
            for i in range(indx):
               node = node.nxt
            return node.get_value()

    @timeit
    def find_index(self, value):    # найти индекс узла по значению
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

    @timeit
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

    @timeit
    def remove_value(self, value):    # удаление по значению
        if self.find_index(value) == 'Not on the list':
            print('Not on the list')
        else:
            self.remove_node(self.find_index(value))

    @timeit
    def show_list(self):      # вывести список
        for i in self:
            print('node №{}: {}'.format(i[0], i[1]))

    def values(self):
        node = self.head
        while node:
            yield node.value
            node = node.nxt

    @timeit
    def display_values(self):  # вывести значения
        for x in self.values():
            print(x, end=' ')
        print()

    @timeit
    def add_after_node(self, index, value):   # добавить значение после узла с данным индексом
        if index > self.last.index:
            raise IndexError("Index out of range")
        elif index == self.last.index:
            self.add_to_end(value)
        elif index == -1:                    # если надо добавить первым, то индекс=-1, я об этом заранее не подумала))
            new_node = Node(value)
            new_node.nxt = self.head
            self.head = new_node
            node = self.head.nxt
            for i in range(self.last.index + 1):
                node.index += 1
                node = node.nxt
        else:
            node = self.head
            for i in range(index):
                node = node.nxt
            new_node = Node(value)
            new_node.index = index
            new_node.nxt = node.nxt
            node.nxt = new_node
            for j in range(index, self.last.index + 1):
                node = node.nxt
                node.index += 1



s = LinkedList()
for i in range(6):
    s.add_to_end(i*2)


with open("data.pickle", "wb") as f:   # сохраним изначальный список в файл
    pickle.dump(s, f)

with open("data.pickle", "rb") as f:   # десериализация
    p = pickle.load(f)

p.display_values()

# дальше просто проверка работы
p.remove_value(4)
print('список после удаления значения:')
p.show_list()
p.add_after_node(2, 11)
print("список после добавления значения:")
p.show_list()
print("поиск по индексу:", p.find_value(3))
print('поиск по значению:', p.find_index(11))
