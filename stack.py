# coding=utf-8

class Stack:

    _list = []

    # 输出长度
    def length(self):
        return len(self._list)

    # 弹出一个栈元素
    def pop(self):
        if self.length() != 0:
            self._list.pop()
            return True
        else:
            return False

    # 推入一个栈元素
    def push(self, item):
        self._list.append(item)

    # 输出栈元素
    def print_stack(self):
        print("当前的栈内容 : ")
        print("--")
        length = self.length()
        while length > 0:
            print(self._list[length - 1])
            length = length - 1
        print("--")


stack = Stack()

a = stack.pop()

print(a)

stack.push(10)

stack.print_stack()

stack.push(11)

stack.print_stack()

stack.push(12)

stack.print_stack()

print(stack.pop())

stack.print_stack()