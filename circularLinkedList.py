# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".

# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.

# You've been given the Linked List Node class code:


class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None



    //check for circularly linkedlist


    def singular(node):
        # create two list

        marker1 = node
        marker2 = node
        # marker2 haven't reached tail and isn't about to finish
        while marker2 != None and marker2.nextNode != None:
            marker1 = marker1.nextNode
            # moving marker2 twice faster than marker1
            marker2 = marker2.nextNode.nextNode

            # it is circular linked list as marker2 meets/passes marker1 so they are equal
            if marker2 == marker1:
                return True
        # maeker2 never meets marker1
        return False