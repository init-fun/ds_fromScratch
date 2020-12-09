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
        self.start = self.start.next

    def del_last_node(self):
        if self.start is None:
            return "Nothing to delete"
        cnode = self.start
        while cnode.next is not None:
            cnode = cnode.next
        cnode.prev.next = None

    def delete_mid_node(self, delete_this):
        if self.start is None:
            return f"Nothing to delete"
        cnode = self.start
        while cnode.next is not None:
            if cnode.data == delete_this:
                break
            cnode = cnode.next

        if cnode is None:
            return f"{delete_this} is not present in the list"
        else:
            cnode.next.prev = cnode.prev
            cnode.prev.next = cnode.next


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
