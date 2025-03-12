---
title: Abstract Data Types
layout: default
jax: True
---
# What is an ADT?
We've seen so far that C is a strongly typed language and that we should be specific about our `int`s, `char`s and more. These were some of the primitive data types that we've worked with and they came with a few operations which are built-in to most languages like C or Python.

What if we wanted more, like having a list of values that we could manipulate in an intuitive way? You might have a few ideas to achieve this so to stay general, we will introduce the concept of an ADT.

{% include colorbox.html 
   title="Definition" 
   content="
   An **abstract data type** (ADT) is any collection of values, together with operations on those values. For example:

- `ints` with operations `+,-,*,/,%`
- `lists` with operations `insert, remove, get`
"
%}

An **ADT** specifies what values are represented and what operations can be performed, but not how to store them or how to carry them out. This makes ADTs important for modularity and reuse, as it is independent of implementation which means that how we use an ADT does not  depend on its implementation. A **data structure** is an implementation of an ADT as it is a way to represent the values, and algorithms for each operation.

The motivation behind distinguishing ADTs from datastructures comes from complexity analysis which describes and calculates (asymptically) the cost of operations. An ADT is a way to describe what behaviour we want to enact but each datastructure that implement said ADT will come with its tradeoffs where some operations are performed quicker while others are performed slower.

## Lists

Let's take a closer look at the list ADT.

A list is an ordered collection of data items that supports the following operations:

- `Insert(list, i, x)`: add item `x` at index `i` of `list`. The item previously at index `i`, and all following items, are shifted up by one index to make room for `x`.
- `Remove(list, i)`: remove item at index `i` of `list`. The item previously at index `i+1`, and all following items, are shifted down by one index to fill the gap.
- `Get(list, i)`: return the item at index `i` of `list`.

We define this ADT very abstractly, such that we only describe the outcome of each operation, but not how to implement it. For example, lists can be implemented using arrays, but it can also be implemented using linked lists.

It is important to distinguish between ADTs and data structures, but it's also an easy distinction to make in most cases:

- Is it an idea? Is its functionality described hand wavily? Then it's likely an ADT.
- Could this be implemented in a few different ways? Then it's likely an ADT.
- Does it have very specific mechanisms like defining pointers to nodes in a specific fashion? Then it's likely a data structure.
- Is this code? Then it's definitely a datastructure.

## ArrayLists

An array is a data structure which implements a list using a contiguous block of memory. A reference is held to the first element of the array and subsequent elements are accessed by offsetting this reference. Note that arrays are strictly non-resizable.

### Complexity of operations
An array lists implement all of the list's operations

- `Insert(list, i, x)` is done in $\mathcal O(n)$ where $n$ is the number of elements. This is because we need to free the current block of memory and allocate another block which is large enough to insert the new element.
- `Remove(list, i)`: is similarly done in $\mathcal O(n)$ except the new memory block is one element smaller instead.
- `Get(list, i)`: is done in $\mathcal O(1)$ because the exact location in memory of the index can be calculated by offsetting the reference to the first element.