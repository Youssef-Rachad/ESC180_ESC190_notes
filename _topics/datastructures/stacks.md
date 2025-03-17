---
title: Stacks
layout: default
jax: True
---
# Stacks on stacks on stacks

{% include colorbox.html 
   title="Definition: Stack ADT" 
   content="
   An **stack** is an ordered collection of elements with the operations `push` and `pop` defined as follows:

- `push` inserts an element into the collection.
- `pop` removes the most recently pushed element that is not yet removed and returns it.

   Observe that the Last element pushed In is always the First element popped Out hence we refer to the stack as a **LIFO** structure.
"
%}

We can intuitively visualise the stack as a tower of blocks where we can only add blocks to the top and tower. Similarly, we can only remove blocks from the top of the tower. 

# Python List Implementation of Stacks

From the above analogy, a natural implementation arises using lists in Python:

```python
class Stack:
  def __init__(self):
    self.data = []

  def push(self, element):
    self.data.append(element)

  def pop(self):
    # shorthand:
    # return self.data.pop()

    ret_val = self.data[-1]
    del self.data[len(self.data) - 1]
    return ret_val

  def __str__(self):
    return "Head -> " + str(self.data)
```

Note that `self.data.pop()` can be used since it is implemented in [Python](https://docs.python.org/3/tutorial/datastructures.html)'s standard library and behaves as expected - it removes the last element of the list and returns it. 
That said, we should try to implement datastructures rigourously and logically when learning them initially.

We can test our stack:
```python
if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(5)
  stack.push(10)
  print("Popping from the stack ", stack.pop()) # 10
  print("Now the stack is ", stack)             # [1, 5]
  stack.push(15)
  print("Popping from the stack ", stack.pop()) # 15
  print("Now the stack is ", stack)             # [1, 5]
```

# Complexity of Operations
Although the complexity of `push`and `pop` seem to be identical to that of the array's, 
we can use an amortised analysis approach to give a more realistic perspective on how stacks are used in practise.

`push` has constant time complexity $$\mathcal O(1)$$ though this is not obvious. 
In fact, we achieve this be reducing how often we need to reallocate memory to store more elements.
Instead of allocating memory for 1 element when we run out of memory, we can double the currently allocated memory such that subsequent pushes are likely to already have enough memory.
Since writing to memory can be done in constant time, we say that the amortised complexity is of $$\mathcal O(1)$$.
Some intuition can be found by considering that whenever we double the allocated memory (or use another strategy, though doubling is quite common), we are 'paying in advance' the computation needed for the next couple of pushes and because exponents grow quickly we pay the cost of reallocating even more memory less frequently. 

This is yet another useful abstraction provided by Python. In C, memory management is done entirely by the engineer, so you would have to implement the memory doubling strategy explicitly. However, Python lists are implement with [amortised analysis](https://wiki.python.org/moin/TimeComplexity) optimisations in mind so the above analysis holds.
