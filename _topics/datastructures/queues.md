---
title: Queues
layout: default
jax: True
---
# Queueing Up Values

{% include colorbox.html 
   title="Definition: Queue ADT" 
   content="
   An **queue** is an ordered collection of elements with the operations `enqueue` and `dequeue` defined as follows:

- `enqueue` inserts an element into the collection.
- `dequeue` removes the earliest pushed element that is not yet removed and returns it.

   Observe that the First element enqueued In is always the First element dequeued Out hence we refer to the queue as a **FIFO** structure.
"
%}

We can intuitively visualise the queue as a queue of people waiting where the first person to queue up is the first person served (wherever it is they are waiting). Similarly, we can only remove blocks from the top of the tower. 

_Notice the close similarity with [stacks]({{ site.baseurl }}{% link _topics/datastructures/stacks.md %})._

# Python List Implementation of Queues

From the above analogy, a natural implementation arises using lists in Python:

```python
class Queue:
  def __init__(self):
    self.data = []

  def enqueue(self, element):
    self.data.append(element)

  def dequeue(self):
    # shorthand:
    # return self.data.pop(0)

    ret_val = self.data[0]
    del self.data[0]
    return ret_val

  def is_empty(self):
    return len(self.data) == 0

  def size(self):
    return len(self.data)

  def __str__(self):
    return "Head -> " + str(self.data)
```

Note that `self.data.pop(0)` can be used since it is implemented in [Python](https://docs.python.org/3/tutorial/datastructures.html)'s standard library and behaves as expected - it removes the _first_ element of the list and returns it. 
That said, we should try to implement datastructures rigourously and logically when learning them initially.

We can test our queue:
```python
if __name__ == "__main__":
  queue = Queue()
  queue.enqueue(1)
  queue.enqueue(5)
  queue.enqueue(10)
  print("Dequeueing from the queue ", queue.dequeue()) # 1
  print("Now the queue is ", queue)             # [5, 10]
  queue.enqueue(15)
  print("Dequeueing from the queue ", queue.dequeue()) # 5
  print("Now the queue is ", queue)             # [10, 15]
```

# Complexity of Operations
Although the complexity of `enqueue`and `dequeue` seem to be identical to that of the array's, 
we can use an amortised analysis approach to give a more realistic perspective on how stacks are used in practise.

`enqueue` has constant time complexity $$\mathcal O(1)$$ though this is not obvious. 
In fact, we achieve this be reducing how often we need to reallocate memory to store more elements.
Instead of allocating memory for 1 element when we run out of memory, we can double the currently allocated memory such that subsequent enqueuees are likely to already have enough memory.
Since writing to memory can be done in constant time, we say that the amortised complexity is of $$\mathcal O(1)$$.
Some intuition can be found by considering that whenever we double the allocated memory (or use another strategy, though doubling is quite common), we are 'paying in advance' the computation needed for the next couple of enqueues and because exponents grow quickly we pay the cost of reallocating even more memory less frequently. 

This is yet another useful abstraction provided by Python. In C, memory management is done entirely by the engineer, so you would have to implement the memory doubling strategy explicitly. However, Python lists are implement with [amortised analysis](https://wiki.python.org/moin/TimeComplexity) optimisations in mind so the above analysis holds.
