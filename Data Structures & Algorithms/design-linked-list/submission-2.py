class MyLinkedList:
    def __init__(self):
        self.head = MyNode(0)
        self.tail = MyNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        for i in range(index):
            cur = cur.next
            if cur is None:
                return -1
        if cur and cur != self.tail:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = MyNode(val, self.head.next, self.head)
        node.next.prev = node
        self.head.next = node
        
    def addAtTail(self, val: int) -> None:
        node = MyNode(val, self.tail, self.tail.prev)
        self.tail.prev = node
        node.prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        
        cur = self.head.next
        for i in range(index):
            cur = cur.next
        
        node = MyNode(val, cur, cur.prev)
        cur.prev.next = node
        cur.prev = node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        for i in range(index):
            if cur == self.tail:
                return
            cur = cur.next

        if cur == self.tail:
            return    
                
        cur.next.prev = cur.prev
        cur.prev.next = cur.next
        
class MyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)