def bubble_sort(the_seq):
    """
    Sorts a sequence in ascending order using the bubble sort algorithm.
    :param the_seq:
    :return:
    """
    # Perform n-1 bubble operations on the sequence
    for i in range(len(the_seq) - 1):
        # Bubble the largest item to the end.
        for j in range(len(the_seq) - i - 1):
            if the_seq[j] > the_seq[j + 1]:
                the_seq[j + 1], the_seq[j] = the_seq[j], the_seq[j + 1]
    return the_seq


def selection_sort(the_seq):
    """
    Sorts a sequence in ascending order using the selection sort algorithm.
    :param the_seq:
    :return:
    """
    for i in range(len(the_seq)):
        # Assume the ith element is the smallest.
        small_index = i
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, len(the_seq)):
            if the_seq[j] < the_seq[small_index]:
                small_index = j

        if small_index != i:
            the_seq[i], the_seq[small_index] = the_seq[small_index], the_seq[i]
    return the_seq


def insertion_sort(the_seq):
    """
    Sorts a sequence in ascending order using the insertion sort algorithm.
    :param the_seq:
    :return:
    """
    n = len(the_seq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        value = the_seq[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < the_seq[pos - 1]:
            # Shift the items to the right during the search.
            the_seq[pos] = the_seq[pos - 1]
            pos -= 1
        the_seq[pos] = value
