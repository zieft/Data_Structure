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


class Array2D:
    """
    A two-dimensional array consists of a collection of elements organized
    into rows and columns. Individual elements are referenced by specifying
    the specific row and column indices (r, c), both of which start at 0.
    """

    def __init__(self, numRows, numCols):
        """
        Creates a 2-D array of size numRows x numCols.
        :param numRows:
        :param numCols:
        """
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array(numRows)

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(numCols):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        """
        Returns the number of rows in the 2-D array.
        :return:
        """
        return len(self._theRows)

    def numCols(self):
        """
        Returns the number of columns in the 2-D array.
        :return:
        """
        return len(self._theRows[0])

    def clear(self, value):
        """
        Clears the array by setting every element to the given value.
        :param value:
        :return:
        """
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self, ndxTuple):
        """
        Gets the contents of the element at position [r,c]
        :param ndxTuple:
        :return:
        """
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
               and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        """
        Sets the contents of the element at position [r,c] to value.
        :param ndxTuple:
        :param value:
        :return:
        """
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
               and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

