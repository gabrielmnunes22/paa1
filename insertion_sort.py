# SELECTION SORT ALGORITHM

def print_arr(arr):
    for num in arr:
        print(num, end = " ")
    print()


# first version

def insertion_sort(arr):
    for i in range(1, len(arr)):
        ref = arr[i]
        for j in range(i - 1, -1, -1):
            if ref < arr[j]:
                temp = arr[j]
                arr[j] = ref
                arr[j + 1] = temp

# optimized version

def insertion_sort_optimized(arr):
    for i in range(1, len(arr)):
        ref = arr[i]
        j = i - 1
        while j >= 0 and ref < arr[j]:
            arr[j + 1] = arr[j]         # shift right 
            j -= 1  
        arr[j + 1] = ref


arr = [5, 2, 6, 4, 1, 0]

print_arr(arr)
insertion_sort_optimized(arr)
print_arr(arr)