class Bag:
    """
    Implements the Bag ADT using a singly linked list.
    """

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, item):
        """
        determines if an item is contained in the bag.
        :param item:
        :return:
        """
        curNode = self._head
        while curNode is not None and curNode.item != item:
            curNode = curNode.next
        return curNode is not None

    def add(self, item):
        """
        Add a new item into the bag.
        根据__init__()，bag实例被创建时只能为空，因此bag中所有的元素都是后期加进去的
        因此可以保证bag中每一个元素都是_BagListNode类的实例，因此具有next方法。
        :param item:
        :return:
        """
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def remove(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next  # next方法来自类_BagListNode，参看add()的说明

        assert curNode is not None, "The item must be in the bag!"

        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next  # unlink the current node.
        return curNode.item

    def __iter__(self):
        """
        Returns an iterator for traversing the list of items.
        :return:
        """
        return _BagIterator(self._head)

class _BagListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class _BagIterator:
    def __init__(self, listhead):
        self._curNode = listhead

    def __iter__(self):
        return self

    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item

    