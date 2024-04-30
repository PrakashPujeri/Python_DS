class STACK :
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def size(self):
        return len(self.items)
ST=STACK()
ST.push(12)
ST.push(23)
ST.push(76)
ST.pop()
ST.size()

ST.peek()
print(ST.pop())
print(ST.pop())
print(ST.peek())