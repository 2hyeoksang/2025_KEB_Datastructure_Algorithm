arr1 = []

def push(num):
    arr1.append(num)


def size(arr1):
    return len(arr1)


def pop(arr1):
    if size(arr1):
        return arr1.pop(0)
    else:
        return -1


def is_empty(arr1):
    if size(arr1):
        return 0
    else:
        return 1


def front(arr1):
    if size(arr1):
        return arr1[0]
    else:
        return -1


def back(arr1):
    if size(arr1):
        return arr1[-1]
    else:
        return -1


N = int(input())
command = [input() for _ in range(N)]
for cmd in command :
    if ' ' in cmd:
        f, num = cmd.split()
        num = int(num)
        if f == "push":
            push(num)

    else:
        if cmd == "front":
            print(front(arr1))
        elif cmd == "back":
            print(back(arr1))
        elif cmd == "pop":
            print(pop(arr1))
        elif cmd == "size":
            print(size(arr1))
        elif cmd == "empty":
            print(is_empty(arr1))