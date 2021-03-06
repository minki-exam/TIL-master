import sys
sys.stdin = open('input.txt', 'r')


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BS():
    def __init__(self):
        self.root = None


    def insert(self, data):
        n = Node(data)
        if self.root is None:
            self.root = n
            print(self.root)

            return
        else:
            current = self.root # left, right


            while 1:
                parent = current
                if current.left == None:
                    current = current.left
                    if current is None:
                        parent.left = n
                        break

                else:
                    current = current.right
                    if current is None:
                        parent.right = n
                        break






    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root:
                # print(root.left)
                # print(root.right)
                _in_order_traversal(root.left)
                print(root.data, end = '')
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)

    def inorder_traverse(self):
        def inorder_traverse(root):
            # if root is None:
            #     return
            # else:
            inorder_traverse(root.left)
            print(root.data, end = '')
            inorder_traverse(root.right)
        inorder_traverse(self.root)


for tc in range(1, 11):
    N = int(input())
    ls = [list(map(str, input().split())) for _ in range(N)]
    print(ls)
    sample = BS()
    for x in ls:
        print(x[1] ,end = '')
        sample.insert(x[1])
    # print(sample.root)
    print()

    print(sample.in_order_traversal())
    print()
    # print(sample.inorder_traverse())













# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None
# class tree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         self.root = self.insert_value(self.root, data)
#         return self.root is not None
#
#     def insert_value(self, node, data):
#         if node is None:
#             node = Node(data)
#         else:
#             if data <= node.data:
#                 node.left = self.insert_value(node.left, data)
#             else:
#                 node.right = self.insert_value(node.right, data)
#         return node





# def inorder_traverse(node):
#     if node == None:
#         return
#     inorder_traverse(node.left)
#     print(node.data, end = ' ')
#     inorder_traverse(node.right)

    # def insert(self, data):
    #     self.root = self._insert_value(self.root, data)
    #     # return self.root is not None
    # def _insert_value(self, node, data):
    #     if node is None:
    #         node = Node(data)
    #     else:
    #         if node.left is None:
    #             node.left = self._insert_value(node.left, data)
    #         elif node.right is None:
    #             node.right = self._insert_value(node.right, data)
    #     return node


