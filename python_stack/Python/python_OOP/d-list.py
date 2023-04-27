# Doubly Linked Lists

# Build a class in Python and demonstrate how you can:
    # add a new node to the end of the list
    # delete an existing node
    # insert a node in between existing nodes(before and after node of given value)

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        new_node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        new_node.prev = runner
        runner.next = new_node

    def insertNode(self, value, pos):
        new_node = Node(value)
        runner = self.head
        counter = 1
        if(pos == 1):
            runner.prev = new_node
            self.head = new_node
            new_node.next = runner
            return
        while(runner.next != None):
            if(pos == counter):
                runner.prev.next = new_node
                new_node.prev = runner.prev
                new_node.next = runner
                runner.prev = new_node
                return
            counter += 1
            runner = runner.next
        if(pos == counter):
                runner.prev.next = new_node
                new_node.prev = runner.prev
                new_node.next = runner
                runner.prev = new_node
                return
        if(runner.next == None):
            new_node.prev = runner
            runner.next = new_node

    def deleteNode(self, value):
        runner = self.head
        if(runner.value == value):    # DONE
            runner.next.prev = None
            self.head = runner.next
            return
        while(runner.next != None):   # DONE
            if(runner.value == value):
                runner.prev.next = runner.next
                runner.next.prev = runner.prev
                break
            runner = runner.next
        if(runner.next == None):      # DONE
            runner.prev.next = None

    def getToMiddle_OfList(self):     # Doesn't return - just prints middle node object or two middle node objects
        runner = self.head
        nodes = 1
        while(runner.next != None):
            runner = runner.next
            nodes += 1
        print(f"\n--- There are {nodes} Nodes in this List ---")
        runner = self.head
        count = 1
        if((nodes % 2) == 0):
            while(runner.next != None):
                if(count == (nodes / 2)):
                    print(f"\nThe middle Nodes of this List are {runner.value} and {runner.next.value}:")
                    print(f"Node: {runner} | Node: {runner.next}")
                    return
                runner = runner.next
                count += 1
        else:
            if(nodes == 1):
                print("\nThere is only 1 Node in this List")
                print(runner)
                return
            while(runner.next != None):
                if(count > (nodes / 2)):
                    print(f"\nThe middle Node of this List is {runner.value}")
                    print(f"Node: {runner}")
                    return
                runner = runner.next
                count += 1

    def convert2Circular(self):
        print("\n--- Converting Doubly Linked List into Circular Linked List - Standy ... ---")
        first_Node = self.head
        runner = self.head
        last_Node = None
        count = 1
        while(runner.next != None):
            runner = runner.next
            count += 1
        last_Node = runner
        print(f"\nFirst Node is: {first_Node}")
        print(f"Last Node is: {last_Node}")
        # Reset
        runner = self.head
        runner.prev = last_Node
        last_Node.next = first_Node
        DL.print_list(count)
        return
    
    def reverse_List(self):
        print(f"\n--- REVERSING LIST - Standby ... ---")
        runner = self.head
        temp = None
        while(runner.next != None):
            temp = runner.prev
            runner.prev = runner.next
            runner.next = temp
            runner = runner.prev
        temp = runner.prev
        runner.prev = runner.next
        runner.next = temp
        runner = runner.prev
        self.head = temp.prev
        DL.print_list(0)
        return

    def removeDuplicates(self):
        print(f"\n--- REMOVING DUPLICATES - Standby ... ---")
        runner = self.head
        while(runner.next != None):
            gunner = self.head
            counter = 0
            while(gunner.next != None):
                if(gunner.value == runner.value):
                    counter += 1
                    if(counter == 2):
                        print(f"\nThere's a duplicate node: {gunner.value}. Removing ...")
                        DL.deleteNode(gunner.value)
                gunner = gunner.next
            if(gunner.value == runner.value):
                counter += 1
                if(counter == 2):
                    print(f"\nThere's a duplicate node: {gunner.value}. Removing ...")
                    DL.deleteNode(gunner.value)
            runner = runner.next
        DL.print_list(0)
        return
    
    def print_list(self, val):
        print("\n--- Printing the values in the List ---")
        runner = self.head
        if(val > 0):
            count = 1
            while(count <= val):
                print(f"\n{runner.value}")
                print(runner)
                print(f"Prev: {runner.prev} | Next: {runner.next}")
                runner = runner.next
                count += 1
            return
        while(runner.next != None):
            print(f"\n{runner.value}")
            print(runner)
            print(f"Prev: {runner.prev} | Next: {runner.next}")
            runner = runner.next
        print(f"\n{runner.value}")
        print(runner)
        print(f"Prev: {runner.prev} | Next: {runner.next}")

DL = DoublyLinkedList(1)
DL.addNode(2)
DL.addNode(3)
DL.addNode(4)
#DL.addNode(4)
DL.addNode(5)
#DL.addNode(5)
#DL.print_list(0)

#DL.deleteNode(1)
#DL.deleteNode(2)
#DL.deleteNode(3)
#DL.deleteNode(4)
#DL.deleteNode(5)
#DL.print_list(0)

#DL.insertNode(6, 1)
#DL.insertNode(6, 2)
#DL.insertNode(6, 3)
#DL.insertNode(6, 4)
#DL.insertNode(6, 5)
#DL.print_list(0)

# Please also think about the following:
    # How would you know if you have a circular linked list?   # DONE
        # DL.convert2Circular()

    # How would you get to the middle of the linked list?      # DONE
        # DL.getToMiddle_OfList()

    # How would you remove duplicate values in the list?       # DONE
        # DL.removeDuplicates()

    # How would you reverse the values in the list?            # DONE
        # DL.reverse_List()
