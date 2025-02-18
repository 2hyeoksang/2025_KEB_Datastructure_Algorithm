import random

class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next :
            current = current.next
        current.next = Node(data)


    def search(self,target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False


    def remove(self,target):
        if self.head.data == target:
            self.head = self.head.next
            print('선두노드 삭제')
            return
        current = self.head
        previous = None
        while current :
            if current.data == target :
                previous.next = current.next
            previous = current  #MOVE
            current = current.next


    def __str__(self):
        node = self.head
        while node is not None :
            print(node.data)
            node = node.next
        return "end"


if __name__ == "__main__":
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)
    print(l)

    l.remove(-11)
    print(l)

    # l = LinkedList()
    # i = 0
    # while i < 20:
    #     n = random.randint(1,20)
    #     l.append(n)
    #     print(n,end = ' ')
    #     i += 1
    #
    # #print(l)
    # print(l.search(10))