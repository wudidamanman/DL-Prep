## this will print a BST in matrix


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PrintTree(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = self.height(root)
        matrix = [['' for n in range((2 ** h) - 1)] for m in range(h)]

        self.place(root, matrix, 0, (2 ** h) - 1, 0)
        for lists in matrix:
            print(lists)
        return matrix

    def height(self, node):
        return max(1 + self.height(node.left), 1 + self.height(node.right)) if node else 0

    def place(self, node, matrix, i, j, row):
        if node:
            col = (i + j) // 2
            matrix[row][col] = str(node.val)
            self.place(node.left, matrix, i, col, row + 1)
            self.place(node.right, matrix, col + 1, j, row + 1)


# from list to tree
from collections import deque


def list2Tree(data):
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            tmp = next(n)
            if tmp is None:
                head.left = None
            else:
                head.left = TreeNode(tmp)
                fringe.append(head.left)
            tmp = next(n)
            if tmp is None:
                head.right = None
            else:
                head.right = TreeNode(tmp)
                fringe.append(head.right)
        except StopIteration:
            break
    return tree


if __name__ == '__main__':
    data = [3, 5, 2, 1, 4, 6, 7, 8, 9, 0, 1, 2, 3, 4]
    data = [5, 1, 4, None, None, 3, 6]
    data = [17, 6, None, 5, 20, 3, 14, 20, 16, 9, 15, 10, 3, 17, None]
    tree = list2Tree(data)

    printT = PrintTree()
    res = printT.printTree(tree)

    # test
    def test(method, random_samples=False):
        # test settings
        times = 10

        sol = method()
        data = [5, 1, 7, None, None, 6, 8]
        # data = [2, 1, 3]
        # data = [3, 1, 5, 0, 2, 4, 6]
        data = [10, 5, 15, None, None, 6, 20]
        from L98_test_case import data

        tree = list2Tree(data)
        printT = PrintTree()
        printT.printTree(tree)

        res = sol.isValidBST(tree)
        print('the tree {} BST '.format(["isn\'t", "is"][res]))

        if random_samples:  # There are other rules constain the data, so it cannot be truly simulate by following code
            import random

            for _ in range(times):
                len1 = random.randint(0, 20)
                data = []
                for __ in range(len1):
                    num1 = random.sample([random.randint(1, 20) for i in range(20)] + [None], 1)
                    data += num1
                print(data)
                tree = list2Tree(data)
                printT = PrintTree()
                printT.printTree(tree)

                res = sol.isValidBST(tree)
                print('the tree {} BST '.format(["isn\'t", "is"][res]))


    test(Solution, True)