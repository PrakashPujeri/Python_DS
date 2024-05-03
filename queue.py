class QUEUE:
    def __init__(self):
        self.items=[]

    def is_empty( self):
         return len(self.items)==0
            
    def enqueue(self,item):
       self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
           print("print is empty")
    def  display(self):
        if not  self.is_empty():
             for item in self.items:
                print(item)
        else:
            print("queue is empty")
           
q=QUEUE()
q.enqueue(10)
q.enqueue(98)
q.enqueue(54)
q.enqueue(6)
q.display()
print("pop items")
q.dequeue()
q.display()