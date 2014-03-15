

def merge_sort(array):
    if len(array) < 2:
        return array

    m = len(array) / 2

    return merge(merge_sort(array[:m]), merge_sort(array[m:]))

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    array = [5, 2, 4, 6, 1, 3]
    print merge_sort(array)

