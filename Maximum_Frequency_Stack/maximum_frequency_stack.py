"""A module with an implemented Frequency Stack"""

class Node:
    """A class representing a node in a linked list"""
    def __init__(self, data, amount = 1, next_ = None):
        self.data = data
        self.amount = amount
        self.next = next_

    def __str__(self) -> str:
        res = 'Node: '
        head = self
        while head:
            res += f'({head.data}, {head.amount}) -> '
            head = head.next
        return res + 'None'


class FreqStack:
    """A class representing a frequency stack"""
    def __init__(self):
        self.head = None
        self.max_ = 1

    def push(self, val: int) -> None:
        """Pushes a value onto the frequency stack"""
        if self.head is None:
            self.head = Node(val, 1)
        else:
            head = self.head
            to_rem = 1
            while head:
                if head.data == val:
                    to_rem = head.amount + 1
                    if to_rem > self.max_:
                        self.max_ = to_rem
                    break
                head = head.next
            self.head = Node(val, to_rem, self.head)

    def pop(self) -> int:
        """Removes and returns the most frequently occurring value from the stack"""
        head = self.head

        if head.amount == self.max_:
            was = head.data
            self.head = head.next
            head_1 = self.head
            while head_1:
                if head_1.amount == self.max_:
                    return was
                head_1 = head_1.next
            self.max_ -= 1
            return was

        while head:
            if head.next and head.next.amount == self.max_:
                was = head.next.data
                head.next = head.next.next
                head_1 = self.head
                while head_1:
                    if head_1.amount == self.max_:
                        return was
                    head_1 = head_1.next
                self.max_ -= 1
                return was
            head = head.next
        return None

    def __str__(self) -> str:
        head = self.head
        res = 'FreqStack: '
        while head:
            res += f'({head.data}, {head.amount}) -> '
            head = head.next

        return res + 'None'
