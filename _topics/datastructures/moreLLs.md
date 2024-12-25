---
title: More Linked Lists
---
# Doubly Linked Lists
Our current implementation for the linked list only allows for forward traversal; what if we wanted to access previous nodes in the linked list?

This is where a doubly linked lists comes into play: by storing a pointer to the previous node we can unlock the ability to move backwards in the linked list. Note however that this great power comes with great responsibility and that we must do some extra housekeeping to update node pointers when inserting/deleting nodes in a doubly linked list.
# Circular Linked Lists
We have the tail node point back to the head node such that when we reach the end of the linked list we can then roll over to the head of the linked list. 
See if you can use the previous implementations of a singly or doubly linked list to implement a circular linked list (the implementation is left as an exercise to the reader).