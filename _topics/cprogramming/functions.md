---
title: Functions in C
layout: default
---
# Functions

Functions generally work mostly the same way as Python. It is important to note that when an input is passed to the function, the function makes a copy of it in the sense that it uses a different locals frame. For example,

```c
#include <stdio.h>
    int f(int x){
        return x + 1;
    }
    int main()
{
        int a = 42;
        int* p_a = &a;
        int b = *p_a; 

        int c = f(b);
        return 0;
    }
```

which gives the additional memory table,

| Locals Frame [Function] | Value |
| ----------------------- | ----- |
| 1280 	                  |42 (`x` of type `int`) |
| 1312 	                  |       |
| 1344 	                  |       |
| 1376 	                  |       |

Therefore, if we were to change the value of x inside the function, it would only affect the value at address 1280, and the value of b (from the main memory table) will not be affected.

# Functions don't return arrays
Understanding why functions in C return a single variable requires an intuition about computer hardware so the following is a brief discussion out of scope:
In assembly, functions store local variables on the stack, so in the stack frame (in Python/C we call this the function frame). When the function call is done, the return value is stored in a register (think of this as a fixed sized memory address the CPU knows about very well) and all the local variables are forgotten about during the cleanup process. Since a register can only hold 1 value, the function can only return 1 variable or, at best, a pointer to the first element in a dynamically allocated block in the heap.

---

Back on course: C retains the idea of returning a single value from a function, hence arrays cannot be returned. When passing arrays into a function or when returning an array from a function, only the reference to the first element is actually passed/returned (1 variable). This means that when passing an array to the function, we can't know the length of the array using `sizeof` since it returns the size of a pointer. This also means that when returning an array from a function, only a reference to the first element is returned so if the array is static then the subsequent elements created in the function frame are lost but if the array is dynamic, the array elements live in the memory where they can still be access via the returned pointer. 

Two common approaches are followed to manipulate arrays in functions:
1. We can dynamically allocate memory during the function call. This creates a pointer which points to an allocated block in memory (outside of the function frame) which we can return.
   
2. We can pre-defined an array (either static or dynamic) and pass it as an argument to the function. This allows the array to be populated in the function.

```c
#include <stdio.h>

void BeamMeUpArray(int arr[])
{
    printf("A pointer is 8 bytes, an integer is 4: 8/2 = %d\n", sizeof(arr)/sizeof(arr[0]));

	// Note that we assume the array is large enough to contain 4 elements
    for(int i = 0; i < 4; i++) {
        arr[i] = i;
    }
}

int main()
{
	int array[4];
	
	BeamMeUpArray(array);
	
    for(int i = 0; i < 4; i++) {
        printf("array[%d] = %d\n", i, array[i]);
    }
    
	return 0;
}
```