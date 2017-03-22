class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traversal(self, head):
        curNode = head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    def unorderedSearch(self, head, target):
        curNode = head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None
    
