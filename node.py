# coding=utf-8

class Node(object):

    def __init__(self, item):
        # 存放的元素
        self.item = item

        # 下一个指针
        self.next = None


class SingleLinkList(object):

    def __init__(self):
        self._head = None  # 头指针
        self._length = 0

    # 链表是否为空
    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    # 链表长度
    def length(self):
        return self._length

    # 链表头部增加元素
    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
        self._length += 1

    # 链表尾部增加元素
    def append(self, item):
        current = self._head
        while current.next is not None:
            current = current.next
        node = Node(item)
        current.next = node
        self._length += 1

    # 指定位置增加元素
    def insert(self, pos, item):
        current = self._head
        i = pos
        # 这个循环是循环到插入位置的上一个
        while i > 1:
            current = current.next
            i -= 1

        node = Node(item)
        node.next = current.next
        current.next = node
        self._length += 1

    # 删除节点
    def remove(self, item):
        current = self._head
        while current.next is not None:
            if current.next.item == item:
                current.next = current.next.next
                self._length -= 1
                break
            else:
                current = current.next

    # 查询节点
    def find(self, item):
        current = self._head
        while current.next is not None:
            if current.next.item == item:
                return True
            else:
                current = current.next
        return False

    # 输出链表
    def print_link_list(self):
        current = self._head
        while current is not None:
            print(current.item)
            current = current.next


# link = SingleLinkList()
#
# link.add(2)
#
# link.add(3)
#
# link.append(1)
#
# link.insert(1, 4)
#
# link.remove(1)
#
# print(link.find(4))
#
# link.print_link_list()
