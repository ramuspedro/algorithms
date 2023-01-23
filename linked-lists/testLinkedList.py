class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

# llist = LinkedList()
# first_node = Node("a")
# llist.head = first_node
# second_node = Node("b")
# first_node.next = second_node
# third_node = Node("c")
# second_node.next = third_node
# print(llist)
llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)