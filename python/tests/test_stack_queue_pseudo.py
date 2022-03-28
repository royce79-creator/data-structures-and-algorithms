from code_challenges.stack_and_queue.stack_and_queue import PseudoQueue

def test_pseudo_queue():
    pseudo = PseudoQueue()
    assert pseudo

def test_pseudo_queue_enqueue():
    pseudo = PseudoQueue()
    pseudo.enqueue('a')
    assert pseudo.dequeue() == 'a'

def test_pseudo_queue_enqueue_multi():
    pseudo = PseudoQueue()
    pseudo.enqueue('a')
    pseudo.enqueue('b')
    pseudo.enqueue('c')
    assert pseudo.dequeue() == 'a'
    assert pseudo.dequeue() == 'b'
    assert pseudo.dequeue() == 'c'

def test_pseudo_queue_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    assert pseudo.dequeue() == 1

def test_pseudo_queue_dequeue_multi():
    pseudo = PseudoQueue()
    pseudo.enqueue(3)
    pseudo.enqueue(2)
    pseudo.enqueue(1)
    assert pseudo.dequeue() == 3
    assert pseudo.dequeue() == 2
    assert pseudo.dequeue() == 1
