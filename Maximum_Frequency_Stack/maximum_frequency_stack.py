""""""

class Node:
    """"""
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
    """"""
    def __init__(self):
        self.head = None
        self.max_ = 1

    def push(self, val: int) -> None:
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
