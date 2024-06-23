---
title: Writing your first program in C
layout: default
---
# Basic Structure
The code in a C file is executed from its `main()` function. 
This is the part of the code which contains the main application.

Additionally, library are imported just as in Python using `#include <...>` statements.

Let's make our first program in C:
```c
#include <stdio.h>

int main()
{
    printf("Hello World!");
    return 0;
}
```
