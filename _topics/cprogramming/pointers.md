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

# Pointers to pointers
It will be useful in many situations to have pointers which point to more pointers. For instance, we can see how dynamic arrays use pointers to reference an array block in memory and by extension, a matrix like concept can be designed using an "array of arrays" which requires a pointer to pointers. 

For now, let's look at a contrived example to double a number:
```c
#include <stdio.h>

void double_without_change(int **p_p_a)
{
  int b  = **p_p_a * 2; // take the value pointed to by the pointer pointed to by p_p_a
                        // we are drilling down to find the value 'a'
                        // the address p_p_a points to the address p_a, we follow it
                        // the address p_a points to the integer a, we go to 'a' and retrieve its value
  *p_p_a = &b;
}

int main()
{
 
  int a = 42; 

  return 0;
}
 ```
# Increment and Decrement Operators
The increment (++) and decrement (--) operators work on numerical primitive types to change the value of the operand by +/- 1, for example `int foo = 5; foo++` increases the value of `foo` by 1.

Of note is the placement of these operators. Unlike most other unary operators, the increment and decrement operators exist in a prefix and a postfix variant which affects the order of operation. Under the hood, the increment operator reads the value of the variable into the expression then modifies it. If we use a postfix operator, the value of the variable is changed _after_ the expression is evaluated but if we use a prefix operator, the value of the variable is changed _before_ the expression is evaluated. 

An example is useful to illustrate this concept:
```c
int num = 0;
while(num < 5) {
  printf("%d", num);
  num = num + 1;
}
// prints 0, 1, 2, 3, 4
// we can write this as

int num = 0;
while(num++ < 5) {  // 1. Access the value of num
                    // 2. Compare it to 5
                    // 3. Increment it by +1
  printf("%d", num);
}
// prints 1, 2, 3, 4, 5

// Now let's observe the change when using a prefix operator
int num = 0;
while(++num < 5) {  // 1. Access the value of num
                    // 2. Increment it by +1
                    // 3. Compare it to 5
  printf("%d", num);
}
// prints 1, 2, 3, 4
```
The fact that the prefix variant increments the value before anything is done and that the postfix variant waits until after the expression is evaluated ties into the greater concept of operator precedence. We say that the prefix operator has a higher precedence than the postfix operator. Operator precedence can also be observed in the following example:
```c
int a = 42;

int b = a++; // 1. Access the value of a
             // 2. Assign it to b (so b = 42)
             // 3. Increment a by +1 (so a = 43)

int c = --a; // 1. Access the value of a
             // 2. Decrement it by -1 (so a = 42)
             // 3. Assign it to c (so c = 42)
```

## Silly string
Let's look at how we can use the increment operator to iterate through a string (in increasingly funny ways) using pointers:
```c

char *str = "abc"; // Re: str holds the address of 'a'
                   //     so 'b' is at the address str+1
                   
str++;             // 1. Access the value of str (address of 'a')
                   // 2. Increment str by 1 (now, address of 'b')

printf("%s\n", str); // prints bc
printf("%c\n", *str);// prints b
printf("%c\n", *str++); // 1. Access the value of str (address of 'b')
                        // 2. Print the value pointed to by str  ('b')
                        // 3. Increment str by 1 (now, address of 'c')
printf("%c\n", *str);// prints c
```
We can then easily set up a program to iterate through a string like so
```c
char *str = "abc";

while(*str != '\0') {
  printf("%c", *str++);
}
```
In this loop, we iterate through the characters in the string using `*str` to access the character and `str++` to increment the pointer simultaneously (`*str++`). The stop condition is reaching the null terminator, but since the null terminator has a falsy value we can simply use `while(*str){...}` which will break when we reach the end of string.

Last, we can make us of all the quirks built-into the C language to write a silly string iteration loop
```c
#include <stdio.h>

int main(){                 
	for(char *str = "54321"; *str; printf("%c,\n", *str++)){}
	// prints 5, 4, 3, 2, 1
}
```
Let's break down the code:
First of all, the for-loop structure is such that 
- we initialise a variable, 
- then check the stop condition 
- execute the code block
- then advance the counter (usually incrementing or decrementing by 1)
In this implementation
- we initialise a string containing a countdown of numbers
- we check that `str` doesn't point to the null terminator yet
- the code block is empty so nothing is executed
- the counter step is just running a command. Here we run the `printf()` command and use the postfix increment operator to advance `str`

Note that this style of programming is highly discouraged as it is very difficult to read (and debug...)

