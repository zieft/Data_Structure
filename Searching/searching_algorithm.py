def linearSearch(the_values, target):
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

def sortedLinearSearch(the_values, item):
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

def findSmallest(the_values):
    """
    find the smallest num in a unsorted sequence.
    :param the_values:
    :return:
    """
    n = len(the_values)
    smallest = the_values[0]
    for i in the_values:
        if i < smallest:
            smallest = i
    return smallest

