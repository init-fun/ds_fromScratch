class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class circularLinkedList:
    def __init__(self):
        self.last_node = None

    def __str__(self):
        res = ""
        if self.last_node is None:
            print(f"list is empty")
            return res

        cnode = self.last_node.next  # ref to firsr node

        while True:
            res += str(cnode.data) + " > "
            cnode = cnode.next
            if cnode == self.last_node.next:
                break
        return res

    def insert_at_begining(self, ele):
        new_node = Node(ele)

        if self.last_node is None:
            self.last_node = new_node
            self.last_node.next = self.last_node
            return self.last_node

        new_node.next = self.last_node.next
        self.last_node.next = new_node

    def insert_at_the_end(self, ele):

        new_node = Node(ele)

        if self.last_node is None:
            self.last_node = new_node
            self.last_node.next = self.last_node
            return self.last_node
        new_node.next = self.last_node.next
        self.last_node.next = new_node
        self.last_node = new_node

    def insert_after(self, node_ele, data):
        if (
            self.last_node is None or self.last_node.next == self.last_node
        ) and pos == 0:
            return self.insert_at_begining(Node(ele))

        cnode = self.last_node.next
        new_node = Node(data)

        while cnode is not self.last_node and cnode.data != node_ele:
            cnode = cnode.next
        if cnode == self.last_node:
            return "element is not present"
        new_node.next = cnode.next
        cnode.next = new_node

    def delete_firstNode(self):
        if self.last_node is None:
            return "Empty list"
        self.last_node.next = self.last_node.next.next
        return

    def delete_lastNode(self):
        if self.last_node is None:
            return "empty list"
        if self.last_node.next == self.last_node:
            self.last_node = None
            return

        cnode = self.last_node.next
        while cnode.next != self.last_node:
            cnode = cnode.next

        cnode.next = self.last_node.next
        self.last_node = cnode
        return

    def delete_Node(self, this_node):
        if self.last_node is None:
            return
        if self.last_node == self.last_node.next and self.last_node.data:
            self.last_node = None
            return

        if self.last_node.next.data == this_node:
            self.last_node.next = self.last_node.next.next
            return

        cnode = self.last_node.next
        while cnode.next != self.last_node.next:
            if cnode.next.data == this_node:
                break
            cnode = cnode.next

        if cnode.next == self.last_node.next:
            print(f"Element {this_node} is not in the list")
        else:
            cnode.next = cnode.next.next
            if self.last_node.data == this_node:
                self.last_node = cnode
        return


myCircular = circularLinkedList()
print(myCircular)

myCircular.insert_at_begining(50)
myCircular.insert_at_begining(40)
myCircular.insert_at_begining(30)
print(myCircular)

myCircular.insert_at_the_end(100)
myCircular.insert_at_the_end(110)

print(myCircular)

myCircular.insert_after(50, 60)
print(myCircular)
print()

myCircular.delete_firstNode()
print(myCircular)

myCircular.delete_lastNode()
print(myCircular)

myCircular.delete_Node(40)
print(myCircular)
