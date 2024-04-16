"""A module with realised Stack using two queues"""

class Node:
    """A class representing a node in a linked list"""
    def __init__(self, data: int, next_ = None):
        self.data = data
        self.next = next_

class MyQueue:
    """A class representing a queue data structure using linked lists"""
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:
        """Pushes an element in the queue"""
        if self.head is None:
            self.tail = Node(val)
            self.head = self.tail
        else:
            self.head = Node(val, self.head)

    def peek(self) -> int:
        """Returns the value of the last element in the queue"""
        return self.tail

    def pop(self) -> int:
        """Removes and returns the front element from the queue"""
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

    def __str__(self) -> str:
        head = self.head
        res = 'Queue: '
        while head:
            res += f'{head.data} -> '
            head = head.next
        return res + 'None'

    def __len__(self) -> int:
        count, head = 0, self.head
        while head:
            count += 1
            head = head.next
        return count

    def is_empty(self) -> bool:
        """Checks if the queue is empty"""
        return self.head is None

class MyStack:
    """A class representing a stack data structure using two queues"""
    def __init__(self):
        self.one_q = MyQueue()
        self.two_q = MyQueue()

    def push(self, val: int) -> None:
        """Pushes an element onto the stack"""
        self.one_q.push(val)

    def pop(self) -> int:
        """Removes and returns the top element from the stack"""
        head = self.one_q.head
        while head.next:
            self.two_q.push(self.one_q.pop())

        self.one_q, self.two_q = self.two_q, self.one_q
        return self.two_q.pop()

    def top(self) -> int:
        """Returns the value of the top element without removing it"""
        head = self.one_q.head
        while head.next:
            self.two_q.push(self.one_q.pop())

        ret  = self.one_q.pop()
        self.two_q.push(ret)

        self.one_q, self.two_q = self.two_q, self.one_q
        return ret

    def empty(self) -> bool:
        """Checks if the stack is empty"""
        return self.one_q.is_empty()
