


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    
    union_linked_list = LinkedList()

    if llist_1 == None:
        return llist_2
    if llist_2 == None:
        return llist_1

    current_ll1 = llist_1.head
    current_ll2 = llist_2.head


    while current_ll1 and current_ll2:
        if current_ll1 is None:
            union_linked_list.append(current_ll2)
            current_ll2 = current_ll2.next
        elif current_ll2 is None:
            union_linked_list.append(current_ll1)
            current_ll1 = current_ll1.next
        
        elif current_ll1.value <= current_ll2.value:
            union_linked_list.append(llist_1)
            current_ll1 = current_ll1.next
        else:
            union_linked_list.append(current_ll2)
            current_ll2 = current_ll2.next

    return union_linked_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    
    inter_secction = LinkedList()

    if llist_1 == None:
        return None
    if llist_2 == None:
        return None

    set1 = set()
    set2 = set()

    current_ll1 = llist_1.head

    while current_ll1 is not None:

        set1.add(current_ll1.value)
        current_ll1 = current_ll1.next

    current_ll2 = llist_2.head

    while current_ll2 is not None:

        set2.add(current_ll2.value)
        current_ll2 = current_ll2.next

    temp = set1.intersection(set2)

    if len(temp) == 0:
        return None

    for element in temp:
        inter_secction.append(element)

    return inter_secction




# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))