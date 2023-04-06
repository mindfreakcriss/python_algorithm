# coding=utf-8
from queue import Queue


class Deque(Queue):

    # 双向队列出队
    def pop(self, front=True):

        if self.length() > 0:
            if front:
                self._list.pop(0)
            else :
                self._list.pop()
        else:
            return False

    # 双向队列入队
    def push(self, item, front=True):
        if front:
            self._list.insert(0, item)
        else:
            self._list.append(item)

# deque = Deque()
#
# deque.push(1,True)
#
# deque.push(2,True)
#
# deque.printQueue()
#
# deque.push(3,False)
#
# deque.printQueue()
#
# deque.pop()
#
# deque.printQueue()
#
# deque.pop(False)
#
# deque.printQueue()