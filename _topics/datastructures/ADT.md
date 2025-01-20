---
title: Abstract Data Types
layout: default
jax: True
---
We've seen so far that C is a strongly typed language and that we should be specific about our `int`s, `char`s and more. These were some of the primitive data types that we've worked with and they came with a few operations which are built-in to most languages like C or Python.

What if we wanted more, like having a list of values that we could manipulate in an intuitive way? You might have a few ideas to achieve this so to stay general, we will introduce the concept of an ADT.

An **abstract data type** (ADT) is any collection of values, together with operations on those values. For example:

- `ints` with operations `+,-,*,/,%`
- `lists` with operations `insert, remove, get`

An **ADT** specifies what values are represented and what operations can be performed, but not how to store them or how to carry them out. They allow for modularity and reuse, as it is independent of implementation. A **data structure** is an implementation of an ADT as it is a way to represent the values, and algorithms for each operation.

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
