from typing import Optional, Type, Any


class StringToTreeInitalizationEror(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'StringToTreeInitalizationError: {self.message}' if self.message else 'StringToTreeInitalizationError'


class Node:
    def __init__(self, data: Any, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.data = data
        self.left = left
        self.right = right

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


class NullNode:
    def __init__(self, parent):
        self.parent = parent
        self.color = 0


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def prnt(self):
        self.dfs(self.root)

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
        return root # так как он станет в верху остальных нод
    return node

class RBTree(BinaryTree):
    def __init__(self, root: Optional[RBnode] = None):
        super().__init__(root)

    def dfs(self, root):
        if type(root) != NullNode:
            self.dfs(root.left)
            if self.root == root:
                print(root, 'root', root.color)
            else:
                print(root, root.color)

            self.dfs(root.right)

    def red_uncle_fix(self, node, paren):
        pass

    def fix_root(self, new_root):
        if self.root.parent is not None:
            self.root = new_root


    def fix_tree(self, node):
        parent = node.parent
        if parent.color == 1:
            gparent = node.parent.parent
            if gparent.left == parent:
                uncle = gparent.right
                if parent.left == node:
                    if uncle.color == 1:
                        parent.color = 0
                        uncle.color = 0
                        if gparent != self.root:
                            gparent.color = 1
                            self.fix_tree(gparent)
                        else:
                            gparent.color = 0
                        return ...
                        # нам нужно проходится вверх от деда, так как в таком случае дед становится красным
                        # это может нарушить прошлое построение дерева
                    # в этом случае нам не нужно ничего менять за дедом, так как узел, который встал на место деда - черный
                    if uncle.color == 0:
                        self.fix_root(right_rotation(parent)) # убрать root
                        parent.color = 0
                        gparent.color = 1
                        return ...
                # в данном случае тоже ничего не надо менять за дедом,
                # так как узел который встал на место деда так и остался черным
                else:

                    if uncle.color == 0:
                        self.fix_root(left_rotation(node))
                        self.fix_root(right_rotation(node))
                        node.color = 0
                        gparent.color = 1
                        return ...
                    if uncle.color == 1:
                        parent.color = 0
                        uncle.color = 0
                        if gparent != self.root:
                            gparent.color = 1
                            self.fix_tree(gparent)
                        else:
                            gparent.color = 0
                        return ...



                        # тут нужно перекрасить деда в красный
                        # добавить проверку на root
                        # ...
            else:
                uncle = gparent.left
                if parent.right == node:
                    if uncle.color == 1:
                        parent.color = 0
                        uncle.color = 0
                        if gparent != self.root:
                            gparent.color = 1
                            self.fix_tree(gparent)
                        else:
                            gparent.color = 0

                        return ...
                        # нам нужно проходится вверх от деда, так как в таком случае дед становится красным
                        # это может нарушить прошлое построение дерева
                    else:
                        self.fix_root(left_rotation(parent)) # убрать self.root
                        parent.color = 0
                        gparent.color = 1
                        return ...
                else:
                    if uncle.color == 0:
                        self.fix_root(right_rotation(node)) # убрать root
                        self.fix_root(left_rotation(node)) # убрать root
                        node.color = 0
                        gparent.color = 1
                        return ...
                    if uncle.color == 1:
                        uncle.color = 0
                        parent.color = 0
                        if gparent != self.root:
                            gparent.color = 1
                            self.fix_tree(gparent)
                        else:
                            gparent.color = 0

                        return ...
                        # тут нужно перекрасить деда в красный, но нужна проверка на root
                        # ...
        else:
            return ...

    def insert(self, data: int):
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


def get_tree_from_file(name: str) -> BinaryTree:
    with open(name, 'r') as file:
        data = file.read()
    return parse_to_tree(data)


def parse_to_tree(string: str) -> BinaryTree:
    parse_stack = []
    buffer = ''
    good_symbols = ('(', ' ', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
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
                    if not parse_stack[-1].left:
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


node_1 = RBnode(1, True, None)
node_2 = RBnode(2, True, node_1, None, None)
node_3 = RBnode(3, True, node_2, None, None)

tree = RBTree()

tree.prnt()

#
# input_string = "(1 (2 (3)) (4 (5)))"
# tree = get_tree_from_file('example.txt')
# tree.prnt()

# a = RBnode(3, 'Red', None)
