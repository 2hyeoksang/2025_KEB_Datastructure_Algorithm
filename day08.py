class Treenode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None



if __name__ == "__main__":
    root = None
    groups = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

    node = Treenode()
    node.data = groups[0]
    root = node

    for group in groups[1:]:
        node = Treenode()
        node.data = group
        current = root

        while True:
            if group < current.data :
                if current.left is None :
                    current.left = node
                    break
                current = current.left

            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right


print("Success")

deleteName = input("name : ")

current = root
parent = None
while True:
    if deleteName == current.data :

        if current.left == None and current.right == None :
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)

        elif current.left != None and current.right == None:
            if parent.left == current :
                parent.left = current.left
            else :
                parent.right = current.left
            del(current)

        elif current.left == None and current.right is not None:
            if parent.left == current:
                parent.left = current.right
            else :

                parent.right = current.right
            del(current)

        print(deleteName, '이(가) 삭제됨.')
        break

    elif deleteName < current.data :
        if current.left is None:
            print(deleteName, '이(가) 트리에 없음')
            break
        parenet = current
        current = current.left

    else :
        if current.right is None:
            print(deleteName, "이(가) 트리에 없음")
            break
        parent = current
        current = current.right

