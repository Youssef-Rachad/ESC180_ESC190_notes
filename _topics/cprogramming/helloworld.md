---
title: Writing your first program in C
layout: default
---
# Basic Structure
Writing code in C can be different from writing in Python. 
For one, the main block was optional in Python and the interpreter could still run scripts that didn't include it.
In C however, the entry point of the code is its `main()` function and is required to run the compiled program.
This is the part of the code which contains the main application.

Additionally, libraries are imported just as in Python using `#include <...>` statements.

Let's make our first program in C:
```c
#include <stdio.h>

int main()
{
    printf("Hello World!");
    return 0;
}
```

# Variables
The way variables are defined in C is one more difference from Python.
Variables must be declared with their data types and don't necessarily need to be initialised 
(although it's a good practise to initialise variables to avoid undefined variable errors in your code).
Note also that while a variable's contents can usually be modified, it's data type cannot be modified.
```c
#include <stdio.h>

int main()
{
    int a;
    a = 42;
    printf("The value of a is %d", a);
    a = 190;

    // a = "ESC"; will give an error at compilation time 
    //            because "ESC" is not an integer

    return 0;
}
```
# The Memory Model
A lot of C's behaviour may initially come across as unintuitive or pedantic since Python hid away much of the mechanical process involved in managing our programs' memory usage.
In fact, we need to declare the data type of a variable before hand because the compiler needs to assign the appropriate space in the memory table; where all of the program's variables are stored. Each data type takes up a specific amount of space (which we will see in [Data Types]({{ site.baseurl }}{% link _topics/cprogramming/datatypes.md %}) later) so the compiler can only store a variable of that size or smaller.

The memory table itself is an association between the virtual memory allocated for the program and the values we define.
In the example above, the program inialises the memory table in the following state:

| Address | Value |
| ------- | ----- |
|  3040   | `42` (`a` of type `int`) |
|  3072   |       |
|  3104   |       |
|  3136   |       |

We can see that at address `3040`, we have enough space for a 32 bit integer and this is where the value of `a` is stored. _In practise, there is some memory padding and the size of an integer comes down to specific implementations of the C language (since the standard defines it as 'at least 16 bits'. This is all an example, as is the value of `3040` to illustrate the concept._

After we update the value of `a` to `43`, we would see:

| Address | Value |
| ------- | ----- |
|  3040   | `43` (`a` of type `int`) |
|  3072   |       |
|  3104   |       |
|  3136   |       |

So the memory table creates an association between the address `3040` and the variable name `a`. Therefore, the variable names we use in the code simply make our lives easier by serving as readable labels to entries in the memory table.

From this model we can understand why reassigning a value of incompatible type throws an error: it won't fit in the allocated memory. Python gets around this issue by reallocating another memory address and storing the new value. Recall lab 9 from ESC180: the `id()` obtained is not exactly the location in memory where the variable is stored but it gives an analogy for how programs are meant to handle memory allocation.

# Standard Input Output
Much of the basic functionality for a typical program is sometimes only accessible through libraries.
For example, we have been importing `<stdio.h>` in order to call `printf()` (_The main reason for this is that C is designed for a plethora of application and not all of them need I/O for example embedded systems_).

Another feature worth mentioning are format specifiers like the `%d`. 
Format specifiers allow us to format strings in one go instead of concatenating multiple strings.
Common format specifiers include:

| Format Specifier | Data Type |
| ---------------- | --------- |
| `%c`             | characters|
| `%d`             | integers (d for decimal)|
| `%e`             | scientific notation|                   
| `%f`             | floats |
| `%s`             | strings|
| `%p`             | pointers|
| `%x`             | hexadecimal|
| `%u`             | unsigned integer |
