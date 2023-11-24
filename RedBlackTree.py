from typing import Optional, Type, Any, Union


class StringToTreeInitalizationEror(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'StringToTreeInitalizationError: {self.message}' if self.message else 'StringToTreeInitalizationError'


class NullNode:
    def __init__(self, parent=None):
        self.parent = parent
        self.color = 0


class Node:
    def __init__(self, data: Any, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.data = data
        self.left = left
        self.right = right
        self.left = left if left is not None else NullNode()
        self.right = right if right is not None else NullNode()

    def __str__(self) -> str:
        return str(self.data)


class RBnode(Node):
    def __init__(self, data: Any, color: bool, parent: Optional['RBnode'], left: 'RBnode' = None,
                 right: 'RBnode' = None):
        super().__init__(data, left, right)
        self.parent = parent
        self.color = color
        self.left = left if left is not None else NullNode(self)
        self.right = right if right is not None else NullNode(self)

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root




    def rb_from_binary(self):
        rb_tree = RBTree()
        stack = [self.root]
        while type(stack[0]) != NullNode:
            curr = stack[-1]
            if type(curr) != NullNode:
                stack.append(curr.left)
                continue
            else:
                stack.pop()
                node = stack.pop()
                stack.append(node.right)
                rb_tree.insert(node.data)
        return rb_tree

    def recursion_dfs(self, root):
        if type(root) != NullNode:
            self.recursion_dfs(root.left)
            if self.root == root:
                print(root, 'root')
            else:
                print(root)
            self.recursion_dfs(root.right)

    def bfs(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if type(node.left) != NullNode:
                queue.append(node.left)
            if type(node.right) != NullNode:
                queue.append(node.right)

            print(node)

    def iterative_in_order_dfs(self):
        stack = [self.root]
        while type(stack[0]) != NullNode:
            curr = stack[-1]
            if type(curr) != NullNode:
                stack.append(curr.left)
                continue
            else:
                stack.pop()
                node = stack.pop()
                stack.append(node.right)
                if node == self.root:
                    print(node, "root")
                else:
                    print(node)

    def iterative_pre_order_dfs(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node)
            if type(node.right) != NullNode:
                stack.append(node.right)
            if type(node.left) != NullNode:
                stack.append(node.left)

    def iterative_post_order_dfs(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node)
            if type(node.left) != NullNode:
                stack.append(node.left)
            if type(node.right) != NullNode:
                stack.append(node.right)

    # def dfs(self, root):
    #     if type(root) != NullNode:
    #         self.dfs(root.left)
    #         if self.root == root:
    #             print(root, 'root', root.color)
    #         else:
    #             print(root, root.color)
    #
    #         self.dfs(root.right)

    def prnt(self, traversal="iterative_in_order_dfs"):
        getattr(self, traversal)()


    # def dfs(self, root):
    #     if root:
    #         self.dfs(root.left)
    #         print(root)
    #         self.dfs(root.right)


def left_rotation(node: RBnode):
    branch_ancestor = node.parent.parent
    to_right = None
    root = None
    if branch_ancestor is not None:
        root = branch_ancestor
        if branch_ancestor.right == node.parent:
            to_right = True
        else:
            to_right = False
    branch_ancestor = node.parent.parent
    node.parent.parent = node
    node.parent.right = node.left
    node.left.parent = node.parent
    node.left = node.parent
    node.parent = branch_ancestor
    if to_right is not None:
        if to_right:
            branch_ancestor.right = node
        else:
            branch_ancestor.left = node
    if root:
        return root  # так как он станет в верху остальных нод
    return node


def right_rotation(node: RBnode):
    branch_ancestor = node.parent.parent
    to_right = None
    root = None
    if branch_ancestor is not None:
        root = branch_ancestor
        if branch_ancestor.right == node.parent:
            to_right = True
        else:
            to_right = False
    node.parent.parent = node
    node.right.parent = node.parent
    node.parent.left = node.right
    node.right = node.parent
    node.parent = branch_ancestor
    if to_right is not None:
        if to_right:
            branch_ancestor.right = node
        else:
            branch_ancestor.left = node
    if root:
        return root  # так как он станет в верху остальных нод
    return node


class RBTree(BinaryTree):
    def __init__(self, root: Optional[RBnode] = None):
        super().__init__(root)

    def fix_root(self, new_root: RBnode) -> None:
        if self.root.parent is not None:
            self.root = new_root
            self.root.color = 0

    # функция для перекрашивания в случае с красным дядей
    def red_uncle(self, gparent: RBnode, parent: RBnode, uncle: RBnode) -> None:
        parent.color = 0
        uncle.color = 0
        if gparent != self.root:
            gparent.color = 1
            self.fix_tree(gparent)
        else:
            gparent.color = 0

    # функция перекрашивания в случае с черным дядей
    def black_uncle(self, parent: RBnode, gparent: RBnode) -> None:
        parent.color = 0
        gparent.color = 1

    def fix_tree(self, node: Union[RBnode, NullNode]) -> None:
        parent = node.parent
        if parent.color == 1:
            gparent = node.parent.parent
            if gparent.left == parent:
                uncle = gparent.right
                if parent.left == node:
                    if uncle.color == 1:
                        self.red_uncle(gparent, parent, uncle)
                        return
                    if uncle.color == 0:
                        self.fix_root(right_rotation(parent))
                        self.black_uncle(parent, gparent)
                        return
                else:
                    if uncle.color == 0:
                        self.fix_root(left_rotation(node))
                        self.fix_root(right_rotation(node))
                        self.black_uncle(node, gparent)
                        return
                    if uncle.color == 1:
                        self.red_uncle(gparent, parent, uncle)
                        return
            else:
                uncle = gparent.left
                if parent.right == node:
                    if uncle.color == 1:
                        self.red_uncle(gparent, parent, uncle)
                        return

                    else:
                        self.fix_root(left_rotation(parent))
                        self.black_uncle(parent, gparent)
                        return
                else:
                    if uncle.color == 0:
                        self.fix_root(right_rotation(node))
                        self.fix_root(left_rotation(node))
                        self.black_uncle(node, gparent)
                        return
                    if uncle.color == 1:
                        self.red_uncle(gparent, parent, uncle)
                        return
        else:
            return

    def find(self, data: int) -> Optional[RBnode]:
        curr_node = self.root
        while type(curr_node) is not NullNode:
            if curr_node.data > data:
                curr_node = curr_node.left
            elif curr_node.data < data:
                curr_node = curr_node.right
            else:
                return curr_node
        return None  # вообще тут можно вызывать ошибку сразу, но наверное лучше вернуть None



    def fix_delete(self, node: RBnode, from_right: bool):
        # в данном случае node - это родитель поддерева, у которого уменьшилась черная высота
        right_son = node.right
        left_son = node.left
        if from_right:  # это значит, что высота уменьшилась у правого относительно этого узла поддерева
            right_gson = left_son.right
            left_gson = left_son.left
            if node.color == 1:
                if left_son.color == 0:
                    if left_gson.color == 0 and right_gson.color == 0:
                        node.color = 0
                        left_son.color = 1
                    elif left_gson.color == 1:
                        left_son.color = 1
                        node.color = 0
                        left_gson.color = 0
                        self.fix_root(right_rotation(left_son))
                    elif right_gson.color == 1:
                        left_son.color = 1
                        left_rotation(right_gson)
                        right_gson.color = 0
            else:
                if left_son.color == 1:
                    self.fix_root(right_rotation(left_son))
                    left_son.color = 0
                    node.color = 1
                    self.fix_delete(node, False)
                else:
                    if left_gson.color == 1:
                        left_son.color = 0
                        node.color = 1
                        left_gson.color = 0
                        self.fix_root(right_rotation(left_son))
                    elif right_gson.color == 1:
                        left_son.color = 1
                        left_rotation(right_gson)
                        right_gson.color = 0
                    elif right_gson.color == 0 and left_gson.color == 0:
                        if node.parent.right == node:
                            self.fix_delete(node.parent, True)
                        else:
                            self.fix_delete(node.parent, False)
        else:
            right_gson = right_son.right
            left_gson = right_son.left
            if node.color == 1:
                if right_son.color == 0:
                    if right_gson.color == 0 and left_gson.color == 0:
                        node.color = 0
                        right_son.color = 1
                    elif right_gson.color == 1:
                        right_son.color = 1
                        node.color = 0
                        right_gson.color = 0
                        self.fix_root(left_rotation(right_son))
                    elif left_gson.color == 1:
                        right_son.color = 1
                        right_rotation(left_gson)
                        left_gson.color = 0
            else:
                if right_son.color == 1:
                    self.fix_root(left_rotation(right_son))
                    right_son.color = 0
                    node.color = 1
                    self.fix_delete(node, False)
                else:
                    if right_gson.color == 1:
                        right_son.color = 0
                        node.color = 1
                        right_gson.color = 0
                        self.fix_root(left_rotation(right_son))
                    elif left_gson.color == 1:
                        right_son.color = 1
                        right_rotation(left_gson)
                        left_gson.color = 0
                    elif left_gson.color == 0 and right_gson.color == 0:
                        if node.parent.right == node:
                            self.fix_delete(node.parent, True)
                        else:
                            self.fix_delete(node.parent, False)


    def replace_and_change_color(self, node, is_right: bool):
        if is_right:
            new_node = node.right
        else:
            new_node = node.left
        parent = node.parent
        if node == self.root:
            self.root = node
            node.parent = None
            return
        if parent.right == node:  # является правым потомком
            new_node.parent = parent
            parent.right = new_node  # перевязываем поддерево
        else:  # является левым потомком
            new_node.parent = parent
            parent.left = new_node
        # так как поддерево, которое является потомком узла только с одним потомком
        # может быть только поддеревом с красным узлом - то для баланса нужно перекрасить его в черный
        new_node.color = 0

    def find_node_for_replace(self, node):
        cur_node = node.left
        prev = None
        while type(cur_node) is not NullNode:
            prev = cur_node
            cur_node = cur_node.right
        return prev

    def del_node(self, data: int):
        node = self.find(data)
        self.delete(node)

    def delete(self, node: RBnode) -> None:
        if type(node.right) is NullNode or type(node.left) is NullNode:
            if type(node.right) is NullNode and type(node.left) is NullNode:  # если у

                if node == self.root:
                    self.root = None
                    return

                is_right = None
                if node.parent.right == node:
                    node.parent.right = NullNode(node.parent)
                    is_right = True
                else:
                    node.parent.left = NullNode(node.parent)
                    is_right = False

                if node.color == 1:
                    return
                self.fix_delete(node.parent, is_right)
                return
            if type(node.right) is not NullNode:
                self.replace_and_change_color(node, True)
                return
            self.replace_and_change_color(node, False)
            return
        else:
            n = self.find_node_for_replace(node)
            node.data = n.data
            self.delete(n)
            return

            # после удаления высота отдного из поддеревьев родительского узла будет нарушена
            # нужно вернуть баланс

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = RBnode(data, 0, None)
            return ...
        root = self.root
        parent = root
        new_node = RBnode(data, 1, None)
        while type(root) is not NullNode:
            if root.data <= data:
                if type(root.right) is NullNode:
                    parent = root
                    root.right = new_node
                    new_node.parent = parent
                    break
                else:
                    parent = root
                    root = root.right
            else:
                if type(root.left) is NullNode:
                    parent = root
                    root.left = new_node
                    new_node.parent = parent
                    break
                else:
                    parent = root
                    root = root.left
        self.fix_tree(new_node)

def parse_to_tree(string: Optional[str] = None, file: str = None) -> BinaryTree:
    if file:
        with open(file, 'r') as file:
            data = file.read()
        string = data
    parse_stack = []
    buffer = ''
    good_symbols = ('(', ' ', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    root = None
    for i in string:
        if i not in good_symbols:
            raise StringToTreeInitalizationEror

        if i == '(':
            parse_stack.append(i)

        elif i.isdigit():
            buffer += i

        elif i == ' ' and buffer:
            parse_stack.append(Node(int(buffer)))
            buffer = ''

        elif i == ')':
            if buffer:
                parse_stack.append(Node(int(buffer)))
                buffer = ''

            sons = []
            while parse_stack and parse_stack[-1] != '(':
                sons.append(parse_stack.pop())

            parse_stack.pop()

            if parse_stack:
                if len(sons) == 1:
                    node = sons[0]
                    if type(parse_stack[-1].left) == NullNode:
                        node.prev = parse_stack[-1]
                        parse_stack[-1].left = node
                    else:
                        parse_stack[-1].right = node
                else:
                    raise StringToTreeInitalizationEror

            else:
                root = sons[0]

    if parse_stack:
        raise StringToTreeInitalizationEror

    return BinaryTree(root)


# node_1 = RBnode(1, True, None)
# node_2 = RBnode(2, True, node_1, None, None)
# node_3 = RBnode(3, True, node_2, None, None)
#
# tree = RBTree()
# tree.insert(2)
# tree.insert(32)
# tree.insert(23)
# tree.insert(21)
# tree.insert(22)
# tree.insert(9)
# tree.insert(1)
# tree.insert(36)
# tree.insert(38)
# tree.insert(35)
# tree.insert(34)
# tree.insert(40)
# tree.insert(37)
# tree.insert(41)
#
#
# tree.prnt(traversal='iterative_in_order_dfs')


# input_string = "(1 (2 (3)) (4 (5)))"
# tree = get_tree_from_file('example.txt')
tree = parse_to_tree(string="(1 (2 (3 (4 (5 (6))))))")
tree.prnt()
print()
rb_tree = tree.rb_from_binary()
rb_tree.prnt()


# a = RBnode(3, 'Red', None)
