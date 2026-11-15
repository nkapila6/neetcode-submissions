class Node:
    def __init__(self, val:int):
        self.val = val
        self.next:Node|None = None

class MyLinkedList:
    def __init__(self):
        self.head:Node|None = None
        self.size = 0
        
    def get(self, index: int) -> int:
        curr, idx = self.head, 0
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx +=1
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size +=1
        
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        self.size +=1
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        # add a node of value val before index-th node
        if index > self.size: 
            return # if idx > length, node won't be inserted
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size: # add at tail
            self.addAtTail(val)
            return

        node = Node(val)
        # traverse and find point where idx == index
        idx, curr, prev = 0, self.head, self.head
        assert curr is not None
        assert prev is not None # silencing lsp fkin hell
        while curr.next != None:
            if idx == index:
                break
            prev = curr
            curr = curr.next
            idx += 1
        
        self.size += 1
        prev.next = node
        node.next = curr
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index <0:
            return
        
        if index == 0 and self.size == 0:
            return
        
        if index == 0:
            if self.head != None and self.head.next != None:
                self.head = self.head.next
                self.size -=1
                return

            if self.head.next == None:
                self.head = None
                self.size -=1
                return

        curr, target, prev = self.head, 0, self.head
        assert curr is not None
        assert prev is not None
        while curr.next is not None:
            if target == index:
                break
            prev = curr
            curr = curr.next
            target += 1
        
        prev.next = curr.next
        self.size -= 1
        del curr
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)