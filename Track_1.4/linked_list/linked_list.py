class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        if self.head is None:
            return

        while self.head and self.head.value == val:
            if not all:  # If we delete only first value
                self.head = self.head.next
                if self.head is None:  # If after deleting the list is empty
                    self.tail = None
                return
            # If first element are equal after deleting all entries
            self.head = self.head.next

        node = self.head
        previous_node = None
        while node is not None:
            if node.value == val:
                if node.next is None:  # If we delete last value
                    previous_node.next = None
                    self.tail = previous_node  # Update tail if deleted last value
                    if not all:  # If we need to delete only one value
                        break
                else:
                    previous_node.next = node.next

                if not all:  # If we need to delete only one value
                    break
            else:
                previous_node = node

            node = node.next

        # If after deleting there are one element then update tail
        if self.head and self.head.next is None:
            self.tail = self.head

    def clean(self):
        if self.head is None:
            return

        while self.head is not None:
            next_node = self.head.next
            del self.head
            self.head = next_node

    def len(self):
        if self.head is None:
            return 0

        node = self.head
        length = 1

        while node is not None:
            next_node = node.next

            if next_node is None:
                return length
            else:
                length += 1
                node = node.next

    def insert(self, afterNode, newNode):
        if afterNode is None:
            # put first
            newNode.next, self.head = self.head, newNode
        else:
            newNode.next, afterNode.next = afterNode.next, newNode

        return
