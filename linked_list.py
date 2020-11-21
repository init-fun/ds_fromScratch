class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"{self.data}"

class linkedList:
    def __init__(self):
        self.start = None

    def __str__(self):
        if self.start == None:
            return 'None'
        cnode = self.start
        final_list = ''
        while cnode is not None:
            final_list += str(cnode.data) + ' '
            cnode = cnode.next
        return final_list
    
    def traverse(self):
        if self.start == None:
            print("List is empty")
            return
        cnode = self.start
        while cnode is not None:
            print(cnode.data, end=" ")
            cnode = cnode.next
        print()
    
    def insert_at_begining(self, ele):
        nNode = Node(ele)
        if self.start is None:
            self.start = nNode
            return
        else:
            cnode = self.start
            nNode.next = cnode
            self.start = nNode
        
    def insert_at_end(self, ele):
        if self.start is None:
            self.start = Node(ele)
            return
        else:
            cnode = self.start
            nNode = Node(ele)
            while cnode.next is not None:
                cnode = cnode.next
            cnode.next = nNode
        
    def insert_at_pos(self, pos, data):
        index = 0
        if self.start is None and pos == 1:
            self.start = Node(data)
            return
        else:
            cnode = self.start
            while cnode is not None and pos < index:
                index += 1
                cnode = cnode.next
        
    def insert_after(self,element,data):
        if self.start is None:
            return f"List is empty"
        cnode = self.start
        nNode = Node(data)
        while cnode is not None and cnode.data != element:
            cnode = cnode.next
        nNode.next =cnode.next
        cnode.next = nNode

    def insert_before(self, element, data):
        if self.start is None:
            return f"List is empty"

        nNode = Node(data)
        

        if self.start.data == element:
            nNode.next = self.start
            self.start = nNode
            return

        cnode = self.start
        while cnode.next is not None:
            if cnode.next.data == element:
                nNode.next = cnode.next
                cnode.next = nNode
                break
            cnode = cnode.next
    
    def delete_firstnode(self):
        if self.start is None:
            print("List is empty")
            return 
        cnode = self.start
        self.start = cnode.next

    def delete_lastnode(self):
        if self.start is None:
            print("List is empty")
            return
        cnode = self.start
        if cnode.next.next is None:
            cnode.next = None
            return

        while cnode.next.next is not None:
            cnode = cnode.next
        cnode.next = None
        return 

    def delete_midnode(self, del_this):
        if self.start is None:
            print("List is empty")
            return
        cnode = self.start
        if cnode.data == del_this and cnode.next is not None:
            self.delete_firstnode()
            return
        
        while cnode.next.next is not None:
            if cnode.next.data == del_this:
                cnode.next = cnode.next.next
            cnode = cnode.next
        else:
            if cnode.next.data == del_this:
                cnode.next = None
                return
            else:
                print(f"{del_this} is not in List")
                return False
        
    def bubble_sort_data(self):
        if self.start is None or self.start.next is None:
            return self.start

        end_node = None
        while self.start.next is not end_node:
            # go until end_node becomes the second node 
            # initially end_node will be the last node
            cnode = self.start
            while cnode.next is not end_node:
                next_node = cnode.next
                if cnode.data > next_node.data:
                    cnode.data, next_node.data = next_node.data, cnode.data
                cnode = cnode.next
            end_node = cnode
            
    def bubble_sort_link(self):
        if self.start is None or self.start.next is None:
            return

        end_node = None
        while end_node is not self.start.next:
            prev_node = cnode = self.start
            while cnode.next is not end_node:
                next_node = cnode.next
                if cnode.data > next_node.data:
                    cnode.next = next_node.next
                    next_node.next = cnode

                    if cnode is not self.start:
                        prev_node.next = next_node
                    else:
                        self.start = next_node
                    cnode,next_node = next_node,cnode
                prev_node = cnode
                cnode = cnode.next
            end_node = cnode
    
    def reverse(self):
        if self.start is None and self.start.next is None:
            return self.start

        cnode = self.start
        prev_node = None
        while cnode is not None:
            next_node = cnode.next
            cnode.next = prev_node
            prev_node = cnode
            cnode = next_node
        self.start = prev_node

    def merge_it(self, sec_list):
         # create a new empty linkedlist
        merge_list = linkedList()
        # set the start of the new merged linked list to the list
        #  that is begin returned from the merge_sec list
        merge_list.start = self.merge_sec(self.start, sec_list.start) 
        return merge_list
    
    def merge_sec(self, first, second):
        # compare the first element of both the list
        # create a new node of the minimum element
        if first.data <= second.data:
            new_node = Node(first.data)
            first = first.next
        else:
            new_node = Node(second.data)
            second = second.next
        # set that new node to a new list
        new_merged_list = new_node
        very_first_node = new_merged_list

        # compare the first and second list's elements 
        # depending on the result, append the element into the new list
        # and move forward in the new list
        while first is not None and second is not None:
             
            if first.data <= second.data:
                new_node = Node(first.data)
                new_merged_list.next = new_node
                first = first.next
            else:
                new_node = Node(second.data)
                new_merged_list.next = new_node
                second = second.next
            new_merged_list = new_merged_list.next

        # add all the remaining elements to the list
        
        #if first list has finished but second has elements left
        while first is not None:
            new_node = Node(first.data)
            new_merged_list.next = new_node
            first = first.next
            new_merged_list = new_merged_list.next
        
        # if second list has finished but first has elements left
        while second is not None:
            new_node = Node(second.data)
            new_merged_list.next = new_node
            second = second.next
            new_merged_list = new_merged_list.next

        return very_first_node
    
    #start of merge sort
    def merge_sort(self):
        # get the first node of the merge list
        self.start = self.main_merge_fun(self.start)
        return self.start

    def main_merge_fun(self, unsorted_list):
        if unsorted_list is None or unsorted_list.next is None:
            return unsorted_list
        
        first_half = unsorted_list
        #currently the first half has the whole list
        second_half = self.divide_into_half(unsorted_list)
        # got the pointer to the other half of the list
        # now merge them together
        first_half = self.main_merge_fun(first_half)
        second_half = self.main_merge_fun(second_half)
        sorted_list = self.merge_two_in_one(first_half, second_half)
        # let's write the merge_two_in_one function from scratch
        return sorted_list

    def divide_into_half(self, orig_list):
        third_node = orig_list.next.next
        while third_node is not None and third_node.next is not None:
            third_node = third_node.next.next
            orig_list = orig_list.next
        second_half = orig_list.next
        orig_list.next = None
        return second_half

    def merge_two_in_one(self, first,second):
       
        if first.data <= second.data:
            new_node = Node(first.data)
            first = first.next
        else:
            new_node = Node(second.data)
            second = second.next
        new_list = new_node
        very_first_node_new = new_list

        while first is not None and second is not None:
            if first.data <= second.data:
                new_node = Node(first.data)
                first = first.next
                new_list.next = new_node
            else:
                new_node = Node(second.data)
                second = second.next
                new_list.next = new_node    
            new_list = new_list.next
            
        while first is not None:
            new_node = Node(first.data)
            first = first.next
            new_list.next = new_node
            new_list = new_list.next

        while second is not None:
            new_node = Node(second.data)
            second = second.next
            new_list.next = new_node
            new_list = new_list.next
        return very_first_node_new
    #end of merge sort


    #inserting a cycle into a linked list    
    
    def insert_cycle_at(self, ele):
        if self.start is None or self.start.next is None:
            return False
        
        cnode = self.start
        prev_node = self.start
        while cnode.next is not None:
            if cnode.data == ele:
                insert_cycle = cnode
                
            prev_node = cnode
            cnode = cnode.next
        
        if insert_cycle:
            cnode.next = insert_cycle
            print("Cycle inserted")
        else:
            print("Can't insert cycle at {ele}")
        
    def contain_cycle(self):
        tmp = self.has_cycle()
        if tmp:
            print(f"\tCycle is at {tmp}")
            return True
        return False


    def has_cycle(self):
        if self.start is None or self.start.next is None:
            return None
        
        slow_ref = self.start
        fast_ref = self.start

        while fast_ref is not None and fast_ref.next is not None:
            fast_ref = fast_ref.next.next
            slow_ref = slow_ref.next
            if fast_ref == slow_ref:
                return slow_ref

        return None
    
    def removing_cycle(self):
        fixed_node = self.has_cycle()
        counting_flag_node = self.has_cycle()
        count = 0
        while True:
            count += 1
            counting_flag_node = counting_flag_node.next
            if fixed_node == counting_flag_node:
                break

        print(f"\tTotal nodes in the cycle are {count}")
        first_node = self.start
        total_len = 0
        while first_node != fixed_node:
            total_len += 1
            first_node = first_node.next
            fixed_node = fixed_node.next
        
        print(f"\tTotal nodes in the list is {count + total_len} ") 
        first_node = self.start
        for i in range(10):
            first_node = first_node.next
        first_node.next = None
        print("Traversing list after removing the cycle")
        return self.traverse()

        


    



