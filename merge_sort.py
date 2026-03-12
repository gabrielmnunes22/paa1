# MERGE SORT IMPLEMENTATION - https://www.youtube.com/watch?v=cVZMah9kEjI&t=39s

def print_arr(arr):
    for num in arr:
        print(num, end = " ")
    print()


def merge_sort(arr):
    if len(arr) > 1:
        leftArr = arr[: len(arr) // 2]       # slicing -> arr[idx_begin, idx_end)
        rightArr = arr[len(arr) // 2 :]

        # recursion
        merge_sort(leftArr)
        merge_sort(rightArr)

        # merge
        i = 0   # left array index
        j = 0   # right array index
        k = 0   # merge array index

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < len(leftArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1



arr = [5, 2, 6, 4, 1, 0]


print_arr(arr)
merge_sort(arr)
print_arr(arr)
 