class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class doublyLinkedList:
    def __init__(self):
        self.start = None

    def __str__(self):
        if self.start is None:
            return f"List is empty"
        res = ""
        cnode = self.start
        while cnode is not None:
            res += str(cnode.data) + " > "
            cnode = cnode.next
        return res

    def insert_at_begining(self, data):
        if self.start is None:
            self.start = Node(data)
            return self.start

        new_node = Node(data)
        cnode = self.start
        new_node.next = cnode
        cnode.prev = new_node
        self.start = new_node

    def insert_at_end(self, data):
        if self.start is None:
            self.start = Node(data)
            return self.start
        cnode = self.start
        while cnode.next is not None:
            cnode = cnode.next
        new_node = Node(data)
        cnode.next = new_node
        new_node.prev = cnode

    def insert_after(self, after_this, data):
        if self.start is None:
            return f"List is empty"

        cnode = self.start
        new_node = Node(data)

        while cnode is not None:
            if cnode.data == after_this:
                break
            cnode = cnode.next

        if cnode is None:
            return f"{after_this} is not present in the list"
        else:
            new_node.prev = cnode
            new_node.next = cnode.next
            if cnode.next is not None:
                cnode.next.prev = new_node
            cnode.next = new_node

    def insert_before(self, before_this, data):
        if self.start is None:
            return f"List is empty"

        cnode = self.start
        new_node = Node(data)

        if cnode.data == before_this:
            # self.insert_at_begining(data)
            new_node.next = cnode
            cnode.prev = new_node
            cnode = new_node
            return

        while cnode is not None:
            if cnode.data == before_this:
                break
            cnode = cnode.next

        if cnode is None:
            return f"{before_this} is not present in the lsit"
        else:
            new_node.prev = cnode.prev
            new_node.next = cnode
            cnode.prev.next = new_node
            cnode.prev = new_node

    def del_very_first(self):
        if self.start is None:
            return "Nothin to delete"
        if self.start.next is None:
            # only Node
            self.start = None
            return

        self.start = self.start.next
        self.start.prev = None

    def del_last_node(self):
        if self.start is None:
            return "Nothing to delete"
        if self.start.next is None:
            self.start = None
            return

        cnode = self.start
        while cnode.next is not None:
            cnode = cnode.next
        cnode.prev.next = None

    def delete_mid_node(self, delete_this):
        if self.start is None:
            return f"Nothing to delete"
        if self.start.next is None:
            # only node
            if self.start.data == delete_this:
                self.start = None
                return
            else:
                return f"{delete_this} is  not present in the list"

        if self.start.data == delete_this:
            # very first node
            self.start = self.start.next
            self.start.prev = None
            return

        cnode = self.start.next
        while cnode.next is not None:
            if cnode.data == delete_this:
                break
            cnode = cnode.next

        if cnode.next is not None:
            # deleting in between node
            cnode.prev.next = cnode.next
            cnode.next.prev = cnode.prev
        else:
            # deletgin the last node
            if cnode.data == delete_this:
                cnode.prev.next = None
            else:
                return f"{delete_this} is not present in the list"

    def reverse(self):
        if self.start is None:
            return f"List is empty"
        if self.start.next is None:
            return self.start

        cnode = self.start
        next_node = self.start.next

        cnode.next = None  # last node to be
        cnode.prev = next_node  # adding the prev to the
        while next_node is not None:

            next_node.prev = next_node.next
            next_node.next = cnode
            cnode = next_node
            next_node = next_node.prev
        return self.start


my_dll = doublyLinkedList()
my_dll.insert_at_begining(60)
my_dll.insert_at_begining(40)
my_dll.insert_at_begining(10)

my_dll.insert_at_end(70)
my_dll.insert_at_end(90)
print("Before => ", my_dll)
my_dll.insert_after(70, 80)
print("After => ", my_dll)

my_dll.insert_before(40, 30)
print("After => ", my_dll)
my_dll.insert_before(30, 20)
print("After => ", my_dll)

my_dll.del_very_first()
# print("After => ", my_dll)

my_dll.del_last_node()
print("After => ", my_dll)

my_dll.delete_mid_node(40)
print("After => ", my_dll)
print()
my_dll.delete_mid_node(20)
print("After => ", my_dll)
my_dll.delete_mid_node(80)
print("After => ", my_dll)
my_dll.delete_mid_node(60)
print("After => ", my_dll)
