
def insertion_sort(input_arr) -> list: # just remove output_arr and directly make changes in input_arr for inplace algo
    output_arr = input_arr.copy()
    for i in range(1, len(output_arr)):
        j = i
        while j >= 1 and output_arr[j] <= output_arr[j - 1]:
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


def counting_sort(arr, key_max=None) -> list:  # Assuming the key is the input itself
    if key_max is None:  # Adds to the time complexity.
        key_max = max(arr)
    n = len(arr)
    output = []
    k = [0 for _ in range(key_max + 1)]
    for i in range(n):
        k[arr[i]] += 1
    for i in range(len(k)):
        for j in range(k[i]):
            output.append(i)
    return output


def counting_sort_for_radix_sort(arr, max_key=None):
    output = []
    n = len(arr)
    if max_key is None:
        k = [[] for _ in range(10)]
    else:
        k = [[] for _ in range(max_key+1)]
    for i in range(n):
        elem = arr[i]
        if k[elem.key] is None:
            k[elem.key] = [elem]
        else:
            k[elem.key].append(elem)
    for i in range(len(k)):
        if k[i] is None:
            continue
        for val in k[i]:
            output.append(val)
    return output


def radix_sort(arr, arr_max=None) -> list:
    if arr_max is None:
        arr_max = max(arr)
    inp = [RadixStruct(1, v) for v in arr]
    n = len(arr)
    divisor = 1
    while arr_max > 0:
        out = counting_sort_for_radix_sort(inp)
        divisor = divisor*10
        arr_max = arr_max//10
        inp = [RadixStruct(divisor, v.value) for v in out]
    return [v.value for v in out]


class RadixStruct:
    def __init__(self, divisor, value):
        self.key = (value//divisor) % 10
        self.value = value
