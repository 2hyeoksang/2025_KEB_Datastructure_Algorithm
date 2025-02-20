class Treenode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def insert_tree(root, grp):   #재귀로 만들 수 있음

    for ele in grp[1:]:
        node = Treenode()
        node.data = ele
        current = root

        while True:
            if node.data < current.data :
                if current.left is None :
                    current.left = node
                    break
                current = current.left
            else : # node.data >= current.data
                if current.right is None:
                    current.right = node
                    break
                current = current.right

    print("Insert Complete")


def pre_order(node):
    if node is None:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


def search_tree(find):
    global root

    current = root
    while True :
        if find == current.data:
            return True

        elif find < current.data:
            if current.left is None:
                return False
            current = current.left

        else :
            if current.right is None:
                return False
            current = current.right


def del_tree(num):
    global root

    current = root
    parent = None

    while True:
        if current.data == num:
            if current.left is None and current.right is None:
                if parent.left == current :
                    parent.left = None
                else:
                    parent.right = None
                del(current)

            elif current.left is not None and current.right is None:
                if  parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                del(current)

            elif current.left is None and current.right is not None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                del(current)

            else:   #current.left & right NOT None
                if parent.left == current:
                    parent.left = min_val(current)
                else:
                    parent.right = min_val(current)
            break

        elif num < current.data :
            parent = current
            current = current.left

        else :
            parent = current
            current = current.right


def min_val(node):
    if node.left.data < node.right.data:
        return node.left
    return node.right


if __name__ == "__main__":
    node = Treenode()
    groups = [10, 8, 5, 12, 20, 11, 3]
    node.data = groups[0]
    root = node
    insert_tree(root, groups)

    while True:
        mode = int(input("(1) 탐색\t(2) 삭제\t(3) 트리 확인\t(4) 종료: "))
        if mode == 4:
            print('프로그램 실행 종료')
            break

        elif mode == 1:
            find_name = int(input("탐색할 수를 입력하시오."))
            t1 = search_tree((find_name))
            if t1 :
                print(f'{find_name}이(가) 존재합니다.')
            else :
                print(f'{find_name}이(가) 존재하지 않습니다.')

        elif mode == 2:
            del_name = int(input("삭제할 수를 입력하시오"))
            t2 = search_tree(del_name)
            if not t2 :
                print(f'{del_name}은 존재하지 않습니다.')
            else:
                del_tree(del_name)
                print(f"{del_name}이 삭제되었습니다.")

        elif mode == 3:
            pre_order(root)