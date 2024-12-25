---
title: Pointers
layout: default
jax: True
---
# Pointers
We can store the address of variables using pointers. To create a variable `p_a` that can store the address of another variable, we use the `int*` type. The operator `&` retrieves the address of a given variable.

```c
#include <stdio.h>
int main()
{
    int a = 42;
    int* p_a = &a; // & is the "address-of" operator
                   // int* is the type "address of int"
    printf("%ld\n", p_a); // %ld specifies a long integer
    return 0;
}
```

In the above code, `p_a` stores the address of `a`, which if we continue to use our earlier memory table, is equal to 3040. We can print the pointer using the type specifier %ld, as pointers are stored as long integers (which takes twice as more bits than regular integers).

Typically, long integers are 64 bits on most systems and integers are 32 bits. If you haven't noticed, this is why the addresses in our example tables go up by 32 ! (to make visualization easier)

The above code may give a warning (depends on system) that the formats that `%ld` expects and the variable given don't match, as `p_a` technically has type `int*`. However, because we can represent `p_a` as a long integer, we can cast it by running ```printf("%ld\n", (long int)p_a);``` instead.
# Dereferencing Operator
The dereferencing operator is given by `*` and acts on a memory address to get the value stored in memory at that address. For example, the code ```int value_of_a = *p_a;``` tells us the program to get the value of `p_a` which is an address, then go to that address, and retrieve the value stored there. Suppose we run the code

```c
#include <stdio.h>
    int main()
{
        int a = 42;
        int* p_a = &a;
        int b = *p_a; 
        return 0;
    }
```

we get the following memory table:

| Address  |  Value |
| -------  |  ------ |
| Addr3040 |  43 (`a` of type `int`) |
| Addr3072 |  3040 (`p_a` of type `int*`) |
| Addr3104 |  (space taken up by above) |
| Addr3136 |  43 (`b` of type `int`) |

The symbol `*` is used both to define variables (i.e. as a type) and also as an operator for dereferencing. While both are used in the context of memory, they are separate. 
You may notice that the variable `p_a` takes up 64 bits instead of the standard 32 bits. This is because addresses are usually stored as long integers by most systems. 
