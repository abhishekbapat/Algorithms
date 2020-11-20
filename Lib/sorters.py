
def insertion_sort(input_arr) -> list: # just remove output_arr and directly make changes in input_arr for inplace algo
    output_arr = input_arr.copy()
    for i in range(1, len(output_arr)):
        j = i
        while j >= 1 and output_arr[j] <= output_arr[ j -1]:
            temp = output_arr[j]
            output_arr[j] = output_arr[ j -1]
            output_arr[ j -1] = temp
            j = j - 1
    return output_arr


def merge_sort(input_arr) -> list:
    ans = []
    if len(input_arr) == 0:
        return ans
    if len(input_arr) == 1:
        return input_arr
    n = len(input_arr) // 2
    left = merge_sort(input_arr[:n])
    right = merge_sort(input_arr[n:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    if i < len(left):
        for n in left[i:]:
            ans.append(n)
    else:
        for n in right[j:]:
            ans.append(n)
    return ans


def heap_sort(input_arr) -> list:
    arr = input_arr.copy()
    n = len(arr)
    for i in range(n//2-1, -1, -1): # Build max heap
        max_heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        max_heapify(arr, i, 0)
    return arr


def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left<n and arr[left] > arr[largest]:
        largest = left
    if right<n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        max_heapify(arr, n, largest)