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
