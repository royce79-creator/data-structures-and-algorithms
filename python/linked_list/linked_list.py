class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        # method body here
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node
    
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        current = self.head
        str_result = ''
        while current:
            str_result += f"{ {current.value} } -> "
            current = current.next
        return str_result + 'None'
# Had help from Alex & Brandon.

    def append(self, value):
        current = self.head
        node1 = Node(value)
        while current:
            if current.next == None:
                current.next = node1
                break 
        current = current.next

    def insert_before(self):
        pass

        

    def insert_after():
        pass

