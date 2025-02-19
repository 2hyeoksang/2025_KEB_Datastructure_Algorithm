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

find_group = input("name: ")
current =root
while True :
    if find_group == current.data :
        print(f'{find_group}을 찾았습니다.')
        break
    elif find_group < current.data:
        if current.left is None:
            print(f'{find_group}이 존재하지 않습니다.')
            break
        current = current.left
    else:
        if current.right is None:
            print(f'{find_group}이 존재하지 않습니다.')
            break
        current = current.right


