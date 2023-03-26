from cq import CircularQueue

cq = CircularQueue()
print("Starting Size", len(cq) )
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
print("Current Size", len(cq) )
print("Current Head", cq.first())
cq.rotate()
print("Current Head after rotating", cq.first())
