class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.next = next

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
    def print_result(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        current = self.head
        if current:
            while current.next != None:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value, self.head)

    def insert_before(self):
        pass

        

    def insert_after():
        pass

    def zip_lists(self, ll1, ll2):
        current_ll1 = ll1.head
        current_ll2 = ll2.head

        while current_ll1 != None and current_ll2 != None:
            next_ll1 = current_ll1.next 
            next_ll2 = current_ll2.next
            
            current_ll2.next = next_ll1
            current_ll1.next = current_ll2
# Looping though list, 
            current_ll1 = next_ll1
            current_ll2 = next_ll2
            ll2.head = current_ll2

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert('1')
    ll1.insert('3')
    ll1.insert('2')
    ll1.print_result()

    ll2 = LinkedList()
    ll2.insert('5')
    ll2.insert('9')
    ll2.insert('4')
    ll2.print_result()

    ll1.zip_lists(ll1, ll2)
    ll1.print_result()
    # LinkedList.to_string(ll1.zip_lists(ll1, ll2))
