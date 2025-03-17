---
title: Better Strings
layout: default
jax: True
---
# Dynamic Strings
We've seen previously how to declare strings - static, using pointers, as constants - and noticed all approaches share a similar pattern of declaring some fixed size of memory and storing characters. What if we wanted to shorten or lenghthen our string?

This is a luxury we took for granted when programming in Python! We could declare some variable and give it any string we wanted, modifying it liberally without second thought. Armed with pointers and structs, we will attempt to emulate this desired behaviour in C and implement our own improvements!

# Functionality Requirements
Let's concretely define the behaviour we are aiming for:
- must support character level reassignment.
  ```c
string = "abc"
string[1] = 'z'
```
- must support appending to the string
  ```c
string = "abc"
string.append('d')
```
- should be easy to manage in memory: allocating, keeping track of sizes and reallocating when needed.

# Implementation
Let's define a custom string struct `mystr` as follows

```c
// my_str.h

#if !defined(MYSTR_H)
#define MYSTR_H
typedef struct mystr{
    char *block;
    int length;   // keep track of the length, we could use a size_t
    int capacity; // keep track of the size of the block
} mystr;

// initialise the string
void mystr_create(mystr **p_p_s);                           // Input: a pointer to apointer of a mystr
                                                            // Effect: set the pointer to the address of a valid mystr
// read a character at an index
char get_char(mystr *p_s, int index);                       // Input: a pointer of a mystr
                                                            // Effect: get the value at index to character
                                                            // sidenote - don't forget to check the index is within range
// change a character at an index
void set_char(mystr *p_s, const char character, int index); // Input: a pointer of a mystr
                                                            // Effect: set the value at index to character
                                                            // sidenote - const char is used here because we don't expect
                                                            //            to change the value of character inside the 
                                                            //            function (but this doesn't necessarily mean it 
                                                            //            can't be changed outside of the function
// read the whole string back
void set_char(mystr *p_s, const char character, int index); // Input: a pointer of a mystr
                                                            // Effect: set the value at index to character
                                                            // sidenote - const char is used here because we don't expect
                                                            //            to change the value of character inside the 
                                                            //            function (but this doesn't necessarily mean it 
                                                            //            can't be changed outside of the function
// append to the string
void append_str(mystr *p_s, const char *src);               // Input: a pointer of a mystr and a string literal
                                                            // Effect: appropriately append src to the mystr 
                                                            //         (adjusting the length and capacity as needed)
// These are secret tools we will use later 
void mystr_cat(mystr *p_dest, const mystr *p_src);
void mystr_destroy(mystr *p_s);
mystr mystr_substr(mystr *p_s, int i, int j);

#endif
```

As you can see, the main difference from a regular dynamically allocated string is that our string will know its length at all times, given that we always store its correct value. We will also go ahead and declare some basic functionality for our string: allocating/freeing and concatenation. Let's flesh out these functions!

```c
// mystr.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mystr.h"

void mystr_create(mystr **p_p_s)
{
  // In this function, we want to allocate an address to a valid mystr
  // so we need a pointer that points to the address of a valid mystr
  // (as opposed to a pointer that points directly to a valid mystr)
  *p_p_s = (mystr *)malloc(sizeof(mystr));                            // allocate enough memory for a char pointer and 2 integers
  if(*p_p_s == NULL){
    printf("ERROR: failed to allocate block of size 'mystr'");
    exit(1);
  }
  (*p_p_s)->capacity = 100;                                           // some default capacity
  (*p_p_s)->block    = (char *)malloc(sizeof(char) * (*p_p_s)->capacity);
  if(*p_p_s == NULL){
    printf("ERROR: failed to allocate block of size 100 chars");
    exit(1);
  }
  ((*p_p_s)->block)[0] = '\0';
  (*p_p_s)->length   = 0;
}

void set_char(mystr *p_s, const char character, int index)
{
  // Change the contents of the block at an index

  if((index >= p_s->length) || (index < 0)){
    printf("ERROR: index %d out of bounds in mystr (length: %d)\n", index, p_s->length);
    exit(1);
  }
  (p_s->block)[index] = character;
}

char get_char(mystr *p_s, int index)
{
  // Read the character at an index
  if (index < 0 || index >= p_s->length){
    printf("ERROR: Trying to access an index out of bounds\n");
    exit(1);
  }
  return p_s->block[index];
}

void append_str(mystr *p_s, const char *src)
{
  // We can't simply use strcat because we expect mystr to manage its capacity (while strcat doesn't not offer this)
  if(p_s->capacity < p_s->sz + strlen(src)){
    // We need to increase the capacity to fit the src string
    int new_capacity = p_s->capacity + strlen(src) + 1;
    // If we are increasing the capacity often, we might want to proactively increase the size
    new_capacity *= 2;
    p_s->block = (char *)realloc(p_s->block, new_capacity * sizeof(char));
    if(p_s->block == NULL){  // error checking: did realloc return a valid address?
      printf("ERROR: failed to reallocate memory block of size %d", new_capacity);
      exit(1);
    }
    p_s->capacity = new_capacity;// Note that we could update the size by setting it to the new capacity before multiplying by 2
  }
  p_s->length = p_s->length + strlen(src);  

  strcat(p_s->block, src);
}
```

