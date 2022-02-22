import random


class Tree:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def insert_value(node, value):
    if node is None:
        return Tree(value)
    if value > node.val:
        node.right = insert_value(node.right, value)
    else:
        node.left = insert_value(node.left, value)
    return node


def tree_sort(data):
    root = Tree(data[0])
    for i in range(1, len(data)):
        insert_value(root, data[i])

    in_order_traversal(root, data, [0])


def in_order_traversal(root, data, index):
    if not root:
        return
    in_order_traversal(root.left, data, index)
    data[index[0]] = root.val
    index[0] += 1
    in_order_traversal(root.right, data, index)

if __name__ == '__main__':
    data = [random.randrange(100) for i in range(20)]
    print(data)
    tree_sort(data)
    print(data)
