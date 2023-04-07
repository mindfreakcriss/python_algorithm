# coding=utf-8

class Node(object):

    def __init__(self, item):
        # 存放的元素
        self.item = item

        # 下一个指针
        self.next = None


class CircleLink(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, item):
        node = Node(item)
        if self.head is not None:
            current = self.head
            while current.next is not self.head:
                current = current.next

            # current 为最后一个节点
            current.next = node
            node.next = self.head
            self.head = node
        else:
            node.next = node
            self.head = node

    def remove(self, item):
        if self.head is not None:
            current = self.head

            # 增加一个尾指针比较好？删除头还得走一圈
            if current.item is item:
                temp = current
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            else:
                while current.next is not self.head:
                    if current.next.item is item:
                        current.next = current.next.next

