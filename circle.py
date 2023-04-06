# coding=utf-8

from queue import Queue

# 循环队列必须是固定的数组容量


class Circle(Queue):

    # 总长度
    _size = 0

    # 头指针
    _front = 0

    # 尾指针
    _rear = 0

    # 当前指针
    _cnt = 0

    def __init__(self, size):
        self._size = size
        self._list = [None] * size # 预先填充所有值

    # 计算长度
    def length(self):
        return (self._rear - self._front + self._size) % self._size

    # 入队 O(1)
    def push(self, item):

        # 判断是否是满的 ==> 尾部 + 1 取余 size  等于头 --> 追上头

        if (self._rear + 1) % self._size == self._front:
            print("the queue is full")
        else:
            self._list[self._rear] = item
            self._rear = (self._rear + 1) % self._size

    # 出队 O(1)
    def pop(self):

        # 判断是否为空 头 == 尾

        if self._rear == self._front:
            print("the queue is empty!!")
        else:
            data = self._list[self._front]
            self._list[self._front] = None
            self._front = (self._front + 1) % self._size
            return data

    def print_queue(self):
        print("当前队列数据：[")
        for i in range(self._size):
            print(self._list[i])
        print("]")


circle = Circle(4)

circle.push(1)

circle.push(2)

circle.push(3)

circle.push(4)

circle.push(5)

circle.print_queue()

circle.pop()

circle.print_queue()

