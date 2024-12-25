---
title: Linked Lists
---
Motivation: We cannot dynamically add an element to an existing array or block of memory easily, as there could be no space there! The only option we have is to re-allocate everything to a new location with enough space. This is inefficient, especially for larger arrays. Instead, we can use a special data structure called a **linked list**.

Linked lists are in fact a data structure which implement the list abstract data type ([ADT](https://youssef-rachad.github.io/ESC180_ESC190_notes/old_site/dsa/adt.html)). Recall the definition of a list:

A list is an ordered collection of data items that supports the following operations:

- `Insert(list, i, x)`: add item `x` at index `i` of `list`. The item previously at index `i`, and all following items, are shifted up by one index to make room for `x`.
- `Remove(list, i)`: remove item at index `i` of `list`. The item previously at index `i+1`, and all following items, are shifted down by one index to fill the gap.
- `Get(list, i)`: return the item at index `i` of `list`.

A linked list consists of a data structure called a `node`, which consists of the following information:

- `data:` the actual data you need to store
- `next:` the address of the next node

We can then make an array by creating a chain of these nodes, where we can find the next node by following the `next` pointer. While this uses up more space than a regular array, it has the benefit of preventing re-allocating everything.  
For example, if we want to add an element to the end of the list, we can simply create a new node and set the `next` pointer of the last node to point to the new node (+ a minor detail we'll touch on in a bit).

See the [lecture slides](https://www.cs.toronto.edu/~guerzhoy/190/lec/W07/LL.pdf) for a visual of linked lists and their operations.

# Linked List Operations

We want to implement the following operations: Inserting, Removing, and Searching.

## Insert Operation

Inserting: Suppose we already have a pointer to a node, and we wish to insert a node after that. What we can do is create this new node, and set its `next` pointer to point to the node that the original node pointed to. Then, we can set the original node's `next` pointer to point to the new node we just created.

- **Analogy:** A popular children's activity is to form a _human train,_ where each person puts their hand on the shoulder of the person in front of them, forming a chain (linked list). If a new participant Bob (the new node) wants to join the train in front of Alice (who is holding Carol's shoulder), Bob can do so by holding onto Carol's shoulder, and then Alice can hold onto Bob's shoulder.

Notice that we can insert nodes in constant time; this is faster than using an array implementation which would run in linear time.

## Remove Operation

Removing: Suppose we already have a pointer to a node, and we wish to delete that node. We can do so by setting the `next` pointer of the node before the node we want to delete to point to the node after the node we want to delete. Finally, we free up the memory.

- **Analogy:** If Bob wants to leave the train, he can simply let go of Carol's shoulder, and Alice can hold onto Carol's shoulder.

Just as with insertion, deletion is constant using a linked list.

## Get Operation

Getting: Suppose we wish to find a node (i.e. its pointer) at a certain index (i.e. the `i`th node) In the previous 2 operations, we assumed we already had this pointer. We can do so by iterating through the linked list by following the `next` pointer until we find the node we want.

- **Analogy:** If a teacher wants to find the 7th student, they can start from the very beginning of the train and follow it to the end until the 7th student is found.

Notice here the drawback of using a linked lists versus an array: getting the ith node requires us to walk the linked list until the desired node is found, meaning we run in linear time. Contrast this to an array which gets its elements in constant time through pointers.

# Implementation in C

We can implement the linked list as follows:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} node;

typedef struct LL{
    node *head;
    int size;
} LL;

void create_node(node **p_n, int data)
{
    *p_n = (node*)malloc(sizeof(node));
    (*p_n)->data = data;
    (*p_n)->next = NULL;
}


void create_LL_from_data(LL **p_LL, int *data_arr, int size)
{
    (*p_LL) = (LL*)malloc(sizeof(LL));
    (*p_LL)->size = 0; // initialize size to 0
    
    // keep track of the last node of the linked list
    node *tail = 0;

    for(int i = 0; i < size; i++){

        // n is a pointer to a node with data = data[i], next = NULL
        node *n;
        create_node(&n, data_arr[i]);

        // If the last node is the 1st node
        if(tail == 0){
            (*p_LL)->head = n;
        }

        // If the last node is not the 1st node
        else{
            // append the new node to the end of the linked list
            tail->next = n;
        }

        // update the tail
        tail = n;

        // update the size
        (*p_LL)->size++;
    }
}

int main(){
    int data_arr[] = {1, 2, 3, 4, 5};
    LL *p_LL;
    create_LL_from_data(&p_LL, data_arr, 5);
}
```

Here are some observations:

- The idea behind the `create_LL_from_data` function is to keep track of the last node of the linked list (known as the tail) and constantly update it such that every time we create a new node, the tail's `next` pointer points to the new node.
- Initializing a new node like `node *n` will cause the `next` pointer to be `0` i.e. `NULL`. This is how we can tell we reached the end of a linked list.
- we need to use pointers to pointers because we want to be able to modify the value of the `LL` pointer (i.e. the memory address it points to), rather than just the value of the data it points to.

### Insert for Linked List

We can implement insertion as follows:

```c

void LL_insert(LL *my_list, int new_elem, int index)
{
  // Create the new node 
  node *n;
  create_node(&n, new_elem);

  // If the list is empty
  if(my_list->head == NULL){
    my_list->head = n;
    my_list->size++;
    return;
  }

  // To insert at the very beginning
  if(index == 0){
    n->next = my_list->head;
    my_list->head = n;
    my_list->size++;
    return;
  }

  // Errors
  if (index < 0 || index > my_list->size-1){
    fprintf(stderr, "Invalid index %d", index);
    exit(1); // exits the program, returns 1 to the OS
  }

  // Traverse to the desired index
  node *cur = my_list->head;
  for(int i = 0; i < index; i++){
    cur = cur->next;
  }

  n->next = cur->next;
  cur->next = n;
  my_list->size++;
}
```

Note that we deal with a few edge cases:

- If the list is empty, which we can check if the head is `NULL`, then we proceed to make the new node the first (and only) element of the linked list.
- We want to implement it such that inserting it at index `0` corresponds to inserting it at the very beginning. To do this, not only do we need to update the `next` pointer of the new node, but the `head` pointer of our linked list. The order here is important. If we instead ran `my_list->head = n;` first, we lose information on where the original head is located.
- If the index is invalid, there are a few possibilities of what we can do.
    1. Just Crash: Sometimes this is a good idea, if we are trying to optimize the code. It's on the user to give valid parameters.
    2. Don't crash and don't insert. Instead, set a global variable to indicate an error. The reason we need a global variable here is that there's no other thing we can return that will indicate this. For example, if we are trying to return the element at an invalid index, a naive idea would be to return something like `-1` or `"Error"`, but how do we know that this is actually an error and their list doesn't actually include this!
    3. Print an error message. In particular the best way to print an error is using `fprintf(stderr, "message")` because it prints to the standard error stream, which is different from the standard output stream. Unlike `printf` (which sometimes doesn't show in terminal), this will always show, and allows regular print statements and error messages to be separated.

In the other cases, we first need to traverse to the desired index. Because this is not an array, we need to follow the linked list via the `next` pointers. Once we reach the desired index, we can update the `next` pointers of the new node and the node before it. Similar to above, the order of updating the `next` pointers matter!

### Remove and Get for Linked List

The code to remove and get for linked lists can be found [here](https://www.cs.toronto.edu/~guerzhoy/190/labs/linkedlist.c) and is very similar to the code for insert. For deletion, we just need to remember to update the `next` pointer of the node before the one we are deleting, and freeing up the memory. Like most cases, the order here is important. Getting is actually partially implemented in insertion and deletion, as we need to find the `i`th element. Error handling for all three functions are also similar.

## Best Practises

Suppose you have a piece of code, that relies on an abstract data structure (i.e. a list). We can define this structure in a header file [list.h](https://www.cs.toronto.edu/~guerzhoy/190/labs/list.h). Recall that an ADT doesn't include how it is implemented, just the operations.  
  
We can now implement this ADT in a separate file. For example, we can either implement it using [linkedlist.c](https://www.cs.toronto.edu/~guerzhoy/190/labs/linkedlist.c) or [arraylist.c](https://www.cs.toronto.edu/~guerzhoy/190/labs/arraylist.c). For example, if our `list.h` file looks like

```c
#if !defined(LIST_H)
#define LIST_H
void create_list_from_data(void **p_list, int *data_arr, int size);
void list_append(void *list, int new_elem);
void list_insert(void *list, int new_elem, int index);
void list_delete(void *list, int index);
void list_free_all(void *list);
int list_get(void *list, int index);
#endif
```

Then our `linkedlist.c` file needs to contain these functions. If we already have code (i.e. the earlier ones we wrote), we don't need to modify them. Instead, we can just create a new function that calls them in order to have the right form. For example,

```c
void list_insert(void *list, int new_elem, int index)
{
    LL_insert((LL*)list, new_elem, index);
}

int list_get(void *list, int index)
{
    return LL_get(list, index);
}
```

Notice that the functions in `list.h` take in void pointers, because we want them to be as general as possible (i.e. could be implemented using either an array or linked list). These additional functions we write in `linkedlist.c` are just wrappers. One final note is that although we can cast the void pointer to the correct type `(LL*)`, it is not necessary.  
  
We can do this for both `linkedlist.c` and `arraylist.c`, and when we want to compile our main program, we can choose to compile it with either `linkedlist.c` or `arraylist.c`. For example, we can run

```bash
gcc linkedlist.c -c -o linkedlist.o
```

to create the object file `linkedlist.o`. We can then compile `main.c` alongside `linkedlist.o` to create an executable. We can do this by running

```bash
gcc main.c linkedlist.o -o main
```

If we instead wanted to compile using the array list implementation, we can run

```bash
gcc main.c arraylist.o -o main
```

This has several advantages:

- Modularity and Reusability: When writing our main code, we don't have to worry about how certain functions are implemented. Also, if we already have code that can implement abstract data structures, we can just re-use them for future projects without changing too much!
- Faster compilation: Using a precompiled object like `linkedlist.o` can save compilation time. Although this is not a big problem now, compilation time can be an issue for larger and more complex projects.

# Implementation in Python

In this lecture, we will discuss how to implement a linked list in Python. Most of the time, you won't need to use a linked list in Python (we'll see an example next Monday), but it is still important to understand how linked lists work, and the work done in this lecture will be useful for implementing other data structures in Python for the rest of this course. The advantage of Python over C is pedagogical here, we want to focus on the data structure and not the specific implementation details.  
  
If you are not familiar with classes, please see the last part of L19. Consider the Node class,

```python
class Node:
  def __init__(self, value):
      self.value = value
      self.next = None
  
  def __str__(self):
      return f"{self.value}"
```

By default, we have set `self.next = None` to indicate that the next node is not yet defined. We can then create a linked list by creating a series of nodes and linking them together. For example,

```python
if __name__ == '__main__':
  n1 = Node(12)
  n2 = Node(15)
  n3 = Node(500)

  n1.next = n2
  n2.next = n3
```

Recall that in the Python memory model, values are not copied. Everything is passed by reference. Therefore, something like `n1.next = n2` means we make `n1.next` refer to the address of `n2` (so they are treated as the "same" thing). In C, the analogy would be

```c
node *n1 = create_node(12)
node *n2 = create_node(15)
n1->next = n2;
```

where the function `create_node()` performs the memory allocation for you, which is what Python is doing behind the scenes. We can also make a linked list class and include some functions. For example,

```python
class LinkedList:
  def __init__(self):
      self.head = None
  
  def get_i(self, i):
      # return the value at index i
      cur = self.head
      for j in range(i):
          cur = cur.next
      return cur.value

  def append(self, value):
      '''Add a new node with the value value to the end of the list'''
      # Create a new node
      new_node = Node(value)
      print(new_node)

      if self.head == None:
          self.head = new_node
      else:
          # Find the last node
          cur = self.head
          while cur.next != None:
              cur = cur.next
          cur.next = new_node
  
  def insert(self, value, i):
      '''Insert a node with the value value at index i'''
      new_node = Node(value)

      if i == 0:
          new_node.next = self.head
          self.head = new_node
      else:
          cur = self.head
          for j in range(i-1):
              cur = cur.next
          new_node.next = cur.next
          cur.next = new_node

  def __str__(self):
      cur = self.head
      s = ""
      if(cur == None):
          return "Empty list :("
      
      while cur != None:
          s += str(cur) + " -> "
          cur = cur.next
      return s[:-4] # remove last arrow
```

Note that we didn't do anything new here. We took the existing code we had in L18 and transformed it into Python equivalents. The only new thing is the `__str__` function, which allows us to easily print out the linked list. For this function we have two cases: if the list is empty, we print something, and if the list is non-empty we print out the values of each node, connected with the -> symbol. We can then test our code,

```python
if __name__ == '__main__':
  LL = LinkedList()
  LL.append(3)
  LL.append(50)
  LL.append(100)

  print(LL)
```