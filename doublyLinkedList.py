class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class doublyLinkedList:
    def __init__(self, data=None):
        self.start = None

    def __str__(self):
        if self.start is None:
            return f"List is empty"
        cnode = self.start
        res = ""
        while cnode is not None:
            res += str(cnode.data) + " > "
            cnode = cnode.next
        return res

    def insert_at_begining(self, ele):
        if self.start is None:
            self.start = Node(ele)
            return

        cnode = self.start
        new_node = Node(ele)

        new_node.next = cnode
        cnode.prev = new_node
        self.start = new_node

    def insert_at_end(self, ele):
        if self.start is None:
            self.insert_at_begining(Node(ele))
            return
        cnode = self.start
        new_node = Node(ele)

        while cnode.next is not None:
            cnode = cnode.next
        cnode.next = new_node
        new_node.prev = cnode

        return

    def insert_node_here(self, ele, pos):
        if (self.start is None and pos == 1) or pos == 1:
            self.insert_at_begining(Node(ele))
            return

        cnode = self.start
        index = 1
        while cnode.next is not None and index < pos:
            cnode = cnode.next
            index += 1

        # insert the new node here
        new_node = Node(ele)
        new_node.prev = cnode
        new_node.next = cnode.next
        cnode.next.prev = new_node
        cnode.next = new_node
        return

    def insert_before_this(self, before_this, ele):
        if self.start is None:
            return "List is empty"

        cnode = self.start
        new_node = Node(ele)
        if cnode.data == before_this:
            return self.insert_at_begining(new_node)
        while cnode.next is not None:
            if cnode.next.data == before_this:
                break
            cnode = cnode.next
        else:
            print(f"{before_this} is not present in the list")
        new_node.prev = cnode
        new_node.next = cnode.next
        cnode.next.prev = new_node
        cnode.next = new_node
        return

    def insert_after_this(self, after_this, ele):
        if self.start is None:
            return "List is empty"

        cnode = self.start
        new_node = Node(ele)
        if cnode.data == after_this:
            new_node.next = cnode.next
            new_node.prev = cnode
            cnode.next = new_node
            new_node.next.prev = new_node
            return

        while cnode is not None:
            if cnode.data == after_this:
                break
            cnode = cnode.next
        else:
            print(f"{before_this} is not present in the list")
        if cnode.next is not None:
            new_node.next = cnode.next
            new_node.prev = cnode
            cnode.next = new_node
            new_node.next.prev = new_node
        return

    def delete_very_first_node(self):
        if self.start is None:
            return f"List is empty"
        self.start = self.start.next
        self.start.prev = None
        return

    def delete_last_node(self):
        if self.start is None:
            return f"List is empty"
        if self.start.next is None:
            self.start = None
            return

        cnode = self.start
        while cnode.next is not None:
            cnode = cnode.next

        cnode.next = None
        return


mydoublylinkedlist = doublyLinkedList()
print(mydoublylinkedlist)

mydoublylinkedlist.insert_at_begining(20)
mydoublylinkedlist.insert_at_begining(10)
mydoublylinkedlist.insert_at_begining(0)
print(mydoublylinkedlist)

mydoublylinkedlist.insert_at_end(30)
mydoublylinkedlist.insert_at_end(40)
print(mydoublylinkedlist)

mydoublylinkedlist.insert_before_this(40, 35)
mydoublylinkedlist.insert_before_this(30, 25)
print(mydoublylinkedlist)

mydoublylinkedlist.insert_after_this(10, 15)
mydoublylinkedlist.insert_after_this(0, 1)
print(mydoublylinkedlist)

mydoublylinkedlist.insert_node_here(2, 2)
mydoublylinkedlist.insert_node_here(3, 3)
print(mydoublylinkedlist)