It's also good practise to abstract away how an implementation of `mystr` works. Instead of accessing the `block` field directly, we should implement a function which returns the contents of the `mystr`.

```c
char* get_str(mystr *p_s)
{
  // Returns the whole string, i.e. the contents of 'block'
  return p_s->block;
}
```

# Testing our mystr so far
Let's try to create our string and read its value with our current implementation

```c
// testing_mystr.c
#include <stdio.h>
#include "mystr.h"

int main()
{
  mystr *p_s;
  mystr_create(&p_s);  // notice we are passing the address of our pointer!
                       // now we have an empty mystr with 100 characters of capacity

  append_str(p_s, "ESC");
  printf("The string is %s\n", p_s->block); // "ESC"

  append_str(p_s, "190");
  printf("The string is %s\n", p_s->block); // "ESC190"

  return 0;
}
```

We can now compile our code and test out the functionality! To do this, we need to tell the compiler what implementation of `mystr.h` to use first.

In VSCode, this `tasks.json` configuration seems to work fine 
```
...
"args": [
    "-fdiagnostics-color=always",
    "-g",
    "mystr.c",
    "testing_mystr.c",
    "-o",
    "${fileDirname}/${fileBasenameNoExtension"
],
...
```

If you're following along on your favourite terminal, the equivalent command can be run
```shell
gcc -fdiagnostics-color=always -g -o testing_mystr.exe mystr.c testing_mystr.c
```

# There's a leak in my string!
Running this code through Valgrind will reveal that there are memory leaks from the mystr allocation. This is because we haven't freed any of the memory we allocated. To do this, we can implement the `void mystr_destroy` function.
```c
// mystr.c
void mystr_destroy(mystr *p_s)
{
  // the order of freeing is important
  // if we free p_s before p_s->block then we lose access
  // to the block and have a memory leak
  free(p_s->block);  // free the block first
  free(p_s);         // free the memory pointed to by p_s
}
```
Now we can recompile and see that the memory is properly released before the program terminates. One subtlety to notice here is the order in which we free the memory: if we free the pointer to mystr first then we effectively have no reference to the block it contained. This causes a memory leak of its own (losing access to allocated memory locks that memory block so it counts as consuming memory without control; though modern OS's can deal with this by destroying the process entirely).
As an exercise, try to reverse the free order and observe the effects.
Generally, it's good practice to think about what parts have no dependent memory blocks and free those first. Note also that the integers are not freed because they are not allocated and their memory is released when we free the pointer to mystr.



Now that we can make one `mystr`, can we make a whole list of them? Sure we can, and we will use an array to implement this list (as opposed to linked lists)!

```c
// test_mystr.c

// First note that we have to dynamically allocate pointers for each mystr
// so the following would not work
// mystr arr[40]; // since we also need to allocate memory for the bloack

  // Instead we allocate an array of 40 mystr pointers
  mystr **str_block = (mystr **)malloc(40 * sizeof(mystr *));
  
  // Now we allocate their blocks
  for(int idx = 0; idx < 40; idx++){
    create_string(&(str_block[idx])); // .. or equivalently
    // create_string(str_block + idx);
  }
```

Here, `**str_block` is a pointer to an array of `mystr *` pointers. We can allocate each `mystr`'s block by accessing the i-th `mystr` and calling the `create_string()` function defined above.

# Using mystr
```c
// testing_mystr.c
#include <stdio.h>
#include "mystr.h"

int main()
{
  mystr *p_s;
  mystr_create(&p_s);  // notice we are passing the address of our pointer!
                       // now we have an empty mystr with 100 characters of capacity

  append_str(p_s, "ESC");
  printf("The string is %s\n", p_s->block); // "ESC"

  append_str(p_s, "190");
  printf("The string is %s\n", p_s->block); // "ESC190"

  return 0;
}
```
