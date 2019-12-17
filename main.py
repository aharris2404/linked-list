class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data=None):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, data):
        current_node = self.head

        while current_node.get_next() != None and current_node.get_data() != data:
            current_node = current_node.get_next()

        return current_node


    def size(self):
        current_node = self.head
        size = 0

        while current_node != None:
            size += 1
            current_node = current_node.get_next()

        return size

    def show(self):
        current_node = self.head

        while current_node != None:
            print(current_node.get_data())
            current_node = current_node.get_next()

        return


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return(self.data)

    def get_next(self):
        return(self.next_node)

    def set_next(self, new_next_node):
        self.next_node = new_next_node
