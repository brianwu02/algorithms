# Insertion Sort

def insertion_sort(A):
    print("%s") % (A)
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            print("A[%s]: %s > %s, swapping A[%s]: %s and A[%s]: %s") % (
                    i, A[i], key, i, A[i], i+1, A[i+1]
                    )
            A[i+1] = A[i] # swap elements
            i = i - 1
            print ("%s \n") % (A)
        A[i+1] = key
    print A
    return A


if __name__ == "__main__":
    array = [5, 2, 4, 6, 1, 3]
    sorted_array = insertion_sort(array)
