import time
import random


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

def get_minrun(n):
    r = 0
    while n >= 64:
        r = r | (n & 1)
        n //= 2
    return n + r
def binaryInsertionSort(array, left_p, right_p, a):

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

def reversedBinaryInsertionSort(array, left_p, right_p, a):
    el = array[a]
    left = left_p
    right = right_p
    while left < right:
        mid = (right + left) // 2
        if array[mid] < array[a]:
            right = mid
        else:
            left = mid + 1
    for i in range(a, left, -1):
        array[i], array[i - 1] = array[i - 1], array[i]





def reverse(array, index1, index2):
    while index1 < index2:
        array[index1], array[index2] = array[index2], array[index1]
        index1 += 1
        index2 -= 1




def TimSort(array):
    array_of_runs = []
    minRun = get_minrun(len(array))
    pointer = 0
    pointer = 0

    while pointer < len(array) - 1:
        start_run = pointer
        if array[pointer] < array[pointer + 1]:     #increment subsequence
            if start_run + minRun < len(array):
                for pointer in range(start_run, start_run + minRun - 1):
                    if array[pointer] > array[pointer + 1]:
                        binaryInsertionSort(array, start_run, pointer, pointer + 1)
            else:
                for pointer in range(start_run, len(array) - 1):
                    if array[pointer] > array[pointer + 1]:
                        binaryInsertionSort(array, start_run, pointer, pointer + 1)
            while pointer + 1 < len(array) and array[pointer] <= array[pointer + 1]:
                pointer += 1

        else:                                       #decrement subsequence
            if start_run + minRun < len(array):
                for pointer in range(start_run, start_run + minRun - 1):
                    if array[pointer] < array[pointer + 1]:
                        reversedBinaryInsertionSort(array, start_run, pointer, pointer + 1)
            else:
                for pointer in range(start_run, len(array) - 1):
                    if array[pointer] < array[pointer + 1]:
                        reversedBinaryInsertionSort(array, start_run, pointer, pointer + 1)
            while pointer + 1 < len(array) and array[pointer] >= array[pointer + 1]:
                pointer += 1
            reverse(array, start_run, pointer)
        array_of_runs.append(array[start_run: pointer + 1])

        while len(array_of_runs) > 2:
            x = len(array_of_runs[-3])
            y = len(array_of_runs[-2])
            z = len(array_of_runs[-1])
            if not ((x >= y + z) and (y >= z)):
                Z = array_of_runs.pop()
                Y = array_of_runs.pop()
                X = array_of_runs.pop()
                if len(X) > len(Z):
                    t = merge(Y, Z)
                    array_of_runs.append(t)
                    array_of_runs.append(X)
                else:
                    t = merge(Y, X)
                    array_of_runs.append(t)
                    array_of_runs.append(Z)

            else:
                break
        if len(array_of_runs) == 2 and len(array_of_runs[-1]) > len(array_of_runs[-2]):
            array_of_runs.append(merge(array_of_runs.pop(), array_of_runs.pop()))


        pointer += 1

    while(len(array_of_runs) > 1):
        array_of_runs.append(merge(array_of_runs.pop(), array_of_runs.pop()))
    return array_of_runs[0]






array = [random.randint(-10_000, 10_000) for i in range(100_000)]

start = time.time()
a = TimSort(array)
end = time.time()


print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
