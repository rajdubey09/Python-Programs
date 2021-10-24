#Queue Implementation

class queue:
    def __init__(self):
        self.queue = []

    #Adding an element
    def enqueue(self,item):
        print("Inserting an Elemant into the Queue",item)
        self.queue.append(item)

    #Removing an element
    def dequeue(self):
        print("Deleting an Element from the Queue",self.queue[0])
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    #Display the Queue
    def display(self):
        print("Displaying the Queue")
        print(self.queue)


q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
