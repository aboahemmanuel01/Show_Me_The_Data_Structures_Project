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
    lst = set()
    current = llist_1.head

    while current:
        lst.add(current.value)
        current = current.next
    current = llist_2.head

    while current:
        lst.add(current.value)
        current = current.next

    output = LinkedList()

    for l in lst:
        output.append(l)

    return output


def intersection(llist_1, llist_2):
    # Your Solution Here
    lst1 = set()
    current = llist_1.head

    while current:
        lst1.add(current.value)
        current = current.next
    
    lst2 = set()
    current = llist_2.head

    while current:
        lst2.add(current.value)
        current = current.next


    lst = []
    for x in lst1:
        if x in lst2:
            lst.append(x)


    output = LinkedList()

    for l in lst:
        output.append(l)

    return output


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


 #Edge Cases:
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [2,4,5,6,8]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))



linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
print(intersection(linked_list_7, linked_list_8))



linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [2,4,6,8]
element_2 = [2,4,6,8]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
print(intersection(linked_list_9, linked_list_10))
