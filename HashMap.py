from typing import Any, Optional
# добавить RedBlck и Treefy
# закрыть некоторые методы

class HashMapException(Exception):
    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return f' HashMapException: {self.message}' if self.message is not None else 'HashMapException'


class Node:
    def __init__(self, hash, key: Any, value: Any):
        self.hash = hash
        self.key = key
        self.value = value
        self.next = None


class Bucket:

    def __init__(self, data: Optional[Node] = None):
        self.size = 0
        self.node = data

    def add(self, data: Node):
        if self.node is None:
            self.size += 1
            self.node = data
            return 1
        else:
            curr_node = self.node
            while curr_node.next:
                if curr_node.hash != data.hash:
                    curr_node = curr_node.next
                else:
                    curr_node.value = data.value
                    return 0
            if curr_node.hash != data.hash:
                self.size += 1
                curr_node.next = data
                return 1
            else:
                curr_node.value = data.value
                return 0




    def get_from_node(self, key):
        curr_node = self.node
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return None

    def set(self, key, value):
        curr_node = self.node
        while curr_node:
            if curr_node.key == key:
                curr_node.value = value
                return curr_node.value
            curr_node = curr_node.next
        return None



    def delete(self, key_hash):
        if self.node.hash == key_hash:
            self.node = self.node.next
            self.size -= 1
            return ...

        curr_node = self.node
        prev_node = curr_node
        while curr_node and curr_node.hash != key_hash:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node:
            prev_node.next = curr_node.next
            self.size -= 1
        else:
            raise HashMapException


    def string(self):
        st = ""
        curr_node = self.node
        while curr_node:
            st += f' {curr_node.key}: {curr_node.value} '
            curr_node = curr_node.next
        return st

    def pop(self) -> Node | None:
        data = self.node
        if self.node:
            self.node = self.node.next
        return data





class HashMap:
    LOAD_FACTOR = 0.75
    SIZE_MULTIPLIER = 2
    START_SIZE = 16

    def __init__(self):
        self.size = 0
        self.array = [Bucket() for i in range(self.START_SIZE)]


    def __len__(self):
        return self.size

    def __rebuild(self):
        new_arr = [Bucket() for i in range(len(self.array) * self.SIZE_MULTIPLIER)]
        prev_arr = self.array
        self.array = new_arr
        for bucket in prev_arr:
            while node := bucket.pop():
                index = node.hash % len(self.array)
                self.array[index].add(node)




    def put(self, key: Any, value: Any):
        key_hash = key.__hash__()
        index = key_hash % len(self.array)
        self.size += self.array[index].add(Node(key_hash, key, value))
        if self.size > int(len(self.array) * self.LOAD_FACTOR):
            self.__rebuild()


    def __getitem__(self, key: Any)->Any:
        key_hash = key.__hash__()
        index = key_hash % len(self.array)
        el = self.array[index]
        val = el.get_from_node(key)
        if val is not None:
            return val
        else:
            raise HashMapException()

    def __setitem__(self, key, value):
        # тут вообще можно всегда использовать put, но в этой реализации не создается лишний Node
        key_hash = key.__hash__()
        index = key_hash % len(self.array)
        el = self.array[index]
        val = el.set(key, value)
        if val is None:
            self.put(key, value)


    def set(self, key:Any):
        key_hash = key.__hash__()
        index = key_hash % len(self.array)
        el = self.array[index]



    def delete(self, key):
        key_hash = key.__hash__()
        index = key_hash % len(self.array)
        el = self.array[index]
        el.delete(key_hash)
        self.size -= 1

    def __str__(self):
        s = '{'
        for i in self.array:
            s += i.string()
        s += '}'
        return s






