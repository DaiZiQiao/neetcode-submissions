# Design Double-Ended Queue

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail =Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)

        prev_node = self.tail.prev
        prev_node.next = new_node
        new_node.next = self.tail
        new_node.prev = prev_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        next_node = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = next_node
        next_node.prev = new_node
    
    def pop(self) -> int:
        if self.isEmpty():
            return -1

        prev_node = self.tail.prev.prev
        value = prev_node.next.val
        prev_node.next = self.tail
        self.tail.prev = prev_node
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        next_node = self.head.next.next
        value = next_node.prev.val
        self.head.next = next_node
        next_node.prev = self.head
        return value
