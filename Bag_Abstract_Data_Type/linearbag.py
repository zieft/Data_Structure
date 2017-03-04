class Bag:
    """
    Implements the Bag ADT container using a Python list.
    """
    def __init__(self):
        """
        Constructs an empty bag.
        """
        self._theItems = []

    def __len__(self):
        """
        Returns the number of items in the bag.
        :return:
        """
        return len(self._theItems)

    def __contains__(self, item):
        """
        Determines if an item is contained in the bag.
        :param item:
        :return:
        """
        return item in self._theItems

    # Adds a new item to the bag.
    def add(self, item):
        self._theItems.append(item)

    # Removes and returns an instance of the item from the bag.
    def remove(self, item):
        assert item in self._theItems.index(item)
        ndx = self._theItems.pop(ndx)

    # Returns an iterator for traversing the list of items
    def __iter__(self):
        return _BagIterator(self._theItems)

class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
