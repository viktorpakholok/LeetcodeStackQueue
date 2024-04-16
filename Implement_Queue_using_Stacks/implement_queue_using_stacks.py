"""Module with implemtentation of Queue with 2 stacks"""

class Node:
    """A class representing a node in a linked list"""
    def __init__(self, data: int, next_ = None):
        self.data = data
        self.next = next_

    def __repr__(self) -> str:
        return f'Node({self.data}, {self.next})'


class MyStack:
    """A class representing a stack data structure using a linked list"""
    def __init__(self) -> None:
        self.head = None

    def push(self, val: int) -> None:
        """Pushes a new element onto the stack"""
        if self.head is None:
            self.head = Node(val)
        else:
            self.head = Node(val, self.head)

    def pop(self) -> int:
        """Removes and returns the top element from the stack"""
        was = self.head.data
        self.head = self.head.next
        return was

    def peek(self) -> int:
        """Returns the value of the top element without removing it"""
        return self.head.data

    def empty(self) -> bool:
        """Checks if the stack is empty"""
        return self.head is None

    def __str__(self) -> str:
        """Returns a string representation of the stack"""
        head = self.head
        res = 'Stack: '
        while head:
            res += str(head.data) + ' -> '
            head = head.next
        return res + 'None'


class MyQueue:
    """A class representing a queue data structure using two stacks"""
    def __init__(self):
        self.one_s = MyStack()
        self.sec_s = MyStack()

    def push(self, val: int) -> None:
        """Pushes an element into the queue"""
        self.one_s.push(val)

    def pop(self) -> int:
        """Removes and returns the front element from the queue"""
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        ret = self.one_s.pop()
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        return ret

    def peek(self) -> int:
        """Returns the value of the front element without removing it"""
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        ret = self.one_s.head.data
        while self.one_s.head:
            self.sec_s.push(self.one_s.pop())

        self.one_s, self.sec_s = self.sec_s, self.one_s
        return ret

    def empty(self) -> bool:
        """Checks if the queue is empty"""
        return self.one_s.head is None
