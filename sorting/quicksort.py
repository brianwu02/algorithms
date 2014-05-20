# naive quicksort implementation where O(n) extra storage space.

def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) <= 1:
        return array
    # select and remove a pivot from an array. select the leftmost.
    pivot = array[0]
    for element in array:
        if element < pivot:
            less.append(element)
        if element == pivot:
            equal.append(element)
        if element > pivot:
            greater.append(element)
    return quicksort(less) + equal + quicksort(greater)


if __name__ == "__main__":
    print quicksort(array=[20, 10, 5, 1, 3, 4, 8, 2, 5])
