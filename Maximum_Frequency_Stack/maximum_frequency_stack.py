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
