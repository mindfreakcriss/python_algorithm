# coding=utf-8

class Queue:

    _list = []
    _size = 0

    def length(self):
        return self._size

    # O(1)
    def push(self, item):
        self._size += 1
        return self._list.append(item)

    # O(n)
    def pop(self):
        if self.length() > 0:
            self._size -= 1
            return self._list.pop(0)
        else:
            return False

    def print_queue(self):
        string = "当前队列元素：["
        for x in self._list:
            string = string + " " + str(x)
        string = string + "]"

        print(string)


# queue = Queue()
#
# queue.push(1)
#
# queue.push(2)
#
# queue.push(3)
#
# queue.printQueue()
#
# queue.pop()
#
# queue.printQueue()