myLinkedList = linkedList()
unsorted_list = linkedList()
# insert at begining
print('Insert at begining')
print("Insert 50")
myLinkedList.insert_at_begining(50)
print("Insert 60")
myLinkedList.insert_at_begining(60)
print("Insert 70")
myLinkedList.insert_at_begining(70)
print("Insert 80")
myLinkedList.insert_at_begining(80)
myLinkedList.traverse()
print("------------")

# for sorting purpose
unsorted_list.insert_at_begining(50)
unsorted_list.insert_at_begining(60)
unsorted_list.insert_at_begining(70)
unsorted_list.insert_at_begining(80)


# insert at end
print('Insert at end')
print("Insert 1000")
myLinkedList.insert_at_end(1000)
print("Insert 1001")
myLinkedList.insert_at_end(1001)
myLinkedList.traverse()

print("------------")
# insert after
print("insert after")
#in the middle of the linkedlist
print("Insert after 50, 999")

myLinkedList.insert_after(50, 999)
#insert at the first element
print("Insert after 80, 81")
myLinkedList.insert_after(80, 81)
#insert after the last element
print("Insert after 1001, 1002")
myLinkedList.insert_after(1001, 1002)
myLinkedList.traverse()


print("------------")
# insert before
print("insert before")
#in the middle of the linkedlist
print("Insert before 999,998")
myLinkedList.insert_before(999, 998)
print("Insert before 1001,1000.5")
myLinkedList.insert_before(1001, 1000.5)
myLinkedList.traverse()

# deleting a node 
print("-------------")
print("Delete node")
print("Delete the very first node")
myLinkedList.delete_firstnode()
# myLinkedList.traverse()
print("Delete the very last node")
myLinkedList.delete_lastnode()
# myLinkedList.traverse()
print("Del node 50")
myLinkedList.delete_midnode(50)
# myLinkedList.traverse()
print("Del node 81")
myLinkedList.delete_midnode(81)
# myLinkedList.traverse()
print("Del node 1002")
myLinkedList.delete_midnode(1002)
myLinkedList.traverse()

print("-------------")
print("Sort the list")
unsorted_list.traverse()
unsorted_list.bubble_sort_data()
unsorted_list.traverse()
print("-------------")

print("-------mergin-----")
first_list = myLinkedList
second_list = unsorted_list
first_list.traverse()
second_list.traverse()

print("merge them together")
new_list = first_list.merge_it(second_list)
print(f"Current State: \n{new_list}")
new_list.merge_sort()
print("merge sort the list")
print(new_list)
print("-------------")

print("Inserting cycle at 998")
new_list.insert_cycle_at(998)
# new_list.traverse()

new_list.contain_cycle()
new_list.removing_cycle()

