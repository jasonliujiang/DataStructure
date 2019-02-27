"""
二叉树的简单实现
"""


class Node:
    # python 的构造方法
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class TwoTree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)

        if self.root is Node:
            self.root = node
        else:
            q = [self.root]

        print('y', self.root)
        while True:
            print('x', q)
            pop_node = q.pop(0)
            if pop_node.left is None:
                pop_node.left = node
                return
            elif pop_node.right is Node:
                pop_node.right = node
            else:
                q.append(pop_node.left, pop_node.right)

    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]

        while q:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)

        return res

    def preorder(self, root):  # 先序遍历
        if root is None:
            return []

        result = [root.item]
        left = self.preorder(root.left)
        right = self.preorder(root.right)

        return result + left + right

    def inorder(self, root):  # 中序序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.child1)
        right_item = self.inorder(root.child2)
        return left_item + result + right_item

    def postorder(self, root):  # 后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.child1)
        right_item = self.postorder(root.child2)
        return left_item + right_item + result
