import re


class MyLinkedList:

    def __init__(self):
        self.val = None
        self.next = None


    def get(self, index: int) -> int:
        cur_node = self
        val = self.val
        for i in range(index):
            if val is None:
                return -1
            
            cur_node = cur_node.next
            val = cur_node.val
            
        return val
            

    def addAtHead(self, val: int) -> None:
        if self.val is None:
            self.val = val
        else:
            self.addAtIndex(0,val)
            print()
        
        


    def addAtTail(self, val: int) -> None:
        if self.val is None:
            self.val = val
            return
        
        head = MyLinkedList()
        head.next = self
        cur = head
        
        while cur.next is not None:
            cur = cur.next
        node = MyLinkedList()
        node.next = None
        node.val = val
        cur.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if self.val is None and index == 0:
            self.val = val
            return
        
        head = MyLinkedList()
        head.next = self
        pre = head
        for i in range(index):
            pre = pre.next
            if pre.next is None:
                break
        node = MyLinkedList()
        node.val = val
        node.next = pre.next
        pre.next = node
        
        if index == 0:
            
            p = head.next
            q = p.next
            q.val, p.val = p.val, q.val
            if q is not None:
                p.next = q.next
                q.next = p

        

    def deleteAtIndex(self, index: int) -> None:
        head = MyLinkedList()
        head.next = self
        pre = head
        if index == 0:
            if self.next is None:
                self.val = None
            else:
                self.val = self.next.val
                self.next = self.next.next
        else:
            for i in range(index):
                pre = pre.next
                if pre.next is None:
                    break
            if pre.next is not None:
                pre.next = pre.next.next
        



# Your MyLinkedList object will be instantiated and called as such:

example = [
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
,[[],[1],[3],[1,2],[1],[0],[0]]]

obj = MyLinkedList()
for idx, op in enumerate(example[0]):
    val = example[1][idx]
    if idx == 0 :
        continue
    if 'Head' in op:
        obj.addAtHead(val[0])
        print('null')
    elif 'Tail' in op:
        obj.addAtTail(val[0])
        print('null')
    elif 'addAtIndex' in op:
        obj.addAtIndex(val[0],val[1])
        print('null')
    elif 'deleteAtIndex' in op:
        obj.deleteAtIndex(val[0])
        print('null')
    elif 'get' in op:
        tmp = obj.get(val[0])
        print(tmp)
    
