import ctypes


class Array:
    """
    Implements the Array ADT using arry capabilities of the ctypes module.

    A one-dimensional array is a collection of contiguous elements in which
    individual elements are identified by a unique integer subscript starting
    with zero. Once an array is created, its size cannot be changed.
    """

    def __init__(self, size):
        """
        Creates an array with size elements.
        :param size:
        """
        assert size > 0, "array size must be bigger than 0."
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.
        :return:
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the contents of the index element.
        这个方法使得数组可以使用[i]来访问第i个元素。
        :param index:
        :return:
        """
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        :param index:
        :param value:
        :return:
        """
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        """
        Clears the array by setting each element to the given value.
        :param value:
        :return:
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.
        :return:
        """
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    """
    An iterator for the Array ADT
    """

    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


class SparseMatrix:
    def __init__(self, numRows, numCols):
        """
        Creates a sparse matrix of size numRows x numCols initialized to 0.
        :param numRows:
        :param numCols:
        """
        self._num_cols = numCols
        self._listOfRows = Array(numRows)

    def numRows(self):
        return len(self._listOfRows)

    def numCols(self):
        return self.numCols()

    def __getitem__(self, index):
        pass

    def __setitem__(self, ndxTuple, value):
        predNode = None
        row, col = ndxTuple
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next

        if curNode is not None and curNode.col == col:
            if value == 0.0:
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    predNode.next = curNode.next
            else:
                curNode.value = value

        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next == curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                predNode.next = newNode



class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None