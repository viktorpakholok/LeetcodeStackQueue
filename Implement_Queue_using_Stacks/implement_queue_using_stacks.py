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
