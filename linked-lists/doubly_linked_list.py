class Node:
    # If data is not given by user, it’s taken as None
    def __init__(self, data=None, next=None, prev=None):
        self.data = data 
        self.next = next
        self.prev = prev

    #method for setting the data field of the node 
    def setData(self, data):
        self.data = data

    #method for getting the data field of the node 
    def getData(self):
        return self.data

    #method for setting the next field of the node 
    def setNext(self, next):
        self.next = next

    #method for getting the next field of the node 
    def getNext(self):
        return self.next

    #returns true if the node points to another node 
    def hasNext(self):
        return self.next != None

    #method for setting the next field of the node 
    def setPrev(self, prev):
        self.prev = prev

    #method for getting the next field of the node
    def getPrev(self):
        return self.prev

    #returns true if the node points to another node 
    def hasPrev(self):
        return self.prev != None

    # __str__ returns string equivalent of Object 
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)

class DoublyLinkedList(object):
    def insertAtBeginning(self, data):
        newNode = Node(data, None, None) 
        if (self.head == None):
            self.head = self.tail = newNode 
        else:
            newNode.prev = None 
            newNode.next = self.head 
            self.head.prev = newNode 
            self.head = newNode

       
    def insertAtEnd(self, data):
        if (self.head == None): # To imply that if head == None
            self.head = Node(data) 
        else:
            current = self.head
        while(current.next != None): 
            current = current.next
        newNode = Node(data)
        newNode.prev = current
        newNode.next = None # default, no need to update

    def getNode(self, index): 
        currentNode = self.head
        if currentNode == None: 
            return None
        i=0
        while i < index and currentNode.next is not None:
            currentNode = currentNode.next 
            if currentNode == None:
                break 
            i += 1
        return currentNode

    def insertAtGivenPosition(self, index, data): 
        newNode = Node(data)
        if self.head == None or index == 0: 
            self.insertAtBeginning(data)
        elif index > 0:
            temp = self.getNode(index)
        if temp == None or temp.next == None: 
            self.insertAtEnd(data)
        else:
            newNode = temp.next
            newNode.prev = temp 
            temp.next.prev = newNode 
            temp = newNode

