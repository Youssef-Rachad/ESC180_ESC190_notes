---
title: Arrays
layout: default
jax: True
---
# Static Arrays
Arrays represent a contiguous block of memory that contains a collection of elements of the same data type. An array literal is the most common way to declare an array.
```c
int main()
{
  int numbers[] = {190, 160, 102, 185, 195, 159};
  return 0;
}
```
In this code block, we allocate enough memory for 6 integers (the size is counted at compile time) and populate it with the specified values.
We can also declare an empty array, which allows us to allocate the proper memory size, which depends on the data type populating the array.
```c
int main()
{
  float values[6];
  // ... later on

  for(int idx = 0; i < 6; i++) {
    values[i] = 3.14 * idx * 2;
  }

  return 0;
}
```
A third, less common instantiation includes the size in the literal `int numbers[6] = {190, 160, 102, 185, 195, 159};` but here the size is redundant. There is one case where the array we want to define is sparse.
```c
int main()
{

  int numbers[] = {
    [1] = 160, 
    [3] = 185, 
    [4] = 195,
  };
    
  return 0;
}
```
Notice that this declaration provides left padding (values before index 1 are populated with 0s). If we additionally want right padding to reserve space in the memory we can instantiate
```c
int main()
{

  int numbers[6] = {
    [1] = 160, 
    [3] = 185, 
    [4] = 195,
  };                 // now we have a 6 element array
    
  return 0;
}
```
We can also define multidimensional arrays as follows
```c
int main()
{

  int matrix[] = {
    {1, 2, 3},
    {4, 5, 6}, 
    {7, 8, 9},
  };
    
  return 0;
}
```
# Dynamic Arrays
When a static array is created, it is stored in a read-only part of the memory meaning that it cannot be resized afterwards. It's very useful to modify arrays in this way and in some cases, static allocation is not possible so let's learn more about dynamic arrays.

We already know that an 'array variable' in reality points to the first element of the array and subsequent elements are adjacent to it. Now, we can use a pointer to hold the address of the element which allows the compiler to store the array in the heap memory (for now, we should only understand that the heap is much larger and modifiable; which we want). Dynamic allocation thus requires calling an allocation method (defined in the standard library):
```c
#include <stdlib.h>

int main()
{

  int *numbers = (int *)malloc(10 * sizeof(int));

  return 0;
}
```
Let's unpack this code:
- Remember that the array is now defined by a pointer `*numbers`
- We allocate memory by calling `malloc`, meaning memory allocation:
	- There are 2 other ways of allocating memory: `calloc` and `realloc`, which we will see later on
- In the `malloc` call, we want enough memory for 10 integers which we obtain using the `sizeof` function
- Finally, we make sure that the result of malloc is a pointer to an integer array so we use a typecast `(int *)`
Suppose we wanted to store 20 integers instead of 10, then we can grow the array by calling
```c
#include <stdio.h>

int main()
{

  int *numbers = (int *)malloc(10 * sizeof(int));
  printf("I need more numbers!" );
  
  numbers = (int *)realloc(numbers, 20 * sizeof(int));
  return 0;
}
```
WARNING: now that we're dynamically allocating memory, we are also responsible for managing it. When we are done with our dynamically allocated array, we need to free the allocated memory used otherwise memory leak might result. A memory leak is the uncontrolled use of a program's memory and this happens when we lose track of the allocated memory or when we keep allocating memory and overconsume the computer's resources. Although we typically won't write code that will test our hardware's limitations, it's still very important to implement best coding practices.

Let's see an example of dynamically allocating a matrix and freeing it: to achieve this, each row of the matrix is a dynamically allocated array and the matrix is constructed using an array of pointers to integers
```
matrix -> [
           row -> [1, 2, 3],
           row -> [4, 5, 6],
           row -> [7, 8, 9],
           ]
```
```c
#include <stdio.h>
#include <stdlib.h>

int main ()
{
  // Create a dynamic array to hold the rows,
  // notice that matrix is a pointer to pointers to ints (int **)
  // because the rows are pointers to integers themselves (int *)
  int **matrix = (int **)malloc(3 * sizeof(int *)); 
  // Now allocate memory for each row
  for (int row = 0; row < 3; row++) { 
    matrix[row] = (int *)malloc(3 * sizeof(int)); 
  }

  // Let's print the contents of our matrix
  printf("matrix = [");
  for (int row = 0; row < 3; row++) { 
    for (int col = 0; col < 3; col++) { 
      printf("%d, ", matrix[row][col]); 
    } 
    printf("\n"); 
  }
  printf("]");

  // Now we need to free the allocated memory
  // This example is sligthly more complicated because we allocated
  // rows too, so let's iterate over the rows then free the matrix.
  // Freeing memory is done by freeing the pointer to that memory
  //   the compiler understands this and knows how to handle the rest
   
  for (int row = 0; row < 3; row++) { 
    free(matrix[row]);
  }
  free(matrix);
  // Note we free in reverse order of allocation.
  // Had we freed matrix before its rows we would lose the pointer to 
  // reference the rows and have a memory leak!
  
  return 0;
}
```
## Brief notes on `sizeof()`
sizeof returns the size occupied in memory by the contents of a variable.
It returns a value of type `size_t`. The `size_t` is defined in a way to guarantee that it can count the elements in an array (among other use cases) so it is forced to be the size of the largest unsigned integer. On my machine, this means that it resembles the unsigned long long which is 64-bit in size. Note that the compiler will give a warning rather than an error in the limit that the size used does not exceed 32 bits (about 4 billion; nothing to worry about hopefully).
