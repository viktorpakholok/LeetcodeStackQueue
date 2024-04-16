""""""

class Node:
    """"""
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self) -> str:
        return f'Node({self.data}, {self.next})'


class MyStack:
    """"""
    def __init__(self) -> None:
        self.head = None

    def push(self, val):
        """"""
        if self.head is None:
            self.head = Node(val)
        else:
            self.head = Node(val, self.head)

    def pop(self):
        """"""
        was = self.head.data
        self.head = self.head.next
        return was

    def peek(self):
        """"""
        return self.head.data

    def empty(self):
        """"""
        return self.head is None

    def __str__(self) -> str:
        """"""
        head = self.head
        res = 'Stack: '
        while head:
            res += str(head.data) + ' -> '
            head = head.next
        return res + 'None'


class MyQueue:
    """"""
    def __init__(self):
        self.one_s = MyStack()
        self.sec_s = MyStack()

    def push(self, x: int) -> None:
        """"""
        self.one_s.push(x)

    def pop(self) -> int:
        """"""
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        ret = self.one_s.pop()
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        return ret

    def peek(self) -> int:
        """"""
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        ret = self.one_s.head.data
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        return ret

    def empty(self) -> bool:
        """"""
        return self.one_s.head is None
