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
    minRun = 32
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
    while len(array_of_runs) > 0:
        if len(array_of_runs) == 1:
            return array_of_runs[0]
        if len(array_of_runs) == 2:
            return merge(array_of_runs[0], array_of_runs[1])
        x = array_of_runs.pop()
        y = array_of_runs.pop()
        z = array_of_runs.pop()
        if len(x) > len(y) + len(z) and len(y) > len(z):
            y = merge(z, y)
            array_of_runs.append(y)
            array_of_runs.append(x)
        else:
            if len(z) >= len(x):
                y = merge(x, y)
                array_of_runs.append(z)
                array_of_runs.append(y)
            else:
                y = merge(z, y)
                array_of_runs.append(x)
                array_of_runs.append(y)


    return array_of_runs


array = [708, 639, 364, 967, 336, 846, 468, 545, 762, 118, 320, 487, 46, 93, 247, 211, 293, 136, 884, 225, 304, 600, 676, 38, 333, 883, 332, 95, 963, 646, 451, 86, 758, 980, 255, 412, 391, 430, 507, 754, 491, 164, 279, 721, 509, 848, 604, 552, 952, 563, 269, 45, 814, 789, 478, 907, 595, 902, 176, 246, 502, 353, 639, 932, 14, 496, 728, 862, 759, 169, 345, 45, 931, 363, 695, 255, 847, 103, 86, 48, 656, 942, 509, 244, 981, 400, 644, 115, 523, 304, 123, 487, 125, 851, 777, 567, 561, 763, 236, 405]
TimSort()

