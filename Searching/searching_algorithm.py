def linear_search(the_values, target):
    """
    sequential search algorithm for unsorted sequence.
    :param the_values:
    :param target:
    :return:boolean
    """
    n = len(the_values)
    for i in range(n):
        # if the target is in the ith element, return True
        if the_values[i] == target:
            return True

    return False


def sorted_linear_search(the_values, item):
    """
    sequential search algorithm for sorted sequence.
    :param the_values:
    :param item:
    :return:
    """
    n = len(the_values)
    for i in range(n):
        if the_values[i] == item:
            return True
        elif the_values[i] > item:
            return False

    return False


def find_smallest(the_values):
    """
    find the smallest num in a unsorted sequence.
    :param the_values:
    :return:
    """
    smallest = the_values[0]
    for i in the_values:
        if i < smallest:
            smallest = i
    return smallest


def binary_search(the_values, target):
    """
    Implementation of the binary search algorithm.
    The variables low and high are used to mark the range of elements in
    the sequence currently under consideration.
    :param the_values:
    :param target:
    :return:
    """
    # Start with the entire sequence of elements.
    low = 0
    high = len(the_values) - 1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if the_values[mid] == target:
            return True
        # Or does the target precede the midpoint?
        elif target < the_values[mid]:
            high = mid - 1
        # Or does it follow the midpoint?
        else:
            low = mid + 1

    # If the sequence cannot be subdivided further, we're done.
    return False
