class Stack:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


    def is_empty(self):
        return len(self.items) == 0




s1 = Stack()
s1.push(-9)
s1.push(11)
s1.push(977)

print(s1.peek())
print(s1.pop())
print(s1.peek())
print(s1.is_empty())
s1.pop()
s1.pop()
print(s1.is_empty())
