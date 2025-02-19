def pre_order(node):
    if node is None:
        return
    print(node.data,end = '-')
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end = '-')


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data,end = '-')
    in_order(node.right)


class Treenode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

node1 = Treenode()
node1.data = '화사'

node2 = Treenode()
node2.data = '솔라'
node1.left = node2

node3 = Treenode()
node3.data = '문별'
node1.right = node3

node4 = Treenode()
node4.data = '휘인'
node2.left = node4

node5 = Treenode()
node5.data = '쯔위'
node2.right = node5

node6 = Treenode()
node6.data = '선미'
node3.left = node6

post_order(node1)
print()
pre_order(node1)
print()
in_order(node1)