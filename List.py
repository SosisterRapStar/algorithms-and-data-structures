from typing import Optional


class ArrayListIterator:
    def __init__(self, list_obj):
        self.counter = 0
        self.lst = list_obj

    def __next__(self):
        if self.counter >= self.lst.size:
            raise StopIteration
        el = self.lst[self.counter]
        self.counter += 1
        return el


class ArrayListException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'ArrayListError: {self.message}' if self.message else 'ArrayListError'


class ArrayListIndexOutOfRange(ArrayListException):
    pass


class ArrayList:
    sort_key = 0
    SIZE_MULTIPLIER = 2
    INITIAL_SIZE = 10
    SHRINK_COEFFICIENT = 0.25

    @classmethod
    def set_sort_key(cls, key: int):
        cls.sort_key = key

    @classmethod
    def sort(cls, array: 'ArrayList', key: int = None):
        if key is None:
            new_arr = TimSort(array)
            return new_arr
        else:
            cls.set_sort_key(key)
            new_arr = TimSort(array)
            cls.set_sort_key(0)
            return new_arr

    def __lt__(self, other):
        return self[self.sort_key] < other[self.sort_key]

    def __gt__(self, other):
        return self[self.sort_key] > other[self.sort_key]

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __le__(self, other):
        return self[self.sort_key] <= other[self.sort_key]

    def __ge__(self, other):
        return self[self.sort_key] >= other[self.sort_key]

    def __init__(self, *args, **kwargs):

        self.array = [0 for g in range(self.INITIAL_SIZE)]
        self.size = 0
        self.capacity = 10
        if args:
            for i in args:
                if type(i) == list:
                    for g in i:
                        self.push_back(g)
                else:
                    self.push_back(i)

    def rebuild_array(self):
        self.capacity *= 2
        new_arr = [0 for g in range(self.capacity)]
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr

    def push_back(self, element):
        if self.size + 1 == self.capacity:
            self.rebuild_array()
        self.size += 1
        self.array[self.size - 1] = element

    def pop(self):
        el = self.array[self.size - 1]
        self.array[self.size - 1] = 0
        self.size -= 1
        if self.size / self.capacity < self.SHRINK_COEFFICIENT:
            self.shrink()
        return el

    def slice(self, start, end):
        if start > end or start < 0 or end < 0:
            return ArrayList()
        if end > self.size:
            end = self.size
        new_arr = ArrayList()
        for i in range(start, end):
            new_arr.push_back(self.array[i])
        return new_arr

    def shrink(self):
        self.capacity //= self.SIZE_MULTIPLIER
        new_arr = [0 for i in range(self.capacity)]
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0:
            opposite_index = self.size + index
            if opposite_index < 0:
                raise ArrayListIndexOutOfRange("Too big negative value")
            return self.array[opposite_index]
        if index >= self.size:
            raise ArrayListIndexOutOfRange("Too big value")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise ArrayListIndexOutOfRange("Ok")
        self.array[index] = value

    def __str__(self):
        if self.size == 0:
            return '[]'
        string = '[ '
        for i in range(self.size - 1):
            string += str(self.array[i]) + ', '
        string += str(self.array[self.size - 1])
        string += ' ]'
        return string

    def __iadd__(self, other):
        for i in range(len(other)):
            self.push_back(other[i])
        return self

    def __add__(self, other):
        new_arr = ArrayList()
        for i in self:
            new_arr.push_back(i)

        for i in range(len(other)):
            new_arr.push_back(other[i])
        return new_arr

    def __iter__(self):
        return ArrayListIterator(self)


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
    array_of_runs = ArrayList()
    minRun = get_minrun(len(array))
    pointer = 0
    pointer = 0

    while pointer < len(array) - 1:
        start_run = pointer
        if array[pointer] < array[pointer + 1]:  # increment subsequence
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

        else:  # decrement subsequence
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
        array_of_runs.push_back(array.slice(start_run, pointer + 1))

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
                    array_of_runs.push_back(t)
                    array_of_runs.push_back(X)
                else:
                    t = merge(Y, X)
                    array_of_runs.push_back(t)
                    array_of_runs.push_back(Z)

            else:
                break
        if len(array_of_runs) == 2 and len(array_of_runs[-1]) > len(array_of_runs[-2]):
            array_of_runs.push_back(merge(array_of_runs.pop(), array_of_runs.pop()))

        pointer += 1

    while (len(array_of_runs) > 1):
        array_of_runs.push_back(merge(array_of_runs.pop(), array_of_runs.pop()))
    return array_of_runs[0]




