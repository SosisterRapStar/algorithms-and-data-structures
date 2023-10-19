def merge(array1, array2):
    new_arr = array1 + array2
    a1 = 0
    a2 = 0
    i = 0
    while a2 != len(array2) and a1 != len(array1):
        if array1[a1] > array2[a2]:
            new_arr[i] = array2[a2]
            a2 += 1
        else:
            new_arr[i] = array1[a1]
            a1 += 1
        i += 1

    while a1 < len(array1):
        new_arr[i] = array1[a1]
        a1 += 1
        i += 1
    while a2 < len(array2):
        new_arr[i] = array2[a2]
        a2 += 1
        i += 1
    return new_arr


# def merge_sort(array):
#     if len(array) <= 2:
#         if array[0] > array[len(array) - 1]:
#             array[0], array[len(array) - 1] = array[len(array) - 1], array[0]
#         return array
#     new_index = len(array) // 2
#     left = merge_sort(array[0:new_index])
#     right = merge_sort(array[new_index:len(array)])
#
#     return merge(left, right)


def binaryInsertionSort(left_p, right_p, a):
    global array
    el = array[a]
    left = left_p
    right = right_p
    while left < right:
        mid = (right + left) // 2
        if array[mid] > array[a]:
            right = mid
        else:
            left = mid + 1
    print(left)
    for i in range(a, left, -1):
        array[i], array[i - 1] = array[i - 1], array[i]

def reversedBinaryInsertionSort(left_p, right_p, a):
    global array
    el = array[a]
    left = left_p
    right = right_p
    while left < right:
        mid = (right + left) // 2
        if array[mid] < array[a]:
            right = mid
        else:
            left = mid + 1
    print(left)
    for i in range(a, left, -1):
        array[i], array[i - 1] = array[i - 1], array[i]





def reverse(index1, index2):
    global array
    while index1 < index2:
        array[index1], array[index2] = array[index2], array[index1]
        index1 += 1
        index2 -= 1

def getMinRun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

def TimSort():
    global array
    minRun = 3
    pointer = 0
    pointer = 0
    array_of_runs = []
    while pointer < len(array) - 1:
        start_run = pointer
        if array[pointer] < array[pointer + 1]:     #increment subsequence
            if start_run + minRun < len(array):
                for pointer in range(start_run, start_run + minRun - 1):
                    if array[pointer] > array[pointer + 1]:
                        binaryInsertionSort(start_run, pointer, pointer + 1)
            else:
                for pointer in range(start_run, len(array) - 1):
                    if array[pointer] > array[pointer + 1]:
                        binaryInsertionSort(start_run, pointer, pointer + 1)
            while pointer + 1 < len(array) and array[pointer] <= array[pointer + 1]:
                pointer += 1

        else:                                       #decrement subsequence
            if start_run + minRun < len(array):
                for pointer in range(start_run, start_run + minRun - 1):
                    if array[pointer] < array[pointer + 1]:
                        reversedBinaryInsertionSort(start_run, pointer, pointer + 1)
            else:
                for pointer in range(start_run, len(array) - 1):
                    if array[pointer] < array[pointer + 1]:
                        reversedBinaryInsertionSort(start_run, pointer, pointer + 1)
            while pointer + 1 < len(array) and array[pointer] >= array[pointer + 1]:
                pointer += 1
            reverse(start_run, pointer)
        array_of_runs.append(array[start_run: pointer + 1])
        pointer += 1
    print(merging(array_of_runs))


def merging(array_of_runs):
    while len(array_of_runs) >= 3:
        if len(array_of_runs[2]) > len(array_of_runs[0]) + len(array_of_runs[1]) :
            if len(array_of_runs[0]) > len(array_of_runs[1]):
                new = merge(array[0], array[1])
                array_of_runs.pop(0)
                array_of_runs[0] = new
            else:
                a = min(array_of_runs[0], array_of_runs[2])
                new = merge(array_of_runs[1], a)
                array_of_runs.pop(0)
                array_of_runs[0] = new
        else:
            a = min(array_of_runs[0], array_of_runs[2])
            new = merge(array_of_runs[1], a)
            array_of_runs.pop(0)
            array_of_runs[0] = new
    if len(array_of_runs) == 2:
        new = merge(array_of_runs[0], array_of_runs[1])
        array_of_runs.pop()
        return new
    return array_of_runs


array = [6, 10, 54, 2, 1, 3, 4, 5, 6, 7, 7, 7, 68, 3,43, 12, 32, 1]
TimSort()

