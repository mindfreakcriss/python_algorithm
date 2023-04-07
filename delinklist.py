# coding=utf-8

class Node(object):

    def __init__(self, item):
        # 存放的元素
        self.item = item

        # 下一个指针
        self.next = None

        # 上一个指针
        self.pre = None


class DeLinkList(object):

    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    # 插入头部
    def add(self, item):
        node = Node(item)

        if self.head is not None:
            node.next = self.head
            self.head.pre = node
            self.head = node
        else:
            self.head = node
            self.rear = node

    # 插入尾部
    def append(self, item):
        node = Node(item)
        self.rear.next = node
        node.pre = self.rear
        self.rear = node

    # 插入中间
    def insert(self, pos, item):
        node = Node(item)
        current = self.head

        i = pos

        while i > 1:
            current = current.next
            i -= 1

        node.next = current.next
        current.next.pre = node
        node.pre = current
        current.next = node


    # 输出
    def print_link(self):
        current = self.head
        print("-----")
        while current is not None:
            print("前指针", current.pre)
            print("当前指针", current)
            print("后指针", current.next)
            current = current.next


# de = DeLinkList()
# de.add(1)
# de.print_link()
#
# de.add(2)
#
# de.append(3)
#
# de.print_link()