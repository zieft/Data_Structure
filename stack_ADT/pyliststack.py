class Stack:
    def __init__(self):
        self._the_item = []

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._the_item)

    def peek(self):
        """
        Returns the top item on the stack without removing it.
        :return:
        """
        assert not self.is_empty(), "Cannot peek at an empty stack!"
        return self._the_item[-1]

    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack!"
        return self._the_item.pop()

    def push(self, item):
        self._the_item.append(item)
