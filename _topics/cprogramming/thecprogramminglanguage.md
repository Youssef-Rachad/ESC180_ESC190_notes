---
title: The C Programming Language
layout: default
---
> "How does the compiler itself get started? Because, of course, the C compiler is written in C!"
>
> - Brian Kernighan, EngPhys 6T4, co-author of The C Programming Language

# The C Programming Language
Generally speaking, we categorise computer languages as either high or low level depending on how much abstraction is built into the language. 

Python is an interpreted language which means that a python script is read block by block or line by line by the Python interpreter and command are executed as they are read. Note that the Python interpreter itself is a program. 

This is in contrast to C which is a compiled language. The compiler (often gcc, clang, llvm or msvc) compiles C source code into an executable that can almost directly be executed by your computer; i.e. without an interpreter. 

We call this computer hardware level instructions `machine code`, these contain very simple instructions such as moving values in memory, adding numbers and jumping to instructions based on conditions. 
Note that while the source code you write is human-readable (in theory - in practice readability depends on you), machine code is designed for the computer and is very impractical to read though it is executed much faster than interpreted code.

Another significant distinction between Python and C is the idea of low-level and high-level languages.
High-level languages like Python contain many useful abstractions which means that we can express complex ideas in the syntax and expect the Python interpreter to understand what we mean. 
```python
# For example:
for i in range(0, 2, 100) ...
```
really means that we create a variable `i` and a list containing the numbers 0 through 100 in steps of 2 then we put 0, 0+2, 0+2+2, ..., 98 into `i`. 

Another example is defining functions like
```python
def f(x):
  return x**2

# now we can write expressions like
f(5) 

# to compute 5^2 = 25
```

Low-level languages have less abstraction and express themselves more mechanically, meaning that we need to use more rudimentary concepts to achieve the same result.
```c
// For example, the same for loop is written as
for(int i = 0; i < 100; i+=2) {
  ...
```
and this requires more explicit instructions as to what we meant by a `range(0, 2, 100)`. 
The lower-levelled the language is, the more it resembles machines code at which point we really get into the 1s and 0s understandable by the hardware.
Low-level languages like C thus have the advantage of giving the programmer more control over how to implement a program.
By using low-level programming, we can avoid ambiguities (notice that in the C implementation, `i` is definitely an integer whereas in Python it was dynamically inferred) and reduces the resources required to develop our solution (this is more relevant to specific applications such as high performance computing and embedded systems but good to know about).

Relevant to ESC190: learning C will teach us a bit more about how a program manages the memory it uses (for storing/accessing variables) and stepping away from certain abstractions will push to think more critically about solving problems.
