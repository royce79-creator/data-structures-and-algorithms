from linked_list.linked_list import LinkedList, Node

def test_node_instance_1():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

def test_node_instance_2():
    node = Node(1,None)
    assert node.next != node
    assert node.value != 2

def test_empty_linked_list():
    ll = LinkedList()
    assert ll.head == None

def test_insert_to_empty_linked_list_3():
    # ll/head = apple -> This is what would be in the list with this node value
    ll = LinkedList()
    ll.insert('goku')
    assert ll.head.value == 'goku'

# From Demo Code
def test_insert_to_linked_list():
    ll = LinkedList()
    # head is empty or none
    node1 = Node('apple')
    # ll.head is none
    ll.head == node1
    # ll.head is apple
    node2 = Node('pear')
    #apple.next is none
    node1.next = node2
    # apple.next is pear
    # apple goes to pear which goes to none
    ll.insert('banana')
    # new order is banana to apple to pear
    assert ll.head.value == 'banana'

def test_includes_in_linked_list():
    ll = LinkedList()
    ll.insert('goku')
    ll.insert('piccolo')
    ll.insert('vegeta')
    ll.insert('gohan')
    assert ll.includes('vegeta') == True

def test_includes_not_in_linked_list():
    ll = LinkedList()
    ll.insert('goku')
    ll.insert('piccolo')
    ll.insert('vegeta')
    ll.insert('gohan')
    assert ll.includes('freiza') != True

def test_to_string_linked_list():
    ll = LinkedList()
    ll.insert('goku')
    ll.insert('freiza')
    ll.insert('gohan')
    assert ll.to_string() == "{ goku } -> { freiza } -> { gohan } -> None"

def test_to_string_not_working():
    ll = LinkedList()
    ll.insert('goku')
    ll.insert('freiza')
    ll.insert('gohan')
    assert ll.to_string() != "{ goku } -> { freiza } -> { gohan } -> None"
