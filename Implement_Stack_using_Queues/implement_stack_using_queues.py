""""""

class Node:
    """"""
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

class MyQueue:
    """"""
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        """"""
        if self.head is None:
            self.tail = Node(val)
            self.head = self.tail
        else:
            self.head = Node(val, self.head)

    def peek(self):
        """"""
        return self.tail

    def pop(self):
        """"""
        head = self.head
        if head.next is None:
            self.head = None
            self.tail = None
            return head.data

        while head.next and head.next.next:
            head = head.next

        self.tail = head
        was = head.next
        head.next = None
        return was.data

    def __str__(self):
        head = self.head
        res = 'Queue: '
        while head:
            res += f'{head.data} -> '
            head = head.next
        return res + 'None'

    def __len__(self):
        count, head = 0, self.head
        while head:
            count += 1
            head = head.next
        return count

    def is_empty(self):
        """"""
        return self.head is None

class MyStack:
    """"""
