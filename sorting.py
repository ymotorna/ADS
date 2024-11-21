import random


def random_array(size):
    return [random.randint(-100, 100) for _ in range(size)]


#selection sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[min_index] > arr[k]:
                min_index = k
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr



# merge sort
def merge(arr1, arr2):
    arr_sorted = []
    i = 0
    u = 0
    l1 = len(arr1)
    l2 = len(arr2)
    while i < l1 and u < l2:
            if arr1[i] <= arr2[u]:
                arr_sorted.append(arr1[i])
                i += 1
            else:
                arr_sorted.append(arr2[u])
                u += 1

    if i != l1:
        for idx in range(i, l1):
            arr_sorted.append(arr1[idx])
    elif u != l2:
        for idx in range(u, l2):
            arr_sorted.append(arr2[idx])
    return arr_sorted


def mergeSort(arr):    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    return merge(a1, a2)




# arr1 = sorted(random_array(6))
# arr2 = sorted(random_array(5))
#
# print(arr1)
# print(arr2)
# arr_sorted = merge(arr1, arr2)
# print(arr_sorted)
#
# array = random_array(7)
# print(array)
# print(mergeSort(array))



# quick sort
def partition(arr, left, right, pivot):
    left_part = []
    right_part = []
    for i in range(left, right+1):
        if arr[i] <= pivot:
            left_part.append(arr[i])
        else:
            right_part.append(arr[i])
    arr[left:right+1] =  left_part + right_part
    return left + len(left_part)


def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot = arr[right]
    idx = partition(arr, left, right, pivot)
    quick_sort(arr, left, idx-1)
    quick_sort(arr, idx+1, right)


array = [85, 6, -96, 65, -55, -15]




# tests
def basic_test(sorting_func):
    arr = [5, 4, 3, 2, 1]
    sorting_func(arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mBasic test passed\033[0m")


def random_test(sorting_func):
    arr = random_array(5)
    s_arr = sorted(arr)
    print("Random array: ", arr)
    sorting_func(arr)
    print("Sorted array: ", arr)
    assert arr == s_arr, f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mRandom test passed\033[0m")


def medium_test(sorting_func):
    arr = random_array(500)
    sorting_func(arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mMedium test passed\033[0m")


def big_test(sorting_func):
    arr = random_array(100)
    arr_copy = arr.copy()

    import time
    start = time.time()
    sorting_func(arr)
    end = time.time()
    print(f"Time to sort 10,000 elements: {end - start:.6f} seconds")

    start = time.time()
    arr_copy.sort()
    end = time.time()
    print(f"Time to sort 10,000 elements with built-in sort: {end - start:.6f} seconds")

    assert arr == arr_copy, f"Expected {arr_copy}, but my sort got {arr}"
    print("\033[92mBig test passed\033[0m")

#
# sorting_func = selection_sort
# print("Selection sort")
# basic_test(sorting_func)
# random_test(sorting_func)
# medium_test(sorting_func)
# big_test(sorting_func)
#
# sorting_func = insertion_sort
# print("\nInsertion sort")
# basic_test(sorting_func)
# random_test(sorting_func)
# medium_test(sorting_func)
# big_test(sorting_func)
#
# sorting_func = quick_sort
# print("Selection sort")
# basic_test(sorting_func)
# random_test(sorting_func)
# medium_test(sorting_func)
# big_test(sorting_func)














