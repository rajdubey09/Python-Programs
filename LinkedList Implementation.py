#Linked List Implementation

class CreateNode:
    def __init__(self,data):
        self.data = data
        self.ref = None
        #print("Node Value Type",type(self.data))
        #print("Node "+self.data+" inserted")

class AddNodeToLinkedList:
    def __init__(self):
        self.head = None

    def TraverseLinkedList(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            h = self.head
            while h is not None:
                print(h.data)
                h = h.ref
                
    def addAtBegin(self,data):
        newNode = CreateNode(data)
        newNode.ref = self.head
        self.head = newNode
        
#Node = CreateNode(9)
#print(CreateNode)
addNode = AddNodeToLinkedList()
addNode.addAtBegin(1)
addNode.addAtBegin(2)
addNode.addAtBegin(3)
addNode.TraverseLinkedList()
