# SLists
class Node:                  # blueprint for node objects
    def __init__(self, value):
        self.value = value
        self.next = None # every object will have created var called next

class SList:                 # blueprint for creating new instances of Node object with parent attributes
    def __init__(self, value):
        node = Node(value)   # node var invokes Node class, creating first Node object
        self.head = node     # an attribute newly created, called head, will become the reference to where in memory the node object is located

    def addNode(self, value): # called for the purpose of creating a new object in the same list
        new_node = Node(value)    # create new node object in list that will inherit value, next and a new attr called head that will reference the newly node object created
        runner = self.head    # runner is necessary
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node

    def removeNode(self, value):
        runner = self.head
        if(runner.value == value):
            self.head = runner.next
        prev = runner
        while(runner.next != None):
            if(runner.value == value):
                prev.next = runner.next
                break
            prev = runner
            runner = runner.next
        if(runner.next == None):
            prev.next = None

    def insertNode(self, value, index):
        new_node = Node(value)
        runner = self.head
        prev = runner
        counter = 1
        while(runner.next != None):
            if(index == 1):
                new_node.next = self.head
                self.head = new_node
                break
            elif(index == counter):
                prev.next = new_node
                new_node.next = runner
                break
            prev = runner
            runner = runner.next
            counter += 1
        if(runner.next == None):
            runner.next = new_node
            runner = new_node
            return

    def printValues(self):
        runner = self.head
        print("--- Printing values in the list ---")
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)

list = SList(5)              # creating first instance of node object that will inherite from Node class: value, value entered in SList class will also be inserted into Node class when called in this line of code. Next none will make sure there is no node object inserted in list after it
list.addNode(4)
list.addNode(7)
list.addNode(8)

list.printValues()

#list.removeNode(5)
#list.removeNode(4)
#list.removeNode(7)
#list.removeNode(8)
#list.printValues()

list.insertNode(9, 3)
list.printValues()

list.insertNode(2, 9)
list.printValues()
